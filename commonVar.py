# commonVar.py

projectVersion = "6"

build = "20180926"

debug = True

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
consumptionRandomComponentSD = 0.1 # nel paper pubblicato 0.3

#(1)
a1 = 0.4
b1 = 0.55 #0.6 #0.55
# Y1=profit(t-1)+wage NB no negative consumption if profit(t-1) < 0

#(2)
a2 = 0.3
b2 = 0.65 #0.7 #0.65
# Y2=wage

#(3)
socialWelfareCompensation = 0.70 #0.60 #0.75 #0.70 #0.3
a3 = 0
b3 = 1
# Y3=socialWelfareCompensation

# quota of the unspent consumption capability coming from the past to be
# added to the corrent consumption plan [0, 1]
reUseUnspentConsumptionCapability= 0.5 #0 #0.5 #1

#wages and revenues
wageBase = 1.
wage = wageBase

fullEmploymentThreshold = 0.05
wageStepInFullEmployment = 0.10

wageAddendum = 0
wageCorrectionInCycle=0
maxAcceptableOligopolistRelativeIncrement = 0.20 #0.30 # was 0.20 in the paper
cumulativelyMeasuringNewEntrantNumber=True
temporaryRelativeWageIncrementAsBarrier = 0.15
ReferenceLevel=0 # to avoit a referenced before assignment error in WorldState


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
thresholdToEntrepreneur = 0.10 #0.08 #0.085 #0.09 #0.10 #0.075 #0.05 #0.05 #0.15 #0.10 #0.075 #0.045 #0.075 # was 0.15 in the paper  # was 0.20 in the init. trials
extraCostsDuration = 5 #3
newEntrantExtraCosts = 60  # was 100.0 # was 2.0

randomComponentOfPlannedProduction = 0.10

# max new entrant number in a time step
absoluteBarrierToBecomeEntrepreneur = 10 #20

maxDemandRelativeRandomShock = 0.15  # was 0.10 #was 0.20

# threshold toWorker
thresholdToWorker = -0.25 # -0.20 was the value in the paper


# price warming has to be done only once (hayekian market)
priceWarmingDone = False

# start the hayekian market at cycle ... (NB > 0)
startHayekianMarket = 1 #3 #1 #6

# use full hayekian paradigm or quasi hayekian paradigm?
# for explanations see the document
# "Oligopoly: the Making of the Simulation Model", section
# "Version 6, the hayekian market"
hParadigm= "quasi" #"noPriceMod" #"full" #"quasi"

# thresholds to decide
# to lower the prices in the 'quasi' hParadigm
soldThreshold1=0.80
# to raise the prices in the 'quasi' hParadigm
soldThreshold2=0.90


# 'quasi' hParadigm, decreasingRateRange
decreasingRateRange=-0.20

# 'quasi' hParadigm, increasingRateRange
increasingRateRange=0.20

# Range of the correction of agent starting prices (h. market)
initShock = 0.10 #0.2 #0.1 #0.3
# initial shift in individual starting prices (h. market)
initShift = -0.15 #-0.10 #0.5 #0.1

# Range of the correction of agent current price (h. market), as buyer/seller
runningShockB = 0.20 #0.10 #0.05
runningShockS = 0.05 #0.02 #0.20 #0.05 #0.10 #0.05
# current shift in individual price correction (h. market)
runningShiftB = 0.1 #0 #0.1
runningShiftS = 0.1 #0 #0.1

# a jump in prices made by the sellers
jump= 0.10 #0.05 #0.30 #0.20 #0.10
pJump=0.10 # 0.05

# Choosing among different quasi hayekian strategies in modifiying seller
# hPriceSd

quasiHchoice="unsold" # three choices: unsold, profictDirect, profitInverse

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

#instruments
startingHayekianCommonPriceAlreadyWritten=False

# infos on substep management
checkResConsUnsoldProd=True

withinASubstep=False
currentCycle=0
subStepCounter=0
