# importing the required module 
import matplotlib.pyplot as plt 
import numpy as np
import random as rnd
import stable as stable
import bolus as bolus

running = True

# Main Program
print("\nWelcome to Better Bolus!\n")

# x axis values 
# x = [0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 1.00, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30, 1.35, 1.40, 1.45, 1.50, 1.55, 2.00, 2.05, 2.10, 2.15, 2.20, 2.25, 2.30, 2.35, 2.40, 2.45, 2.50, 2.55, 3.00, 3.05, 3.10, 3.15, 3.20, 3.25, 3.30, 3.35, 3.40, 3.45, 3.50, 3.55, 4.00] 
x = [0.08163265, 0.1632653, 0.24489795, 0.3265306, 0.40816325, 0.48979589999999995, 0.5714285499999999, 0.6530611999999999, 0.7346938499999999, 0.8163264999999998, 0.8979591499999998, 0.9795917999999998, 1.0612244499999999, 1.1428570999999998, 1.2244897499999998, 1.3061223999999998, 1.3877550499999998, 1.4693876999999997, 1.5510203499999997, 1.6326529999999997, 1.7142856499999997, 1.7959182999999996, 1.8775509499999996, 1.9591835999999996, 2.0408162499999998, 2.1224488999999997, 2.2040815499999997, 2.2857141999999997, 2.3673468499999997, 2.4489794999999996, 2.5306121499999996, 2.6122447999999996, 2.6938774499999996, 2.7755100999999995, 2.8571427499999995, 2.9387753999999995, 3.0204080499999995, 3.1020406999999994, 3.1836733499999994, 3.2653059999999994, 3.3469386499999993, 3.4285712999999993, 3.5102039499999993, 3.5918365999999993, 3.6734692499999992, 3.755101899999999, 3.836734549999999, 3.918367199999999, 3.999999849999999]
# corresponding y axis values 
y = [] 

# bolus profile values as an object of arrays, each with two values, the first being the amount of insulin in units, and the second being the amount of time in minutes between now and when the bolus would be taken
bolusProfile = {}

# totalOnBoardInsulin = {}

# validatedBoolAnswer = []
# validatedTrendingInfo = []

def checkBGInput(bgInput):
    if bgInput < 120 or bgInput > 499:
        print("Invalid Input \nYou must enter an input equal to or between 120-499")
        print("Please enter a Blood Glucose value between 120-499")
        bgInput = int(input())
        return checkBGInput(bgInput)
    else: 
        y.append(bgInput)

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

while running == True:
    # naming the x axis 
    plt.xlabel('Time (hrs)') 
    # naming the y axis 
    plt.ylabel('BG (mg/dl)') 
    # setting y ranges
    plt.ylim(20, 600)
    y = [] 
    print("Please enter a Blood Glucose value between 120-499")
    bgInput = int(input())
    checkBGInput(bgInput)
    print(f"initial bg: {y[0]}mg/dl. Do you know how your current BG is trending? \nEnter 'y' for Yes or 'n' for No. If you aren't sure, enter 'n'.")
    boolAnswer = input()
    validatedBoolAnswer = checkBoolAnswer(boolAnswer)
    print(f"You answered {validatedBoolAnswer}")
    if validatedBoolAnswer[0] == "y":
        print("Please enter: \n'rising fast' for quickly rising BG \n'rising' for gently rising BG \n'stable' for stable BG \n'dropping' for dently dropping BG \n'dropping fast' for quickly dropping BG")
        trendingInfo = input()
        validatedTrendingInfo = checkTrendingInfo(trendingInfo)
        print(f"You answered {validatedTrendingInfo}")
        count = 48
        if validatedTrendingInfo == "stable":
            while count > 0:
                count -= 1
                stableVariance = rnd.randint(-5, 5)
                y.append(y[-1] + stableVariance)
            # giving a title to my graph 
            plt.title('Predicted Unadjusted Blood Glucose')
             # function to show the plot 
             # plotting the points  
            plt.plot(x, y) 
            plt.show() 
    if validatedBoolAnswer == "n":
        print("No trending info, proceeding")

    
    def addBolus():
        print("Would you like to add a Bolus? Type 'y' for Yes or 'n' for No")
        boolAnswer = input()
        validatedBoolAnswer = checkBoolAnswer(boolAnswer)
        print(f"You answered {validatedBoolAnswer}")
        if validatedBoolAnswer[-1] == "y":
            print("Please enter how many units of fast acting insulin to bolus")
            bolus = float(input())
            print("Please enter how many minutes from now (divisible by 5) the bolus will be applied")
            timeInput = float(input())
            # validatedTimeInput = checkTimeInput(timeInput)
            # print("time ver", checkTimeInput(timeInput))
            print(f"You added {bolus} units, to be applied in {timeInput} minutes")
            # print(timeInput)
            bolusProfile.update({timeInput: bolus})
            # print(bolusProfile)
            addBolus()
        if validatedBoolAnswer[-1] == "n":
            exit

    addBolus()
    bolusList = sorted(bolusProfile.items())

    insulinProfileList = sorted(bolus.insulinProfile.items())
    insulinEffect = []
    
  
    for i in range(len(insulinProfileList)):
        insulinEffect.append(insulinProfileList[i][1] * bolusList[0][1])

   

    def bolusStack():
        if len(bolusList) > 1:
            for i in range(len(bolusList) - 1):
                startTime = bolusList[i+1][0]
                # print('time', startTime)
                startIndex = list(bolus.insulinProfile.keys()).index(startTime)
                insulinEffectCopy = insulinEffect.copy()
                # print('slice', insulinEffect[startIndex:])
                del(insulinEffect[startIndex:])
                for subI in range(len(y[startIndex:])):
                    # print(insulinEffectCopy[startIndex:][subI], ' to ', insulinEffectCopy[startIndex:][subI] + insulinProfileList[subI][1] * bolusList[i+1][1])
                    insulinEffect.append(insulinEffectCopy[startIndex:][subI] + insulinProfileList[subI][1] * bolusList[i+1][1])
                    # print(subI)
    bolusStack()

    print(insulinEffect)

    insulinEffectResistanceAdjusted = []

    for i in range(len(y)):
        resistanceFactor = (1 - bolus.insulinResistanceAlgo(y[i]))
        insulinEffectResistanceAdjusted.append(int((insulinEffect[i] * resistanceFactor) * 4))

    yAdjusted = []
    
    for i in range(len(y)):
        if i == 0:
            yAdjusted.append(y[i] - insulinEffectResistanceAdjusted[i])
        else:
            yAdjusted.append(yAdjusted[i-1] - insulinEffectResistanceAdjusted[i])
    
    # print(yAdjusted)

    # naming the x axis 




    plt.xlabel('Time (hrs)') 
    # naming the y axis 
    plt.ylabel('BG (mg/dl)') 
    plt.ylim(20, 600)
    # plt.xticks(x, x)
    plt.title('Predicted Blood Glucose Adjusted For Bolus')
    # function to show the plot 
    # plotting the points  
    plt.plot(x, yAdjusted) 
    plt.show() 
    









    
    # function to show the plot 
    # plt.show() 

    # testing 
    # print(len(x))
    # print("initial bg:", y)

    