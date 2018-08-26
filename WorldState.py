# WorldState.py
from Tools import *
import commonVar as common
import statistics

def checkHayekianPrices(a):
    # list a not empty
    if a!=[]: m = statistics.mean(a)
    else: m = -100 # -100 will not appear in graphs
    # and with at least one element
    if len(a)>1: sd = statistics.stdev(a)
    else: sd=-100 # -100 will not appear in graphs
    return (m,sd)


class WorldState(object):
    def __init__(self):
        # the environment
        print("World state has been created.")

    # set market price V1
    def setMarketPriceV1(self):
        # to have a price around 1
        common.price = 1.4 - 0.02 * common.totalProductionInA_TimeStep
        print("Set market price to ", common.price)
        common.price10 = common.price * 10  # to plot

    # set market price V2
    def setMarketPriceV2(self):
        common.price = common.totalPlannedConsumptionInValueInA_TimeStep / \
            common.totalProductionInA_TimeStep
        print("Set market price to ", common.price)


    # set market price V3
    def setMarketPriceV3(self):
        shock0 = random.uniform(-common.maxDemandRelativeRandomShock,
                                common.maxDemandRelativeRandomShock)
        shock = shock0

        print("\n-------------------------------------")

        if shock >= 0:
            totalDemand = \
                common.totalPlannedConsumptionInValueInA_TimeStep * \
                (1 + shock)
            common.price = (common.totalPlannedConsumptionInValueInA_TimeStep *
                            (1 + shock))  \
                / common.totalProductionInA_TimeStep
            print("Relative shock (symmetric) ", shock0)
            print("Set market price to ", common.price)
            # common.totalDemandInPrevious_TimeStep is necessary for
            # adaptProductionPlan and adaptProductionPlanV6
            common.totalDemandInPrevious_TimeStep=totalDemand

        if shock < 0:
            shock *= -1.  # always positive, boing added to the denominator
            totalDemand = \
                common.totalPlannedConsumptionInValueInA_TimeStep / \
                (1 + shock)
            common.price = (common.totalPlannedConsumptionInValueInA_TimeStep /
                            (1 + shock))  \
                / common.totalProductionInA_TimeStep
            print("Relative shock (symmetric) ", shock0)
            print("Set market price to ", common.price)
            # common.totalDemandInPrevious_TimeStep is necessary for
            # adaptProductionPlan and adaptProductionPlanV6
            common.totalDemandInPrevious_TimeStep=totalDemand

        print("-------------------------------------\n")


    # set market price V6
    def setMarketPriceV6(self):

        print("\n-------------------------------------")

        if common.cycle < common.startHayekianMarket:

           shock0 = random.uniform(-common.maxDemandRelativeRandomShock,
                                   common.maxDemandRelativeRandomShock)
           shock = shock0

           if shock >= 0:
               totalDemand = \
                   common.totalPlannedConsumptionInValueInA_TimeStep * \
                   (1 + shock)
               common.price=(common.totalPlannedConsumptionInValueInA_TimeStep\
                               *(1 + shock))  \
                               / common.totalProductionInA_TimeStep
               print("Relative shock (symmetric) ", shock0)
               print("Set market price to ", common.price)
               # common.totalDemandInPrevious_TimeStep is necessary for
               # adaptProductionPlan and adaptProductionPlanV6
               common.totalDemandInPrevious_TimeStep=totalDemand

           if shock < 0:
               shock *= -1.  # always positive, boing added to the denominator
               totalDemand = \
                   common.totalPlannedConsumptionInValueInA_TimeStep / \
                   (1 + shock)
               common.price=(common.totalPlannedConsumptionInValueInA_TimeStep \
                               /(1 + shock))  \
                               / common.totalProductionInA_TimeStep
               print("Relative shock (symmetric) ", shock0)
               print("Set market price to ", common.price)
               # common.totalDemandInPrevious_TimeStep is necessary for
               # adaptProductionPlan and adaptProductionPlanV6
               common.totalDemandInPrevious_TimeStep=totalDemand

        # hayekian phase
        else:
            (common.price, common.hPriceSd)=checkHayekianPrices(\
                   common.hayekianMarketTransactionPriceList_inACycle)

            print("Hayekian phase (NA as not available values)")
            if common.price != -100:    print("Mean price ",common.price)
            else:                       print("Mean price NA")
            if common.hPriceSd != -100: print("Mean price s.d.",common.hPriceSd)
            else:                       print("Mean price s.d. NA")

        print("-------------------------------------\n")



    # random shock to wages (temporary method to experiment with wages)
    def randomShockToWages(self):
        k = 0.10
        shock = random.uniform(-k, k)

        if shock >= 0:
            common.wage *= (1. + shock)

        if shock < 0:
            shock *= -1.
            common.wage /= (1. + shock)

    # shock to wages (full employment case)
    def fullEmploymentEffectOnWages(self):

        # wages: reset incumbent action if any
        if common.wageAddendum > 0:
            common.wage -= common.wageAddendum
            common.wageAddendum = 0

        # employed people
        peopleList = common.g.nodes()
        totalPeople = len(peopleList)
        totalEmployed = 0
        for p in peopleList:
            if p.employed:
                totalEmployed += 1
        # print totalPeople, totalEmployed
        unemploymentRate = 1. - float(totalEmployed) / \
            float(totalPeople)
        if not common.fullEmploymentStatus and \
           unemploymentRate <= common.fullEmploymentThreshold:
            common.wage *= (1 + common.wageStepInFullEmployment)
            common.fullEmploymentStatus = True

        if common.fullEmploymentStatus and \
           unemploymentRate > common.fullEmploymentThreshold:
            common.wage /= (1 + common.wageStepInFullEmployment)
            common.fullEmploymentStatus = False

    # incumbents rising wages as an entry barrier
    def incumbentActionOnWages(self):

        # current number of entrepreneurs
        peopleList = common.g.nodes()
        nEntrepreneurs = 0
        for p in peopleList:
            if p.agType == "entrepreneurs":
                nEntrepreneurs += 1
        nEntrepreneurs = float(nEntrepreneurs)

        # no cumulative measure
        # as in the Section incumbentActionOnWages, as in WorldState, with details
        # in the Reference
        if not common.cumulativelyMeasuringNewEntrantNumber:
          # previous number of entrepreneurs
          # values in str_df at the beginning of each cycle (B as beginning)
          nEntrepreneursB = common.str_df.iloc[-1, 0]  # indexing Python style

          # print nEntrepreneurs, nEntrepreneurs0

          # wages: reset incumbent action if any
          if common.wageAddendum > 0:
              common.wage -= common.wageAddendum
              common.wageAddendum = 0

          # wages: set
          if nEntrepreneursB >= 1:
              if nEntrepreneurs / nEntrepreneursB - 1 > \
                 common.maxAcceptableOligopolistRelativeIncrement:
                common.wageAddendum = common.wage *\
                 common.temporaryRelativeWageIncrementAsBarrier
                common.wage += common.wageAddendum

        # cumulative measure
        # as in the Section incumbentActionOnWages, as in WorldState, with details
        # in the Reference
        if common.cumulativelyMeasuringNewEntrantNumber:
          print("///////// ","common.cycle",common.cycle)
          if common.cycle == 1:
                # values in str_df at the beginning of each cycle
                nEntrepreneursB_1     = common.str_df.iloc[-1, 0]#indexing Py. style
                nEntrepreneursB       = common.str_df.iloc[-1, 0]
                ReferenceLevel_1      = common.str_df.iloc[-1, 0]
                common.ReferenceLevel = common.str_df.iloc[-1, 0]
                                      # common to avoid a reference error
          else:
                nEntrepreneursB_1 = common.str_df.iloc[-2, 0]#indexing Py. style
                nEntrepreneursB   = common.str_df.iloc[-1, 0]
                ReferenceLevel_1  = common.ReferenceLevel

          #if nEntrepreneursB - nEntrepreneursB_1 <= 0 or \
          if  nEntrepreneursB_1 / ReferenceLevel_1 > \
                   common.maxAcceptableOligopolistRelativeIncrement:
                      common.ReferenceLevel = nEntrepreneursB
          else:
                      common.ReferenceLevel = ReferenceLevel_1

          # wages: reset incumbent action if any
          if common.wageAddendum > 0:
              common.wage -= common.wageAddendum
              common.wageAddendum = 0

          # wages: set
          if common.ReferenceLevel >= 1:
              if nEntrepreneurs / common.ReferenceLevel - 1 > \
                 common.maxAcceptableOligopolistRelativeIncrement:
                common.wageAddendum = common.wage *\
                 common.temporaryRelativeWageIncrementAsBarrier
                common.wage += common.wageAddendum

          print("/// ","nEntrepreneurs",nEntrepreneurs)
          print("/// ","nEntrepreneursB",nEntrepreneursB)
          print("/// ","nEntrepreneursB_1",nEntrepreneursB_1)
          print("/// ","ReferenceLevel",common.ReferenceLevel)
          print("/// ","ReferenceLevel_1",ReferenceLevel_1)
          print("/// ","wageAddendum",common.wageAddendum)
