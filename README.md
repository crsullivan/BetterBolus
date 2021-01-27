# BetterBolus V2.0
A tool to better understand how to safely and efficiently treat high blood sugar, and to model the effects of fast acting insulin.

## THIS PROGRAM IS CURRENTLY FOR MODELING PURPOSES ONLY AND SHOULD NOT BE USED TO DETERMINE HOW TO MANAGE AN INDIVIDUAL'S BLOOD GLUCOSE

### Version 2.1
Version 2.1 is on track for release by EOD January 29, 2021. This update will improve the UI, as well as fine tune the insulin resistance algorithm, particularly at the upper range.

### Running the Program
Step 1: Ensure all necessary dependencies are installed with the exception of pyinstaller.
Step 2: cd into project directory.
Step 3: type "python BetterBolus.py" or "python3 BetterBolus.py" depending on your OS
Step 4: Hit Enter and the user interface will load up.

### Dependencies

matplotlib - Latest version is best.

sortedcontainers - Latest version is best

pyinstaller - Latest version is best, only necessary to convert to the executable

### Potential Issues
Currently this program assumes that when the user wants to bolus, they want the first bolus immediately in an attempt to stabilize dangerous blood glucose levels as quickly as possible. Therefore, the first bolus entered is automatically applied at 0.00 (immediately). This may change in future updates.

Due to Blood Glucose being affected by hundreds more variables than one can realistically ask a user to account for (like exact altitude, an objective measurement of their stress levels, the exact level of caffeine currently in their bloodtstream, etc) liberties are taken by the program in predicting a realistic potential outcome based off what the user can reliably provide. A pseudo-random number generator is used to establish a certain controlled level of variance and unpredictability in blood these glucose models.

#### About PyInstaller
If desired, the program can be compiled into an executable with pyinstaller, while this is not necessary, it does provide an easy way to continuously access the application without having to cd into the project folder every time.
