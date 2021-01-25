import matplotlib.pyplot as plt 
import numpy as np
import random as rnd
import tkinter as tk
from tkinter import filedialog, Text
import stable as stable
import rising as rising
import dropping as dropping
import rising_fast as rising_fast
import dropping_fast as dropping_fast
import bolus as bolus

# x axis values 
x = [0.08163265, 0.1632653, 0.24489795, 0.3265306, 0.40816325, 0.48979589999999995, 0.5714285499999999, 0.6530611999999999, 0.7346938499999999, 0.8163264999999998, 0.8979591499999998, 0.9795917999999998, 1.0612244499999999, 1.1428570999999998, 1.2244897499999998, 1.3061223999999998, 1.3877550499999998, 1.4693876999999997, 1.5510203499999997, 1.6326529999999997, 1.7142856499999997, 1.7959182999999996, 1.8775509499999996, 1.9591835999999996, 2.0408162499999998, 2.1224488999999997, 2.2040815499999997, 2.2857141999999997, 2.3673468499999997, 2.4489794999999996, 2.5306121499999996, 2.6122447999999996, 2.6938774499999996, 2.7755100999999995, 2.8571427499999995, 2.9387753999999995, 3.0204080499999995, 3.1020406999999994, 3.1836733499999994, 3.2653059999999994, 3.3469386499999993, 3.4285712999999993, 3.5102039499999993, 3.5918365999999993, 3.6734692499999992, 3.755101899999999, 3.836734549999999, 3.918367199999999, 3.999999849999999]
# corresponding y axis values list, values to be added by the program, starting with initial BG
y = [] 

bgInput = ""
# insert current bg at start of y axis (current blood glucose)
def initial_bg(bg):
    y.append(bg)
# check if user has trernding info
def unadjusted_graph(trending):
    if trending == "Stable":
        # build the rest of the y axis for a stable profile
        yBuild = (stable.stableBuild())
        for i in range(len(yBuild)):
            y.append(y[i] + yBuild[i])
    if trending == "Rising":
        # build the rest of the y axis for a rising profile
        yBuild = (rising.risingBuild())
        for i in range(len(yBuild)):
            y.append(y[i] + yBuild[i])
    if trending == "Dropping":
        # build the rest of the y axis for a dropping profile
        yBuild = (dropping.droppingBuild())
        for i in range(len(yBuild)):
            y.append(y[i] + yBuild[i])
    if trending == "Rising Fast":
        # build the rest of the y axis for a rising_fast profile
        yBuild = (rising_fast.rising_fastBuild())
        for i in range(len(yBuild)):
            y.append(y[i] + yBuild[i])
    if trending == "Dropping Fast":
        # build the rest of the y axis for a dropping_fast profile
        yBuild = (dropping_fast.dropping_fastBuild())
        for i in range(len(yBuild)):
            y.append(y[i] + yBuild[i])
    if trending == "Unknown":
        trending = "none"
        # build the rest of the y axis for a stable profile
        yBuild = (stable.stableBuild())
        for i in range(len(yBuild)):
            y.append(y[i] + yBuild[i])

def show_unadjusted_graph():
    # naming the x axis 
    plt.xlabel('Time (hrs)') 
    # naming the y axis 
    plt.ylabel('BG (mg/dl)') 
    # setting y ranges
    plt.ylim(20, 600)
    # giving a title to my graph 
    plt.title('Predicted Unadjusted Blood Glucose') 
    # plotting the points  
    plt.plot(x, y) 
    # function to show the plot
    plt.show() 

insulinProfileList = sorted(bolus.insulinProfile.items())

def applyInitialBolus(bolusProfile):
    insulinEffect = []
    bolusList = sorted(bolusProfile.items())
    for i in range(len(insulinProfileList)):
        insulinEffect.append(insulinProfileList[i][1] * bolusList[0][1])
    return insulinEffect

def bolusStack(insulinEffect, bolusProfile):
    bolusList = sorted(bolusProfile.items())
    for i in range(len(bolusList) - 1):
        startTime = float(bolusList[i+1][0])
        startIndex = list(bolus.insulinProfile.keys()).index(startTime)
        insulinEffectCopy = insulinEffect.copy()
        del(insulinEffect[startIndex:])
        for subI in range(len(y[startIndex:])):
            insulinEffect.append(insulinEffectCopy[startIndex:][subI] + insulinProfileList[subI][1] * bolusList[i+1][1])
    return insulinEffect
# # bolusStack()
insulinEffectResistanceAdjusted = []
def build_resistance_profile(trending, insulinEffect):
    if trending == "Rising":
        # build the rest of the y axis for a rising profile
        for i in range(len(y)):
            resistanceFactor = (1 - rising.insulinResistanceAlgo(y[i]))
            insulinEffectResistanceAdjusted.append(((insulinEffect[i] * resistanceFactor) * 4))
    if trending == "Dropping":
        # build the rest of the y axis for a dropping profile
        for i in range(len(y)):
            resistanceFactor = (1 - dropping.insulinResistanceAlgo(y[i]))
            insulinEffectResistanceAdjusted.append(((insulinEffect[i] * resistanceFactor) * 4))
    if trending == "Rising Fast":
        # build the rest of the y axis for a rising_fast profile
        for i in range(len(y)):
            resistanceFactor = (1 - rising_fast.insulinResistanceAlgo(y[i]))
            insulinEffectResistanceAdjusted.append(((insulinEffect[i] * resistanceFactor) * 4))
    if trending == "Dropping Fast":
        # build the rest of the y axis for a dropping_fast profile
        for i in range(len(y)):
            resistanceFactor = (1 - dropping_fast.insulinResistanceAlgo(y[i]))
            insulinEffectResistanceAdjusted.append(((insulinEffect[i] * resistanceFactor) * 4))
    if trending == "Unknown" or trending == "Stable":
        for i in range(len(y)):
            resistanceFactor = (1 - stable.insulinResistanceAlgo(y[i]))
            insulinEffectResistanceAdjusted.append((insulinEffect[i] * resistanceFactor) * 4)
    return insulinEffectResistanceAdjusted

def show_adjusted_graph(insulinEffectResistanceAdjusted):
    yAdjusted = []
    for i in range(len(y)):
        if i <= 2:
            yAdjusted.append(y[i])
        else:
            yAdjusted.append(yAdjusted[i-1] - insulinEffectResistanceAdjusted[i])
    # naming the x axis 
    plt.xlabel('Time (hrs)') 
    # naming the y axis 
    plt.ylabel('BG (mg/dl)') 
    # setting y ranges
    plt.ylim(20, 600)
    # giving a title to my graph 
    plt.title('Predicted Adjusted Blood Glucose') 
    # plotting the points  
    plt.plot(x, yAdjusted) 
    # function to show the plot
    plt.show() 


        


        