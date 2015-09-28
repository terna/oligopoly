#WorldState.py
from Tools import *
import commonVar as common

class WorldState:
    def __init__(self, number):
        # the environment
        self.number = number
        self.generalMovingProb=1
        print "World state number ", self.number, \
     	      " has been created."


    # set market price
    def setMarketPrice(self):
        # to have a price around 1
        common.price= 1.4 - 0.02 * common.totalProductionInA_TimeStep
        print "Set market price to ", common.price
