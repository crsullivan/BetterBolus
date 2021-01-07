import random as rnd

def stableBuild():
    y = []
    count = 48
    while count > 0:
        count -= 1
        stableVariance = rnd.randint(-5, 5)
        y.append(stableVariance)
    return y 