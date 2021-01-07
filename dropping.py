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