#WorldState.py
from Tools import *
import commonVar as common

class WorldState:
    def __init__(self, number):
        # the environment
        self.number = number
        #self.generalMovingProb=1 # not used in Oligopoly project
        print "World state number ", self.number, \
     	      " has been created."


    # set market price V1
    def setMarketPriceV1(self):
        # to have a price around 1
        common.price= 1.4 - 0.02 * common.totalProductionInA_TimeStep
        print "Set market price to ", common.price
        common.price10=common.price*10 #to plot


    # set market price V2
    def setMarketPriceV2(self):
        common.price= common.totalPlannedConsumptionInValueInA_TimeStep / \
                      common.totalProductionInA_TimeStep
        print "Set market price to ", common.price

    # set market price V3
    def setMarketPriceV3(self):
        shock0=random.uniform(-common.maxDemandRelativeRandomShock, \
                              common.maxDemandRelativeRandomShock)
        shock=shock0

        print "\n-------------------------------------"

        if shock >= 0:
          common.totalDemandInPrevious_TimeStep = \
             common.totalPlannedConsumptionInValueInA_TimeStep * \
             (1 + shock)
          common.price= (common.totalPlannedConsumptionInValueInA_TimeStep * \
                         (1 + shock))  \
                         / common.totalProductionInA_TimeStep
          print "Relative shock (symmetric) ", shock0
          print "Set market price to ", common.price

        if shock <  0:
          shock *=-1. #always positive, boing added to the denominator
          common.totalDemandInPrevious_TimeStep = \
              common.totalPlannedConsumptionInValueInA_TimeStep / \
              (1 + shock)
          common.price= (common.totalPlannedConsumptionInValueInA_TimeStep / \
                         (1 + shock))  \
                         / common.totalProductionInA_TimeStep
          print "Relative shock (symmetric) ", shock0
          print "Set market price to ", common.price

        print "-------------------------------------\n"


    # random shock to wages (temporary method to experiment with wages)
    def randomShockToWages(self):
          k=0.10
          shock= random.uniform(-k,k)

          if shock >= 0:
           common.wage *= (1.+shock)

          if shock < 0:
           shock *= -1.
           common.wage /= (1.+shock)
