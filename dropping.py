import random as rnd

def droppingBuild():
    y = []
    count = 48
    while count > 30:
        count -= 1
        stableVariance = rnd.randint(-5, -1)
        y.append(stableVariance)
    while count > 0 and count <= 30:
        count -= 1
        stableVariance = rnd.randint(-5, 5)
        y.append(stableVariance)
    return y 

def insulinResistanceAlgo(bg):
    resistanceLevel = 0
    count = 48
    while count > 30:
        count -= 1
        if bg - 200 > 0:
            resistanceLevel = -((bg - 200) / 400)
            return resistanceLevel
        else:
            resistanceLevel = -.25
            return resistanceLevel
    while count > 0 and count <= 30:
        count -= 1
        if bg - 200 > 0:
            resistanceLevel = (bg - 200) / 300
            return resistanceLevel
        else:
            return resistanceLevel