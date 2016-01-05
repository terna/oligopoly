#Agent.py
from Tools import *
from agTools import *
from random import *
import graphicDisplayGlobalVarAndFunctions as gvf
import commonVar as common
import numpy.random as npr

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
        self.plannedProduction=-100 #not used in plots if -100
        self.consumption=0
        self.employed=False

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

    # reset values, redefining the method of agTools.py in $$slapp$$
    def setNewCycleValues(self):
        common.totalProductionInA_TimeStep=0
        common.totalPlannedConsumptionInValueInA_TimeStep=0

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

    def hireFireWithProduction(self):

        # workers do not hire/fire
        if self.agType == "workers": return

        # to decide to hire/fire we need to know the number of employees
        # the value is calcutated on the fly, to be sure of accounting for
        # modifications coming from outside
        # (nbunch : iterable container, optional (default=all nodes)
        # A container of nodes. The container will be iterated through once.)

        laborForce0=gvf.nx.degree(common.g, nbunch=self) + \
                           1 # +1 to account for the entrepreneur itself

        # required labor force
        laborForceRequired=int(
                    self.plannedProduction/common.laborProductivity)

        # no action
        if laborForce0 == laborForceRequired: return

        # hire
        if laborForce0 < laborForceRequired:
            n = laborForceRequired - laborForce0
            tmpList=[]
            for ag in self.agentList:
              if ag != self:
                 if ag.agType=="workers" and not ag.employed:
                    tmpList.append(ag)

            if len(tmpList) > 0:
                k = min(n, len(tmpList))
                shuffle(tmpList)
                for i in range(k):
                    hired=tmpList[i]
                    hired.employed=True
                    gvf.colors[hired]="Aqua"
                    gvf.createEdge(self, hired)
                    #self, here, is the hiring firm

            # count edges (workers) of the firm, after hiring (the values is
            # recorded, but not used directly)
            self.numOfWorkers=gvf.nx.degree(common.g, nbunch=self)
            # nbunch : iterable container, optional (default=all nodes)
            # A container of nodes. The container will be iterated through once.
            print "entrepreneur", self.number, "has", \
                  self.numOfWorkers, "edge/s after hiring"

        # fire
        if laborForce0 > laborForceRequired:
            n = laborForce0 - laborForceRequired

            # the list of the employees of the firm
            entrepreneurWorkers=gvf.nx.neighbors(common.g,self)
            #print "entrepreneur", self.number, "could fire", entrepreneurWorkers

            if len(entrepreneurWorkers) > 0: # has to be, but ...
                 shuffle(entrepreneurWorkers)
                 for i in range(n):
                    fired=entrepreneurWorkers[i]

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



    # fireIfProfit
    def fireIfProfit(self):

        # workers do not fire
        if self.agType == "workers": return

        if self.profit>=common.firingThreshold: return

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

        # this is an entrepreneur action
        if self.agType == "workers": return


        # to produce we need to know the number of employees
        # the value is calcutated on the fly, to be sure of accounting for
        # modifications coming from outside
        # (nbunch : iterable container, optional (default=all nodes)
        # A container of nodes. The container will be iterated through once.)

        laborForce=gvf.nx.degree(common.g, nbunch=self) + \
                   1 # +1 to account for the entrepreneur itself

        # productivity is set to 1 in the benginning
        self.production = common.laborProductivity * \
                          laborForce

        # totalProductionInA_TimeStep
        common.totalProductionInA_TimeStep += self.production


    # makeProductionPlan
    def makeProductionPlan(self):

        # this is an entrepreneur action
        if self.agType == "workers": return

        self.plannedProduction=npr.poisson(common.Lambda,1)[0] # 1 is the number
        # of element of the returned matrix (vector)



    # calculateProfit V0
    def evaluateProfitV0(self):

        # this is an entrepreneur action
        if self.agType == "workers": return

        # the number of pruducing workers is obtained indirectly via
        # production/laborProductivity
        #print self.production/common.laborProductivity
        self.profit=(self.production/common.laborProductivity) * \
                     (common.revenuesOfSalesForEachWorker - \
                      common.wage) + gauss(0,0.05)

    # calculateProfit
    def evaluateProfit(self):

        # this is an entrepreneur action
        if self.agType == "workers": return

        # the number of pruducing workers is obtained indirectly via
        # production/laborProductivity
        #print self.production/common.laborProductivity
        self.profit=common.price * self.production - \
                    common.wage * (self.production/common.laborProductivity)
        #print "profit", self.profit


    # compensation
    def planConsumptionInValue(self):
        self.consumption=0
        #case (1)
        #Y1=profit(t-1)+wage NB no negative consumption if profit(t-1) < 0
        # this is an entrepreneur action
        if self.agType == "entrepreneurs":
            self.consumption = common.a1 + \
                               common.b1 * (self.profit + common.wage) + \
                               gauss(0,common.consumptionErrorSD)
            if self.consumption < 0: self.consumption=0
            #profit, in V2, is at time -1 due to the sequence in schedule2.xls

        #case (2)
        #Y2=wage
        if self.agType == "workers" and self.employed:
            self.consumption = common.a2 + \
                               common.b2 * common.wage + \
                               gauss(0,common.consumptionErrorSD)

        #update totalPlannedConsumptionInValueInA_TimeStep
        common.totalPlannedConsumptionInValueInA_TimeStep+=self.consumption
        #print "C sum", common.totalPlannedConsumptionInValueInA_TimeStep


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
