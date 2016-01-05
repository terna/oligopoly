#commonVar.py

projectVersion = 1.1

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
sigma=0.7

#size of the nodes
nsize=150

#demand funtion paramenters (1) entrepreneurs as consumers (2) employed workers
#(3) unemployed workers
#with Ci = ai + bi Y + u
#u=N(0,consumptionErrorSD)
consumptionErrorSD=0.05

#(1)
a1=1
b1=0.6
#Y1=profit(t-1)+wage NB no negative consumption if profit(t-1) < 0

#(2)
a2=0.2
b2=0.7
#Y2=wage

#(3)
socialWelfareCompensation=0.3
#che cosa stampiamo?
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

#Poisson mean in plannedProduction
Lambda=5
