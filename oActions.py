from Tools import *
from Agent import *
import graphicDisplayGlobalVarAndFunctions as gvf
import commonVar as common

def do1b(address):

    # having the map of the agent
    agL=[]
    for ag in address.modelSwarm.agentList:
        agL.append(ag.number)
    agL.sort()
    #print "\noActions before drawGraph agents", agL
    #print "oActions before drawGraph nodes", common.g.nodes()

    #basic action to visualize the networkX output
    gvf.openClearNetworkXdisplay()
    gvf.drawGraph()


def do2a(address,cycle):
            self=address # if necessary

            # ask each agent, without parameters

            print "Time = ", cycle, "ask all agents to report position"
            askEachAgentInCollection(address.modelSwarm.getAgentList(),Agent.reportPosition)


def do2b(address,cycle):
            self=address # if necessary

            # ask a single agent, without parameters
            print "Time = ",cycle,"ask first agent to report position"
            if address.modelSwarm.getAgentList() != []:
                askAgent(address.modelSwarm.getAgentList()[0],\
                         Agent.reportPosition)

def otherSubSteps(subStep, address):

            if subStep == "pause":
              raw_input ("Hit enter key to continue")
              return True

            elif subStep == "visualizePlot":
              visualizePlot(address.modelSwarm.agentList,common.cycle)
              return True

            elif subStep == "prune":
              common.prune=True
              newValue=raw_input (("Prune links with weight < %d\n"+\
                                   "Enter to confirm "+\
                                   "or introduce a new level: ") % \
                                       common.pruneThreshold)
              if newValue !="": common.pruneThreshold=int(newValue)
              return True

            # this subStep performs only partially the "end" item; the execution
            # will continue in ObserverSwarm.py
            elif subStep == "end":
                if not common.IPython:
                    common.toBeExecuted="gvf.plt.figure(2);gvf.plt.close()"

            else: return False

##graphical function
def visualizePlot(aL,t):
    #print "visualizePlot acting with", len(aL)-1, "agents, at time step", t
    unemployed=0
    totalProfit=0
    totalPlannedProduction=0

    for ag in aL:
       if not ag.employed: unemployed+=1
       if ag.agType == "entrepreneurs":
           totalProfit+=ag.profit
           totalPlannedProduction+=ag.plannedProduction # -100 if not used
    #print "unemployed",unemployed, "totalProfit", totalProfit, \
    #      "totalProduction", common.totalProductionInA_TimeStep


    # this global is a trick to avoid the 'not referenced' error being the
    # def of the variables within an if
    global x, y1, y2, y3, y4, y5, line1, line2, line3, line4, line5, ax

    if not common.IPython:
       gvf.plt.figure(2)
       mngr2=gvf.plt.get_current_fig_manager()
       mngr2.window.wm_geometry("+650+0")
       mngr2.set_window_title("Time series")

    """
    if common.IPython:
       gvf.plt.figure("1. Links Entrepreneurs - Workers; 2. Time Series ")
       gvf.plt.subplot(2,1,2)
    """

    #Matplotlib colors
    #http://matplotlib.org/api/colors_api.html

    #html colors
    #http://www.w3schools.com/html/html_colornames.asp

    if t == 1:
      x =  [1]
      y1 = [unemployed]
      y2 = [totalProfit]
      y3 = [common.totalProductionInA_TimeStep]
      y4 = [totalPlannedProduction]
<<<<<<< HEAD
      if y4[0] > 0: y5 = [common.price10] # to avoid error in Version 0 schedule
      gvf.plt.ion()
      f2=gvf.plt.figure(2)
      ax = f2.gca()
      ax.set_autoscale_on(True)
=======
      if y4[0] > 0: y5 = [common.price] # to avoid error in Version 0 schedule
      if not common.IPython:
       gvf.plt.ion()
       f2=gvf.plt.figure(2)
       ax = f2.gca()
       ax.set_autoscale_on(True)
      if common.IPython:
        f2=gvf.plt.figure()
        ax = f2.gca()
        ax.set_autoscale_on(True)

>>>>>>> V1
      line1, = ax.plot(x, y1,label='unemployed',color='OrangeRed')
      line2, = ax.plot(x, y2,label='totalProfit',color='LawnGreen')
      line3, = ax.plot(x, y3,label='totalProduction',color='Blue')
      if y4[0] > 0:
          line4, = ax.plot(x, y4,label='plannedProduction',color='Violet')
<<<<<<< HEAD
          line5, = ax.plot(x, y4,label='price10',color='Gray')
      #loc values at http://matplotlib.org/1.3.1/users/legend_guide.html
      ax.legend(loc=6)
      gvf.plt.draw()
      gvf.plt.figure(1)
=======
          line5, = ax.plot(x, y4,label='price',color='Gray')
      ax.legend()
      if not common.IPython: gvf.plt.figure(1)
      if common.IPython: gvf.plt.show()
>>>>>>> V1

    else:
      if common.IPython:
              f2=gvf.plt.figure()
              ax = f2.gca()
              ax.set_autoscale_on(True)

              line1, = ax.plot(x, y1,label='unemployed',color='OrangeRed')
              line2, = ax.plot(x, y2,label='totalProfit',color='LawnGreen')
              line3, = ax.plot(x, y3,label='totalProduction',color='Blue')
              if y4[0] > 0:
                line4, = ax.plot(x, y4,label='plannedProduction',color='Violet')
                line5, = ax.plot(x, y4,label='price',color='Gray')
              ax.legend()
      x.append(t)
      y1.append(unemployed)
      y2.append(totalProfit)
      y3.append(common.totalProductionInA_TimeStep)
      if y4[0] > 0:
          y4.append(totalPlannedProduction)
<<<<<<< HEAD
          y5.append(common.price10)
      gvf.plt.figure(2)
=======
          y5.append(common.price)
      if not common.IPython: gvf.plt.figure(2)
>>>>>>> V1
      line1.set_xdata(x)
      line1.set_ydata(y1)
      line2.set_xdata(x)
      line2.set_ydata(y2)
      line3.set_xdata(x)
      line3.set_ydata(y3)
      if y4[0] > 0:
          line4.set_xdata(x)
          line4.set_ydata(y4)
          line5.set_xdata(x)
          line5.set_ydata(y5)
      ax.relim()
      ax.autoscale_view(True,True,True)
      if not common.IPython: gvf.plt.figure(1)
      if common.IPython: gvf.plt.show()
