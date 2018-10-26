import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up,
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # TO DO
    currentPop = CURRENTRABBITPOP
    if currentPop < 10:
        return

    birthProb = 1.0 - (currentPop/float(MAXRABBITPOP))
    newRabbits = 0
    for r in range(currentPop):
        chance = random.random()
        if chance < birthProb:
            newRabbits += 1
    endPop = currentPop + newRabbits
    CURRENTRABBITPOP = min(MAXRABBITPOP, endPop)

def foxGrowth():
    """
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO
    currentPop = CURRENTFOXPOP
    if currentPop < 10:
        return

    killCount = 0
    for f in range(currentPop):
        killProb = (CURRENTRABBITPOP/float(MAXRABBITPOP))
        eatChance = random.random()
        if eatChance < killProb and CURRENTRABBITPOP > 10:
            killCount += 1
            CURRENTRABBITPOP -= 1
    newFoxes = 0
    for i in range(killCount):
        birthProb = 1/float(3)
        birthChance = random.random()
        if birthChance < birthProb:
            newFoxes += 1
    dead = 0
    for j in range(currentPop - killCount):
        deathProb = 1/float(10)
        deathChance = random.random()
        if deathChance < deathProb:
            dead += 1
    afterBirths = min(CURRENTRABBITPOP, CURRENTFOXPOP+newFoxes)
    afterDeaths = max(10, afterBirths-dead)
    CURRENTFOXPOP = afterDeaths


def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    # TO DO
    rabbitPops = []
    foxPops = []
    for s in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbitPops.append(CURRENTRABBITPOP)
        foxPops.append(CURRENTFOXPOP)
    return (rabbitPops, foxPops)

runSimulation(10)


