#Agent.py
from Tools import *
from agTools import *
from random import *
import graphicDisplayGlobalVarAndFunctions as gvf
import commonVar as common

class Agent(superAgent):
    def __init__(self, number,myWorldState,
                 xPos=0, yPos=0, agType=""):

        #print xPos,yPos

        # the graph
        if gvf.getGraph() == 0: gvf.createGraph()
        common.g.add_node(self)

        # the environment

        self.agOperatingSets=[]
        self.number = number
        self.agType=agType
        self.numOfWorkers=0
        self.profit=0

        if agType == 'workers':
            common.orderedListOfNodes.append(self)
            #use to keep the order
            #in output (ex. adjacency matrix)

            # colors at http://www.w3schools.com/html/html_colornames.asp
            gvf.colors[self]="OrangeRed"

            self.employed=False

        if agType == 'entrepreneurs':
            common.orderedListOfNodes.append(self)
            #use to keep the order
            #in output (ex. adjacency matrix)

            # colors at http://www.w3schools.com/html/html_colornames.asp
            gvf.colors[self]="LawnGreen"

            self.employed=True

        self.myWorldState = myWorldState
        self.agType=agType

        # the agents
        if common.verbose: print "agent of type", self.agType, \
               "#", self.number, "has been created at", xPos, ",", yPos

        gvf.pos[self]=(xPos,yPos)
        common.g_labels[self]=str(number)
        # to be used to clone (if any)
        self.xPos=xPos
        self.yPos=yPos

    # talk
    def talk(self):
	    print self.agType, self.number

    # hireIfProfit
    def hireIfProfit(self):

        # workers do not hire
        if self.agType == "workers": return

        if self.profit<=common.hiringThreshold: return

        tmpList=[]
        for ag in self.agentList:
            if ag != self:
               if ag.agType=="workers" and not ag.employed:
                  tmpList.append(ag)

        if len(tmpList) > 0:
            hired=tmpList[randint(0,len(tmpList)-1)]

            hired.employed=True
            gvf.colors[hired]="Aqua"
            gvf.createEdge(self, hired) #self, here, is the hiring firm

        # count edges (workers) of the firm, after hiring (the values is
        # recorded, but not used directly)
        self.numOfWorkers=gvf.nx.degree(common.g, nbunch=self)
        # nbunch : iterable container, optional (default=all nodes)
        # A container of nodes. The container will be iterated through once.
        print "entrepreneur", self.number, "has", \
              self.numOfWorkers, "edge/s after hiring"

        # fireIfProfit
    def fireIfProfit(self):

        # workers do not fire
        if self.agType == "workers": return

        if self.profit<firingThreshold: return

        # the list of the employees of the firm
        entrepreneurWorkers=gvf.nx.neighbors(common.g,self)
        #print "entrepreneur", self.number, "could fire", entrepreneurWorkers

        if len(entrepreneurWorkers) > 0:
            fired=entrepreneurWorkers[randint(0,len(entrepreneurWorkers)-1)]

            gvf.colors[fired]="OrangeRed"
            fired.employed=False

            common.g_edge_labels.pop((self,fired))
            common.g.remove_edge(self, fired)

            # count edges (workers) after firing (recorded, but not used
            # directly)
            self.numOfWorkers=gvf.nx.degree(common.g, nbunch=self)
            # nbunch : iterable container, optional (default=all nodes)
            # A container of nodes. The container will be iterated through once.
            print "entrepreneur", self.number, "has", \
                  self.numOfWorkers, "edge/s after firing"



    # produce
    def produce(self):
        # the value is calutated on the fly, to be sure of accounting for
        # modifications coming from outside
        # (nbunch : iterable container, optional (default=all nodes)
        # A container of nodes. The container will be iterated through once.)
        laborForce=gvf.nx.degree(common.g, nbunch=self) + \
                   1 # +1 to account for the entrepreneur itself
        self.profit=laborForce*(common.revenuesOfSalesForEachWorker - \
                    common.wage) + gauss(0,0.5)
        #print self.profit


    # get graph
    def getGraph(self):
        return common.g


"""


    # addAFactory
    def addAFactory(self):
        if self.agType != "entrepreneurs": return

        # create a new factory cloning an existing one
        # choose randomly a factory (also a cloned one)

        toBeCloned=self
        #print toBeCloned.number

        # creating

        common.clonedN+=1
        anAgent = Agent(toBeCloned.number*100+common.clonedN,
                        self.myWorldState,
                        toBeCloned.xPos+modPosition(),
                        toBeCloned.yPos+modPosition(),
                        agType=toBeCloned.agType,
                        sector=toBeCloned.sector)
        self.agentList.append(anAgent)
        if common.verbose: print "Factory", self.number, "has created factory #",\
                                  anAgent.number,"in sector",anAgent.sector

    # remove itself
    def removeItself(self):
        if self.agType != "entrepreneurs": return

        toBeRemoved=self
        if common.verbose: print "Factory #",toBeRemoved.number,\
                                 "removed itself from sector",toBeRemoved.sector
        self.agentList.remove(toBeRemoved)

        #print "removeItself verification of surviving agents"
        #for i in range(len(self.agentList)):
        #    if self.agentList[i].agType=="entrepreneurs":
        #          print self.agentList[i].number,

        common.orderedListOfNodes.remove(toBeRemoved)
        #print "\nremoveItself node removed in graph", toBeRemoved, \
        #      toBeRemoved.number

        edges_toBeDropped=[]
        for edge in common.g.edges():
            if edge[0]==toBeRemoved or edge[1]==toBeRemoved:
                edges_toBeDropped.append(edge)
        if edges_toBeDropped != []:
            for edge in edges_toBeDropped:
               #print "removeItself edge removed in graph", edge
               if common.g_edge_labels.has_key(edge):
                   common.g_edge_labels.pop(edge)

        #print "removeItself previous nodes in graph", common.g.nodes()
        common.g_labels.pop(toBeRemoved)

        # remove factoryInWhichRecipeIs from all the recipes, also
        # that having just left this factory and waiting for
        # searchForSector order
        if self.agentList != []:
            for anAg in self.agentList:
                if anAg.agType=="workers" and \
                   anAg.factoryInWhichRecipeIs==self:
                       anAg.factoryInWhichRecipeIs=None

        # recipes in the waiting list
        #print "removeItself recipes in the factory before cleaning"
        #if self.recipeWaitingList != []:
        #    for aR in self.recipeWaitingList:
        #        print aR.number, aR.factoryInWhichRecipeIs,
        #        aR.content
        #else: print "None"

        if self.recipeWaitingList != []:
            for aRecipe in self.recipeWaitingList:
                aRecipe.content = []
                aRecipe.canMove=False
                #aRecipe.factoryInWhichRecipeIs=None # done above

        #print "removeItself recipes in the factory after cleaning"
        #if self.recipeWaitingList != []:
        #    for aR in self.recipeWaitingList:
        #        print aR.number, aR.factoryInWhichRecipeIs, aR.content
        #else: print "None"

        common.g.remove_node(toBeRemoved)
        #print "removeItself residual nodes in graph", common.g.nodes()


def modPosition():
    if random.randint(0,1)==0:return random.randint(-8,-6)
    else:                     return random.randint( 6, 8)
"""
