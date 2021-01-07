import random as rnd

def stableBuild():
    y = []
    count = 48
    while count > 0:
        count -= 1
        stableVariance = rnd.randint(-5, 5)
        y.append(stableVariance)
    return y 

def insulinResistanceAlgo(bg):
    resistanceLevel = 0
    if bg - 200 > 0:
        resistanceLevel = (bg - 200) / 300
        return resistanceLevel
    else:
        return resistanceLevel

