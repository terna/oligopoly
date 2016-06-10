#commonVar.py

projectVersion = 4

build = "20160610"

# the time is set by ObserverSwarm with
# common.cycle=1
# in the benginning

prune=False
pruneThreshold=0

g=0             #this variable will contain the address of the graph
g_labels=0      #this variable will contain the address of the labels
g_edge_labels=0 #this variable will contain the address of the labels of the edges

btwn=0 # this variable will contain the betweenness centrality indicators
clsn=0 # this variable will contain the closeness centrality indicators



orderedListOfNodes=[]
verbose=False
clonedN=0

#sigma of the normal distribution used in randomize the position of the agents/nodes
#sigma=0.7
sigma=1.2

#size of the nodes
nsize=150

#demand funtion paramenters (1) entrepreneurs as consumers (2) employed workers
#(3) unemployed workers
#with Ci = ai + bi Y + u
#u=N(0,consumptionErrorSD)
consumptionRandomComponentSD=0.3

#(1)
a1=0.4
b1=0.55
#Y1=profit(t-1)+wage NB no negative consumption if profit(t-1) < 0

#(2)
a2=0.3
b2=0.65
#Y2=wage

#(3)
socialWelfareCompensation=0.3
a3=0
b3=1
#Y3=socialWelfareCompensation

#wages and revenues
wage=1
revenuesOfSalesForEachWorker=1.005

#labor productivity
laborProductivity=1

#thresholds (for Version 0)
hiringThreshold=0
firingThreshold=0

#macro variables
totalProductionInA_TimeStep=0
totalPlannedConsumptionInValueInA_TimeStep=0

#Poisson mean in makeProoductionPlan, will be modified in paramenters.py
#in the function loadParameters
Lambda=5

#to internally calculate the Poisson mean (Lambda) in makeProoductionPlan
#for time=1 in V3 we use the ratio rho
rho=0.8

#threshold toEntrepreneur
thresholdToEntrepreneur=0.20
extraCostsDuration=3
newEntrantExtraCosts=2.0

randomComponentOfPlannedProduction=0.10

absoluteBarrierToBecomeEntrepreneur=20

maxDemandRelativeRandomShock=0.20

#threshold toWorker
thresholdToWorker=-0.20

fullEmploymentThreshold=0.05
wageStepInFullEmployment=0.10
fullEmploymentStatus=False

nodeNumbersInGraph=False
