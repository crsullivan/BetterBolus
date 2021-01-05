# importing the required module 
import matplotlib.pyplot as plt 
import numpy as np
import random as rnd
import stable as stable

# Main Program
print("\nWelcome to Better Bolus!\n")

# x axis values 
x = [0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 1.00, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30, 1.35, 1.40, 1.45, 1.50, 1.55, 2.00, 2.05, 2.10, 2.15, 2.20, 2.25, 2.30, 2.35, 2.40, 2.45, 2.50, 2.55, 3.00, 3.05, 3.10, 3.15, 3.20, 3.25, 3.30, 3.35, 3.40, 3.45, 3.50, 3.55, 4.00] 
# corresponding y axis values 
y = [] 

# bolus profile values as an object of arrays, each with two values, the first being the amount of insulin in units, and the second being the amount of time in minutes between now and when the bolus would be taken
bolusProfile = {}

validatedTrendingAnswer = []
validatedTrendingInfo = []

def checkBGInput(bgInput):
    if bgInput < 120 or bgInput > 499:
        print("Invalid Input \nYou must enter an input equal to or between 120-499")
        print("Please enter a Blood Glucose value between 120-499")
        bgInput = int(input())
        checkBGInput(bgInput)
    else: 
        y.append(bgInput)

def checkTrendingAnswer(trendingAnswer):
    if trendingAnswer != 'y' and trendingAnswer != 'n':
        print("\nInvalid Input\n \nYou must enter either 'n' for No or 'y' for Yes. Do you know how your current BG is trending?")
        trendingAnswer = input()
        checkTrendingAnswer(trendingAnswer)
    else: 
        validatedTrendingAnswer.append(trendingAnswer)

def checkTrendingInfo(trendingInfo):
    if trendingInfo != 'rising fast' and trendingInfo != 'rising' and trendingInfo != 'stable' and trendingInfo != 'dropping' and trendingInfo != 'dropping fast':
        print("\nInvalid Input, please try again\n")
        print("Please enter: \n'rising fast' for quickly rising BG \n'rising' for gently rising BG \n'stable' for stable BG \n'dropping' for dently dropping BG \n'dropping fast' for quickly dropping BG")
        trendingInfo = input()
        checkTrendingInfo(trendingInfo)
    else: 
        validatedTrendingInfo.append(trendingInfo)

while True:

    print("Please enter a Blood Glucose value between 120-499")
    bgInput = int(input())
    checkBGInput(bgInput)
    print(f"initial bg: {y[0]}mg/dl. Do you know how your current BG is trending? \nEnter 'y' for Yes or 'n' for No. If you aren't sure, enter 'n'.")
    trendingAnswer = input()
    checkTrendingAnswer(trendingAnswer)
    print(f"You answered {validatedTrendingAnswer[0]}")
    if validatedTrendingAnswer[0] == "y":
        print("Please enter: \n'rising fast' for quickly rising BG \n'rising' for gently rising BG \n'stable' for stable BG \n'dropping' for dently dropping BG \n'dropping fast' for quickly dropping BG")
        trendingInfo = input()
        checkTrendingInfo(trendingInfo)
        print(f"You answered {validatedTrendingInfo[0]}")
        count = 48
        if validatedTrendingInfo[0] == "stable":
            print(y[-1])
            print(stable.stableY.stableVariance)
            while count > 0:
                count -= 1
                stableVariance = rnd.randint(-5, 5)
                y.append(y[-1] + stableVariance)
            print(y)
    if validatedTrendingAnswer[0] == "n":
        print("No trending info, proceeding")
    

    # setting y ranges
    plt.ylim(20, 600)

    # plotting the points  
    plt.plot(x, y) 
    
    # naming the x axis 
    plt.xlabel('Time') 
    # naming the y axis 
    plt.ylabel('BG mg/dl') 
    
    # giving a title to my graph 
    plt.title('Predicted Blood Glucose')
    
    # function to show the plot 
    plt.show() 

    # testing 
    # print(len(x))
    # print("initial bg:", y)

    