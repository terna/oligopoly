#WorldState.py
from Tools import *

class WorldState:
    def __init__(self, number):
        # the environment
        self.number = number
        self.generalMovingProb=1
        print "World state number ", self.number, \
     	      " has been created."

    # ",**d" in the parameter lists of the methods is a place holder
    # in case we use, calling the method, a dictionary as last parameter

    # set generalMovingProb
    def setGeneralMovingProb(self,**d):
        if d.has_key("generalMovingProb"):
            self.generalMovingProb=d["generalMovingProb"]
        else:
            print "*********** key 'generalMovingProb' is not defined"
            self.generalMovingProb=1

    # get generalMovingProb
    def getGeneralMovingProb(self):
        return self.generalMovingProb
