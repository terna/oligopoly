from Tools import *
from Agent import *
import time
import csv
import graphicDisplayGlobalVarAndFunctions as gvf
import commonVar as common
import pandas as pd

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

            elif subStep == "collectStructuralData":
              collectStructuralData(address.modelSwarm.agentList,common.cycle)
              return True

            elif subStep == "collectTimeSeries":
              collectTimeSeries(address.modelSwarm.agentList,common.cycle)
              return True

            elif subStep == "visualizePlot":
              visualizePlot()
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
                    # += and ; as first character because a first part
                    # of the string toBeExecuted is already defined in
                    # commonVar.py
                    common.toBeExecuted+=";gvf.plt.figure(2);gvf.plt.close()"

            else: return False



# collect Structural Data
def collectStructuralData(aL,t):
    #creating the dataframe
    try: common.str_df
    except:
       common.str_df = pd.DataFrame(columns=\
         ['entrepreneurs','workers'])
       print "\nCreation of fhe structural dataframe\n"
       #print common.str_df

    nWorkers=0
    nEntrepreneurs=0
    for ag in aL:
        if ag.agType=="entrepreneurs":
            nEntrepreneurs+=1
        if ag.agType=="workers":
            nWorkers+=1
    #print nEntrepreneurs, nWorkers
    str_df2 = pd.DataFrame([[nEntrepreneurs, nWorkers]], \
              columns=['entrepreneurs','workers'])
    #print str_df2

    common.str_df=common.str_df.append(str_df2,ignore_index=True)
    #print common.str_df #warning: here the row index starts from 0
                         #(correctly in this case, being initial data
                         #in each period)



## collect time series
def collectTimeSeries(aL,t):

    #creating the dataframe
    try: common.ts_df
    except:
       common.ts_df = pd.DataFrame(columns=\
         ['unemployed','totalProfit','totalProduction','plannedProduction',\
          'price','wage'])
       print "\nCreation of fhe time series dataframe\n"
       #print common.ts_df

    unemployed=0
    totalProfit=0
    totalPlannedProduction=0
    for ag in aL:
       if not ag.employed: unemployed+=1
       if ag.agType == "entrepreneurs":
           totalProfit+=ag.profit
           totalPlannedProduction+=ag.plannedProduction

    ts_df2 = pd.DataFrame([[unemployed, totalProfit, \
                         common.totalProductionInA_TimeStep, \
                         totalPlannedProduction, \
                         common.price, common.wage]], \
    columns=['unemployed','totalProfit','totalProduction','plannedProduction',\
             'price','wage'])
    #print ts_df2

    common.ts_df=common.ts_df.append(ts_df2,ignore_index=True)
    #print common.ts_df #warning: here the row index starts from 0


##graphical function
def visualizePlot():

    #Matplotlib colors
    #http://matplotlib.org/api/colors_api.html

    #html colors
    #http://www.w3schools.com/html/html_colornames.asp


    if common.cycle == 1 and \
       (not common.IPython or common.graphicStatus=="PythonViaTerminal"):
       # the or is about ipython running in a terminal
       gvf.plt.figure(2)
       mngr2=gvf.plt.get_current_fig_manager()
       mngr2.window.wm_geometry("+0+0")
       mngr2.set_window_title("Time series")

       params = {'legend.fontsize': 10}
       gvf.plt.rcParams.update(params)

    if not common.IPython or common.graphicStatus=="PythonViaTerminal":
       # the or is about ipython running in a terminal
       gvf.plt.ion()
       f2=gvf.plt.figure(2)
       gvf.plt.clf()
       myax = f2.gca()
       #myax.set_autoscale_on(True)

       ts_dfOut=common.ts_df
       #set index to start from 1
       ts_dfOut.index += 1
       myPlot=ts_dfOut.plot(secondary_y=['price','wage'],\
                  marker="*",color=["OrangeRed","LawnGreen",\
                                    "Blue","Violet","Gray","Brown"],\
                                    ax=myax)
       myPlot.set_ylabel('unemployed, totalProfit, totalProduction, plannedProduction')
       myPlot.right_ax.set_ylabel('price, wage')
       myPlot.legend(loc='upper left')
       myPlot.axes.right_ax.legend(loc='lower right')


    if common.IPython and not common.graphicStatus=="PythonViaTerminal":
       # the and not is about ipython running in a terminal
       f2=gvf.plt.figure()
       myax = f2.gca()
       #myax.set_autoscale_on(True)
       gvf.plt.title('Time Series')

       ts_dfOut=common.ts_df
       #set index to start from 1
       ts_dfOut.index += 1
       myPlot=ts_dfOut.plot(secondary_y=['price','wage'],\
                  marker="*",color=["OrangeRed","LawnGreen",\
                                    "Blue","Violet","Gray","Brown"],\
                                    ax=myax)
       myPlot.set_ylabel('unemployed, totalProfit, totalProduction, plannedProduction')
       myPlot.right_ax.set_ylabel('price, wage')
       myPlot.legend(loc='upper left')
       myPlot.axes.right_ax.legend(loc='lower right')


    if not common.IPython or common.graphicStatus=="PythonViaTerminal":
       # the or is about ipython running in a terminal
       gvf.plt.figure(1)
       #gvf.plt.show()
       #gvf.plt.pause(0.01) #to display the sequence

    if common.IPython and not common.graphicStatus=="PythonViaTerminal":
       # the and not is about ipython running in a terminal
       gvf.plt.show()



##saving time series via toBeExecuted in commonVar.py
def saveTimeSeries():
    tt=time.strftime("%Y%m%d-%H:%M:%S")

    fileName=tt+"_ts.csv"
    csvfile=open(common.pro+"/"+fileName,"w")
    common.ts_df.to_csv(csvfile,index_label=False,index=False)
    csvfile.close()

    fileName=tt+"_str.csv"
    csvfile=open(common.pro+"/"+fileName,"w")
    common.str_df.to_csv(csvfile,index_label=False,index=False)
    csvfile.close()

    print "two files with date and hour", tt, "written in oligopoly folder."


"""
###########################################################################

##graphical function
def visualizePlotFirstVersion(aL,t):
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
    global x, y1, y2, y3, y4, y5, y5base, y6, y6base, line1, line2, line3, line4, line5, line6, ax

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
          y5base = [common.price]
          y5 = [common.price]
          if len(aL)>=100  :y5 = [common.price*10]
          if len(aL)>=1000 :y5 = [common.price*100]
          if len(aL)>=10000:y5 = [common.price*1000]
          #print "************** unemployed", y1
          #print "************** price", y5
          y6base = [common.wage]
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
          gvf.plt.pause(0.01) #to display the sequence
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

          y5base.append(common.price)
          if                      len(aL)<100  : y5.append(common.price)
          elif len(aL)>=100   and len(aL)<1000 : y5.append(common.price*10)
          elif len(aL)>=1000  and len(aL)<10000: y5.append(common.price*100)
          elif len(aL)>=10000                  : y5.append(common.price*1000)
          #print "************** unemployed", y1
          #print "************** price", y5

          y6base.append(common.wage)
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
          gvf.plt.pause(0.01) #to display the sequence
      if common.IPython and not common.graphicStatus=="PythonViaTerminal":
       # the and not is about ipython running in a terminal
          gvf.plt.show()



##saving time series via toBeExecuted in commonVar.py
def saveTimeSeriesFirstVersion():
    fileName=time.strftime("%Y%m%d-%H:%M:%S.csv")
    csvfile=open(common.pro+"/"+fileName,"w")
    csv_writer=csv.writer(csvfile, delimiter=',')

    csv_writer.writerow(['unemployed','totalProfit','totalProduction',\
                         'plannedProduction','price','wage'])

    for i in range(len(y1)):
        csv_writer.writerow([y1[i],y2[i],y3[i],y4[i],y5base[i],y6base[i]])

    csvfile.close()
    print "file",fileName, "written in oligopoly folder."
"""
