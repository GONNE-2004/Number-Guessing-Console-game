import random
from art import logo

#print a number at random


# initialize 2 difficulty level
EASY_LEVELS_TURNS = 10
HARD_LEVELS_TURNS = 5

#ask the user to choose difficulty level
def difficulty():
    """contains the choice btn difficulty levels"""
    while True:
        level = input("Type 'easy' or 'hard' to set difficulty  ").lower().strip()
        if level == "easy":
            return EASY_LEVELS_TURNS
        elif level == "hard":
            return HARD_LEVELS_TURNS
        else:
            print("Invalid choice, please choose: easy or hard!")


def compare_answer(user_guess, answer_guess, turns):
    """contains comparing logic"""
    if user_guess > answer_guess:
        print("Too high, try again!")
        return turns - 1 # reduces 1 if the guess is greater than number
    elif user_guess < answer_guess:
        print("Too low, try again!")
        return turns - 1 # reduces 1 if guess is lower than number
    else:
        print(f"You got it:{answer_guess}")
        return "congrats!"


def get_guess(prompt : str):
    "Ensures the user enters the correct data type again and again"
    while True:
        try:
            guess = int(input(prompt))

            if 1 <= guess <= 100: #enures the input range is btn 1-100
                return guess
            else:
                print("Please enter a number between 1-100!")

        except ValueError:
            print("Input invalid, please enter a postive number.")


def game():
    """contains logic which helps the game repeat again and again"""
    again = True

    while again:
        print(logo)
        print("Welcome the Number Guessing Game!")
        print("Am thinking of a number between 1-100")
        number = random.randint(1, 101)
        print(number)

        turns = difficulty() #initialised ii to it in order to choose btn easy and hard chances

        guess = 0
        while guess != number:
            print(f"You have:{turns} chances to guess the number!")

            guess = get_guess("Guess a number:  ")

            turns = compare_answer(guess, number, turns) #initialised here but this time to compare in order to help with reducing the chances & comparing btn the 2 number
            if turns == 0:
                print("You have ran of out chances, you lose!")
                print(f"The number was: {number}")
                return
            elif guess != number:
                print("Guest again!")

        play_again = input("Type 'yes' to restart the game or 'no' to stop: \n").lower().strip()
        if play_again == "no":
            again = False
            print("Thanks for play, goodbye")
        elif play_again == "yes":
            print("\n" * 20)
        else:
            ("Please enter 'yes or no'")





game()