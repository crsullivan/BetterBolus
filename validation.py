def checkBGInput(bgInput):
    try:
        bgInput = int(bgInput)
        if bgInput < 120 or bgInput > 499:
            print("Invalid Input \nYou must enter an input equal to or between 120-499")
            print("Please enter a Blood Glucose value between 120-499")
            bgInput = input()
            return checkBGInput(bgInput)
        else: 
            return bgInput
    except ValueError:
        if bgInput != 'e':
            print("Invalid input. please enter an integer between 120 and 499, or type 'e' to exit.")
            bgInput = input()
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
    if len(timeInput) != 4:
        print("Please ensure your input is in the following format and try again: (hours).(minutes)")
        timeInput = input()
        return checkTimeInput(timeInput)
    else:
        try:
            timeInput = float(timeInput)
            if (round(timeInput * 100)) % 5 != 0:
                print("Invalid input, enter a time divisible by 5.")
                timeInput = input()
                return checkTimeInput(timeInput)
            else:
                print("time input", timeInput)
                return timeInput
        except ValueError:
            print("Please enter a valid time using numbers and following this format: (hours):(minutes)")
            timeInput = input()
            return checkTimeInput(timeInput)

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


