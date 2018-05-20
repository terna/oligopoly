# commonVar.py

projectVersion = "6 tmp few workers and h. phase at 1"

build = "20180419"

debug = False

# function for the management of the paramenters
def setVar():
    #print(nameValues)
    globals().update(nameValues)

def check(nn):
    try:
        globals()[nn]
        return (True, globals()[nn])
    except BaseException:
        return (False, False)



# controlling the existence of an agent with number==0 used by reset
# step in modelActions.txt
agent1existing = False

# the time is set by ObserverSwarm with
# common.cycle=1
# in the benginning

prune = False
pruneThreshold = 0

g = 0  # this variable will contain the address of the graph
g_labels = 0  # this variable will contain the address of the labels
g_edge_labels = 0  # this variable will contain the address of the labels of the edges

btwn = 0  # this variable will contain the betweenness centrality indicators
clsn = 0  # this variable will contain the closeness centrality indicators


orderedListOfNodes = []
verbose = False
clonedN = 0

# sigma of the normal distribution used in randomize the position of the agents/nodes
# sigma=0.7
sigma = 1.2

# size of the nodes
nsize = 150

# demand funtion paramenters (1) entrepreneurs as consumers (2) employed workers
#(3) unemployed workers
# with Ci = ai + bi Y + u
# u=N(0,consumptionErrorSD)
consumptionRandomComponentSD = 0.3

#(1)
a1 = 0.4
b1 = 0.6 #0.55
# Y1=profit(t-1)+wage NB no negative consumption if profit(t-1) < 0

#(2)
a2 = 0.3
b2 = 0.7 #0.65
# Y2=wage

#(3)
socialWelfareCompensation = 0.3
a3 = 0
b3 = 1
# Y3=socialWelfareCompensation

#wages and revenues
wage = 1.

fullEmploymentThreshold = 0.05
wageStepInFullEmployment = 0.10
fullEmploymentStatus = False

wageAddendum = 0
maxAcceptableOligopolistRelativeIncrement = 0.30 # was 0.20 in the paper
temporaryRelativeWageIncrementAsBarrier = 0.15


revenuesOfSalesForEachWorker = 1.005

# work troubles, production correction Psi, relative value
productionCorrectionPsi = 0.10
# does it generate a cut of the wages
wageCutForWorkTroubles = False
# price penalty for work troubles
penaltyValue = 0  # was 0.10

# labor productivity
laborProductivity = 1

# thresholds (for Version 0)
hiringThreshold = 0
firingThreshold = 0

# macro variables
totalProductionInA_TimeStep = 0
totalPlannedConsumptionInValueInA_TimeStep = 0
totalConsumptionInQuantityInA_TimeStep = 0
totalConsumptionInQuantityInPrevious_TimeStep = 0

# Poisson mean in makeProoductionPlan, will be modified in paramenters.py
# in the function loadParameters
nu = 5

# to internally calculate the Poisson mean (nu) in makeProoductionPlan
# for time=1 in V3 we use the ratio rho
rho = 0.9

# threshold toEntrepreneur
thresholdToEntrepreneur = 0.05 # was 0.15 in the paper  # was 0.20 in the init. trials
extraCostsDuration = 3
newEntrantExtraCosts = 60  # was 100.0 # was 2.0

randomComponentOfPlannedProduction = 0.10

# max new entrant number in a time step
absoluteBarrierToBecomeEntrepreneur = 20

maxDemandRelativeRandomShock = 0.15  # was 0.10 #was 0.20

# threshold toWorker
thresholdToWorker = -0.25 # -0.20 was the value in the paper

# start the hayekian market at cycle ... (NB > 0)
startHayekianMarket = 1 #6

# Range of the correction of agent starting prices (h. market)
initShock = 0.3
# initial asymmetry in individual starting prices (h. market)
initShift = 0.1

# Range of the correction of agent current price (h. market), as buyer/seller
runningShockB = 0.05
runningShockS = 0.05
# current asymmetry in individual price correction (h. market)
runningAsymmetryB = 0.9
runningAsymmetryS = 0.9

nodeNumbersInGraph = False

# step to be executed at end (plus an optional second part added
# within oActions.py)
toBeExecuted = "saveData()"

# specialAction in observerActions.txt is evatulated to "makeSpecialAction"
# defined in oActions.py
specialAction = "makeSpecialAction()"
# with
file_modPars=False
# as feasibility control

# pars definitions to use them in the table of the modified pars
parsDict={}

# to report hayekian price st. dev. if not still calculated
hPriceSd = -100 # -100 will not appear in graphs

# predefintion
totalConsumptionInQuantityInPrevious1_TimeStep=0
