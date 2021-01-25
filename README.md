# BetterBolus
A tool to better understand how to safely and efficiently treat high blood sugar, and to model the effects of fast acting insulin.

## THIS PROGRAM IS CURRENTLY FOR MODELING PURPOSES ONLY AND SHOULD NOT BE USED TO DETERMINE HOW TO MANAGE AN INDIVIDUAL'S BLOOD GLUCOSE

### Dependencies

matplotlib - Latest version is best.

sortedcontainers - Latest version is best

### Potential Issues
Currently this program assumes that when the user wants to bolus, they want the first bolus immediately in an attempt to stabilize dangerous blood glucose levels as quickly as possible. Therefore, the first bolus entered is automatically applied at 0.00 (immediately). This may change in future updates.

Due to Blood Glucose being affected by hundreds more variables than one can realistically ask a user to account for (like exact altitude, an objective measurement of their stress levels, the exact level of caffeine currently in their bloodtstream, etc) liberties are taken by the program in predicting a realistic potential outcome based off what the user can reliably provide. A pseudo-random number generator is used to establish a certain controlled level of variance and unpredictability in blood these glucose models.
