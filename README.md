# Overview
The Password Generator is a Python script that generates random passwords based on user-defined difficulty levels and length. The script allows users to select from different difficulty levels and generates passwords accordingly. The available levels range from simple lowercase letters to more complex combinations of letters and numbers.

# Features
* Easy: Generates a password using only lowercase letters.
* Hard: Generates a password using both uppercase and lowercase letters.
* Hackproof: Generates a password using uppercase and lowercase letters along with digits.

# Code Explanation
## Importing Modules
* ascii_lowercase: Contains all lowercase letters.
* ascii_letters: Contains both lowercase and uppercase letters.
* digits: Contains all numeric digits.
* punctuation: Contains all punctuation characters.
* choice: Used to randomly select characters.
## Functions
* lower_alpha_gen(n): Generates a random string of lowercase letters with length n.

* alpha_gen(n): Generates a random string of both uppercase and lowercase letters with length n.

* alpha_num_gen(n): Generates a random string of uppercase and lowercase letters along with digits with length n.

## Main Code
* The main() function contains the main loop for the script:

* Prompts the user to select a difficulty level.
* Prompts the user to enter the desired length of the password.
* Validates inputs and generates passwords based on the selected level.
* Asks the user if they want to generate another password or exit.<br>

The script ensures user inputs are valid and provides appropriate feedback for incorrect inputs.
