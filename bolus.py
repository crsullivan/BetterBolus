class Bolus:
    def __init__(self, units, time):
        self.units = units
        self.time = time

def enterBolus():
    print("Would you like to enter a bolus? Type 'y' for Yes, 'n' for No.")