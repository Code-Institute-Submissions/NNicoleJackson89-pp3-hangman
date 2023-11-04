# Import section
import random

# Prints the logo & Welcome message
print(r"""
  _    _          _   _  _____ __  __          _   _ 
 | |  | |   /\   | \ | |/ ____|  \/  |   /\   | \ | |
 | |__| |  /  \  |  \| | |  __| \  / |  /  \  |  \| |
 |  __  | / /\ \ | . ` | | |_ | |\/| | / /\ \ | . ` |
 | |  | |/ ____ \| |\  | |__| | |  | |/ ____ \| |\  |
 |_|  |_/_/    \_\_| \_|\_____|_|  |_/_/    \_\_| \_|
""")

welcome_str = """Welcome to the word guessing game where its all about
animals and staying ALIVE..."""
print(welcome_str)


def display_rules():
    """
    This fuction will display the rules if the user inputs y and skips this
    section if n is inputted
    """
    question = input("Would you like to see the rules? y = yes, n = no. \n")
    if question.lower() == "y":
        print("**************************************************************")
        print("Hangman is a simple word game, quessing one letter at a time,")
        print("Guess animal names with difficulty of easy, medium or hard,")
        print("If 6 incorrect letters are guessed, you will be hung and lose,")
        print("To win you will need to complete the word before being hung.")
        print("**************************************************************")
    elif question.lower() == "n":
        print("Request user name function to be placed here")
    else:
        print("Please enter 'y' for yes or 'n' for no.")
display_rules()