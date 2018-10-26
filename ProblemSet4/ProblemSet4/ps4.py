# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *


def runSim(numViruses, maxPop, maxBirthProb, clearProb, resistances, delay,
                       mutProb, numTrials):
    totalPopSizes = 0
    resistantPopSizes = []
    for t in range(numTrials):
        viruses = []
        for v in range(numViruses):
            viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
        p = TreatedPatient(viruses, maxPop)
        for s1 in range(150):
            p.update()
        p.addPrescription('guttagonol')
        for s2 in range(delay):
            p.update()
        p.addPrescription('grimpex')
        for s3 in range(150):
            p.update()
        totalPopSize = p.getTotalPop()
    return totalPopSize
#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """

    finalPops = []
    for t in range(numTrials):
        currentTrial = runSim(100, 1000, .1, .05, {'guttagonol': False, 'grimpex': False}, 300, .005, 1)
        finalPops.append(currentTrial)
    pylab.hist(finalPops, bins=25)
    pylab.show()
    






#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    finalPops = []
    for t in range(numTrials):
        currentTrial = runSim(100, 1000, .1, .05, {'guttagonol': False, 'grimpex': False}, 0, .005, 1)
        finalPops.append(currentTrial)
    pylab.hist(finalPops, bins=25)
    pylab.show()
