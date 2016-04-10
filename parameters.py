#parameters.py
from Tools import *
import commonVar as common

import networkx as nx
import matplotlib as mplt

def loadParameters(self):

  print "NetworkX version %s running" % nx.__version__
  print "Matplotlib version %s running\n" % mplt.__version__

  nxv=nx.__version__.split('.')
  vOK=False
  if int(nxv[0])>1: vOK=True
  if len(nxv)>=2:
      if int(nxv[0])==1 and int(nxv[1])>9: vOK=True
  if len(nxv)>=3:
      if int(nxv[0])==1 and int(nxv[1])==9 and int(nxv[2])>=1: vOK=True

  if not vOK:
		print "NetworkX 1.9.1 or greater required"
		os.sys.exit(1)
  #sigma of the normal distribution used in randomize the position of the agents/nodes
  print "sigma of the normal distribution used in randomizing the position of the agents/nodes ", common.sigma

  mySeed = input("random number seed (1 to get it from the clock) ")
  if mySeed == 1:
        random.seed()
  else:
        random.seed(mySeed)

  self.nAgents = 0
  print "No 'bland' agents"

  #self.worldXSize= input("X size of the world? ")
  self.worldXSize=1
  #print "X size of the world not relevant"

  #self.worldYSize= input("Y size of the world? ")
  self.worldYSize=50
  #print "y size of the world not relevant"

  # Version 1 thresholds
  print "Versions 1 hiringThreshold", common.hiringThreshold, \
                   "firingThreshold", common.firingThreshold

  # wages
  print "wage base", common.wage

  # revenue of sales per worker (version 0)
  print "revenues of sales for each worker in Version 0", \
        common.revenuesOfSalesForEachWorker

  # laboor productivity
  print "labor productivity", common.laborProductivity

  #Poisson mean in plannedProduction
  print "Poisson distribution mean in planned production (not used in V.0);"
  tmp=raw_input(
     "suggested Lambda=5 (enter to confirm or input a number) ")
  try: common.Lambda=int(tmp)
  except: pass
  print "Resulting value", common.Lambda


  # cycles
  self.nCycles = input("How many cycles? (0 = exit) ")

  v = raw_input("verbose? (y/[n]) ")
  if v=="y" or v=="Y":
    common.verbose=True #predefined False
