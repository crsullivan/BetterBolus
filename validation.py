def checkBGInput(bgInput):
    if bgInput < 120 or bgInput > 499:
        print("Invalid Input \nYou must enter an input equal to or between 120-499")
        print("Please enter a Blood Glucose value between 120-499")
        bgInput = int(input())
        return checkBGInput(bgInput)
    else: 
        return bgInput

def checkBoolAnswer(boolAnswer):
    if boolAnswer != 'y' and boolAnswer != 'n':
        print("\nInvalid Input\n \nYou must enter either 'n' for No or 'y' for Yes")
        boolAnswer = input()
        return checkBoolAnswer(boolAnswer)
    else: 
        return boolAnswer

def checkTrendingInfo(trendingInfo):
    if trendingInfo != 'rising fast' and trendingInfo != 'rising' and trendingInfo != 'stable' and trendingInfo != 'dropping' and trendingInfo != 'dropping fast':
        print("\nInvalid Input, please try again\n")
        print("Please enter: \n'rising fast' for quickly rising BG \n'rising' for gently rising BG \n'stable' for stable BG \n'dropping' for dently dropping BG \n'dropping fast' for quickly dropping BG")
        trendingInfo = input()
        return checkTrendingInfo(trendingInfo)
    else: 
        return trendingInfo

def checkTimeInput(timeInput):
    if timeInput % 5 != 0:
        print("Invalid input, enter a time divisible by 5. For example: '15' for fifteen minutes")
        timeInput = int(input())
        return checkTimeInput(timeInput)
    else:
        print("time input", timeInput)
        return timeInput

def checkBolus(bolus):
    try:
        bolus = float(bolus)
        if bolus <= 0:
            print("Please enter a valid number of units to bolus")
            bolus = input()
            return checkBolus(bolus)
        else:
            return bolus
    except ValueError:
        print("Please enter a valid number of units to bolus")
        bolus = input()
        return checkBolus(bolus)


