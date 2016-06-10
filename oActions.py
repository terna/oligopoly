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
                if not common.IPython or common.graphicStatus=="PythonViaTerminal":
                    # the or is about ipython running in a terminal
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
    global x, y1, y2, y3, y4, y5, y6, line1, line2, line3, line4, line5, line6, ax

    if not common.IPython or common.graphicStatus=="PythonViaTerminal":
       # the or is about ipython running in a terminal
       gvf.plt.figure(2)
       mngr2=gvf.plt.get_current_fig_manager()
       mngr2.window.wm_geometry("+0+0")
       mngr2.set_window_title("Time series")


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
      if y4[0] > 0: # if => to avoid error in Version 0 schedule
          y5 = [common.price]
          if len(aL)>=100  :y5 = [common.price*10]
          if len(aL)>=1000 :y5 = [common.price*100]
          if len(aL)>=10000:y5 = [common.price*1000]
          #print "************** unemployed", y1
          #print "************** price", y5
          y6 = [common.wage]
          if len(aL)>=100  :y6 = [common.wage*10]
          if len(aL)>=1000 :y6 = [common.wage*100]
          if len(aL)>=10000:y6 = [common.wage*1000]

      if not common.IPython or common.graphicStatus=="PythonViaTerminal":
       # the or is about ipython running in a terminal
       gvf.plt.ion()
       f2=gvf.plt.figure(2)
       ax = f2.gca()
       ax.set_autoscale_on(True)
      if common.IPython and not common.graphicStatus=="PythonViaTerminal":
       # the and not is about ipython running in a terminal
        f2=gvf.plt.figure()
        ax = f2.gca()
        ax.set_autoscale_on(True)
        gvf.plt.title('Time Series')
      line1, = ax.plot(x, y1,label='unemployed',color='OrangeRed', marker="*")
      line2, = ax.plot(x, y2,label='totalProfit',color='LawnGreen', marker="*")
      line3, = ax.plot(x, y3,label='totalProduction',color='Blue', marker="*")
      if y4[0] > 0:
          line4, = ax.plot(x, y4,label='plannedProduction',color='Violet', marker="*")

          if                    len(aL)<100   :
            line5, = ax.plot(x, y5,label='price',color='Gray', marker="*")
          elif   len(aL)>=100 and len(aL)<1000  :
            line5, = ax.plot(x, y5,label='price*10',color='Gray', marker="*")
          elif len(aL)>=1000 and len(aL)<10000:
            line5, = ax.plot(x, y5,label='price*100',color='Gray', marker="*")
          elif len(aL)>=10000                 :
            line5, = ax.plot(x, y5,label='price*1000',color='Gray', marker="*")

          if                    len(aL)<100   :
            line6, = ax.plot(x, y6,label='wage',color='Brown', marker="*")
          elif   len(aL)>=100 and len(aL)<1000  :
            line6, = ax.plot(x, y6,label='wage*10',color='Brown', marker="*")
          elif len(aL)>=1000 and len(aL)<10000:
            line6, = ax.plot(x, y6,label='wage*100',color='Brown', marker="*")
          elif len(aL)>=10000                 :
            line6, = ax.plot(x, y6,label='wage*1000',color='Brown', marker="*")

      ax.legend(loc=6)
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
          line6.set_xdata(x)
          line6.set_ydata(y6)

      #loc values at http://matplotlib.org/1.3.1/users/legend_guide.html
      if not common.IPython or common.graphicStatus=="PythonViaTerminal":
      # the or is about ipython running in a terminal
          gvf.plt.figure(1)
          gvf.plt.show()
      if common.IPython and not common.graphicStatus=="PythonViaTerminal":
       # the and not is about ipython running in a terminal
          gvf.plt.show()

    else:
      if common.IPython and not common.graphicStatus=="PythonViaTerminal":
              # the and not is about ipython running in a terminal
              f2=gvf.plt.figure()
              ax = f2.gca()
              ax.set_autoscale_on(True)

              line1, = ax.plot(x, y1,label='unemployed',color='OrangeRed', marker="*")
              line2, = ax.plot(x, y2,label='totalProfit',color='LawnGreen', marker="*")
              line3, = ax.plot(x, y3,label='totalProduction',color='Blue', marker="*")
              if y4[0] > 0:
                line4, = ax.plot(x, y4,label='plannedProduction',color='Violet', marker="*")
                #line5, = ax.plot(x, y5,label='price',color='Gray', marker="*")
                #line6, = ax.plot(x, y6,label='wage',color='Brown', marker="*")
                if                    len(aL)<100   :
                  line5, = ax.plot(x, y5,label='price',color='Gray', marker="*")
                elif   len(aL)>=100 and len(aL)<1000  :
                  line5, = ax.plot(x, y5,label='price*10',color='Gray', marker="*")
                elif len(aL)>=1000 and len(aL)<10000:
                  line5, = ax.plot(x, y5,label='price*100',color='Gray', marker="*")
                elif len(aL)>=10000                 :
                  line5, = ax.plot(x, y5,label='price*1000',color='Gray', marker="*")

                if                    len(aL)<100   :
                  line6, = ax.plot(x, y6,label='wage',color='Brown', marker="*")
                elif   len(aL)>=100 and len(aL)<1000  :
                  line6, = ax.plot(x, y6,label='wage*10',color='Brown', marker="*")
                elif len(aL)>=1000 and len(aL)<10000:
                  line6, = ax.plot(x, y6,label='wage*100',color='Brown', marker="*")
                elif len(aL)>=10000                 :
                  line6, = ax.plot(x, y6,label='wage*1000',color='Brown', marker="*")

              ax.legend(loc=6)
              gvf.plt.title('Time Series')
      x.append(t)
      y1.append(unemployed)
      y2.append(totalProfit)
      y3.append(common.totalProductionInA_TimeStep)
      if y4[0] > 0:
          y4.append(totalPlannedProduction)

          if                      len(aL)<100  : y5.append(common.price)
          elif len(aL)>=100   and len(aL)<1000 : y5.append(common.price*10)
          elif len(aL)>=1000  and len(aL)<10000: y5.append(common.price*100)
          elif len(aL)>=10000                  : y5.append(common.price*1000)
          #print "************** unemployed", y1
          #print "************** price", y5

          if                      len(aL)<100  : y6.append(common.wage)
          elif len(aL)>=100   and len(aL)<1000 : y6.append(common.wage*10)
          elif len(aL)>=1000  and len(aL)<10000: y6.append(common.wage*100)
          elif len(aL)>=10000                  : y6.append(common.wage*1000)


      if not common.IPython or common.graphicStatus=="PythonViaTerminal":
          # the or is about ipython running in a terminal
          gvf.plt.figure(2)
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
          line6.set_xdata(x)
          line6.set_ydata(y6)
      ax.relim()
      ax.autoscale_view(True,True,True)
      if not common.IPython or common.graphicStatus=="PythonViaTerminal":
          # the or is about ipython running in a terminal
          gvf.plt.figure(1)
          gvf.plt.show()
      if common.IPython and not common.graphicStatus=="PythonViaTerminal":
       # the and not is about ipython running in a terminal
          gvf.plt.show()
