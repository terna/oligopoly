#commonVar.py
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

#wages and revenues
wage=1
revenuesOfSalesForEachWorker=1.005
hiringThreshold=0
firingThreshold=0
