import random as rnd

def dropping_fastBuild():
    y = []
    count = 48
    while count > 35:
        count -= 1
        stableVariance = rnd.randint(-10, -5)
        y.append(stableVariance)
    while count > 25 and count <= 35:
        count -= 1
        stableVariance = rnd.randint(-5, -1)
        y.append(stableVariance)
    while count > 0 and count <= 25:
        count -= 1
        stableVariance = rnd.randint(-5, 5)
        y.append(stableVariance)
    return y 