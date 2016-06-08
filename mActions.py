from Tools import *
from Agent import *
import os
import random
import commonVar as common

def do0(address):
            self=address # if necessary
            askEachAgentInCollection(address.agentList, Agent.setNewCycleValues)

def do1(address):
            self=address # if necessary
            actionDictionary[self.actionGroup1.getName()]=self.actionGroup1

            # keep safe the original list
            address.agentListCopy=address.agentList[:]
            # never in the same order (please comment if you want to keep
            # always the same sequence
            random.shuffle(address.agentListCopy)

def createTheAgent(self,line,num,leftX,rightX,bottomY,topY,agType):
                # explicitly pass self, here we use a function

                # workers
                if agType=="workers":
                 anAgent = Agent(num, self.worldStateList[0],
	                             float(line.split()[1])+random.gauss(0,common.sigma),
	                             float(line.split()[2])+random.gauss(0,common.sigma),
	                             agType=agType)
                 self.agentList.append(anAgent)
                 anAgent.setAgentList(self.agentList)

                # entrepreneurs
                elif agType=="entrepreneurs":
                 anAgent = Agent(num, self.worldStateList[0],
                                 float(line.split()[1])+random.gauss(0,common.sigma),
                                 float(line.split()[2])+random.gauss(0,common.sigma),
                                 agType=agType)
                 self.agentList.append(anAgent)

                 anAgent.setAgentList(self.agentList) #in ModelSwarm.py


                else:
                 print "Error in file "+agType+".txt"
                 os.sys.exit(1)
