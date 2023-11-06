# Import section
import random
from words import words_list

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
animals and staying ALIVE... \n"""
print(welcome_str)


def display_rules():
    """
    This fuction will display the rules if the user inputs y and skips this
    section if n is inputted
    """
#     while True:
#         question = input("Would you like to see the rules, y/n?\n")
#         if question.lower() == "y":
#             print(
#                 "\n*******************************************************\n" +
#                 "This is a simple word game, quess one letter at a time.\n" +
#                 "Guess animal names with 3 difficulty levels:\n" +
#                 "Easy, medium or hard.\n" +
#                 "If 6 incorrect letters are guessed, you will be hung.\n" +
#                 "To win you need to complete the word before being hung.\n" +
#                 "*******************************************************"
#                 )
#             break
#         elif question.lower() == "n":
#             break
#         else:
#             print("Please enter 'y' for yes or 'n' for no. \n")



# def users_name():
#     """
#     This function will ask the user to enter their, an error will be 
#     raised where numbers, characters or spaces are entered
#     """
#     while True:
#         try:
#             name = input("\nPlease enter your name:\n")
#             if not name.isalpha():
#                 raise ValueError("Your name can only contain letters.\n")
#             else:
#                 print(f"\nReady to play {name.capitalize()}...\n")
#                 break
#         except ValueError as err:
#             print(err)


# def random_word(words_list):
#     """
#     This function returns a random word of various difficulty from the words list
#     """
#     word = random.choice(words_list)
#     return word.upper()


 


# display_rules()
# users_name()











# def difficulty_level():
#     """
#     This function allows the user to select between three levels of
#     difficulty, easy, medium or hard
#     """
#     while True:
#         try:
#             level = input("Would you like to play easy, medium or hard?\n").lower()
#             if level == "easy":
#                 print(words.easy_list)
#             elif level == "medium":
#                 print(words.medium_list)
#             elif level == "hard":
#                 print(words.hard_list)
#             else level not in ["easy", "medium". "hard"]:
#                 raise ValueError("You need to choose easy, medium or hard")
#         except ValueError as err:
#             print(err)

# difficulty_level()





