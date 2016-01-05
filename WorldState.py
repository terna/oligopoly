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
        common.price10=common.price*10 #to plot
