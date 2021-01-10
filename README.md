# BetterBolus V1.0
A tool to better understand how to safely and efficiently treat high blood sugar, and to model the effects of fast acting insulin.

## THIS PROGRAM IS CURRENTLY FOR MODELING PURPOSES ONLY AND SHOULD NOT BE USED TO DETERMINE HOW TO MANAGE AN INDIVIDUAL'S BLOOD GLUCOSE

### Running the Program
Step 1: Ensure all necessary dependencies are installed
Step 2: cd into project directory
Step 3: type "python main.py" or "python3 main.py" depending on your OS
Step 4: Hit Enter and follow the console prompts, once a graph is generated, simply closing the graph will prompt you to the next stage of the program.

### Dependencies
numpy version 1.19.3 - I would not recommend trying to use the latest version of numpy due to a bug with Windows. Microsoft expects this issue to be resolved within Q1 of 2021.

matplotlib - Latest version is best.

random - Latest version is best.

### Potential Issues
Currently this program assumes that when the user wants to bolus, they want the first bolus immediately in an attempt to stabilize dangerous blood glucose levels as quickly as possible. Therefore, the first bolus entered is automatically applied at 0.00 (immediately). This may change in future updates.

Due to Blood Glucose being affected by hundreds more variables than one can realistically ask a user to account for (like exact altitude, an objective measurement of their stress levels, the exact level of caffeine currently in their bloodtstream, etc) liberties are taken by the program in predicting a realistic potential outcome based off what the user can reliably provide. A pseudo-random number generator is used to establish a certain controlled level of variance and unpredictability in blood these glucose models.

## Version 2 
I am planning on refactoring into a standalone executable that should be able to run on any desktop environment. This will improve accessibility and user friendliness. V2 expected by EOD January 15th, 2021.
