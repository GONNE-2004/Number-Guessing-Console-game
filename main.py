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


def compare_answer(user_guess : int, answer_guess : int):
    """Compares the guess and number then returns message accordlly"""
    if user_guess > answer_guess:
        return (False,"Too high, try again!")
    elif user_guess < answer_guess:
        return (False,"Too low. Try again")
    else:
        return (True,f"You got it:{answer_guess}")


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


def print_welcome():
        """Holds game intro and rule"""
        print(logo)
        print("Welcome the Number Guessing Game!")
        print("Am thinking of a number between 1-100")


def play_around():
        """holds one complete round of the game and turns"""
        print_welcome()
        number = random.randint(1, 101)
        turns = difficulty() #initialised ii to it in order to choose btn easy and hard chances
        print(number)
        while turns > 0:
            print(f"Turns left: {turns}")
            guess = get_guess("Guess a number (1-100): ")

            correct, message = compare_answer(guess, number)
            print(message) # i initiatied 2 variable in tuples the corrects returns the boolean and message returns str from the compare_answer function

            if correct:
                return True  # Player won
            turns -= 1

        print(f"Game over! The number was {number}.")
        return False  # Player lost



def game():
    """holds main loop which deal with restart and stop of the program"""
    again = True
    while again:
        play_around()
        play_again = input("Type 'yes' to restart the game or 'no' to stop: \n").lower().strip()
        if play_again == "no":
            again = False
            print("Thanks for play, goodbye")
        elif play_again == "yes":
            print("\n" * 20)
        else:
            ("Please enter 'yes or no'")
game()