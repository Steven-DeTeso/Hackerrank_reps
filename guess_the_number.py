import random

logo = """
  _   _                 _                      ____                     _                ____                      
 | \ | |_   _ _ __ ___ | |__   ___ _ __ ___   / ___|_   _  ___  ___ ___(_)_ __   __ _   / ___| __ _ _ __ ___   ___ 
 |  \| | | | | '_ ` _ \| '_ \ / _ \ '__/ __| | |  _| | | |/ _ \/ __/ __| | '_ \ / _` | | |  _ / _` | '_ ` _ \ / _ \
 | |\  | |_| | | | | | | |_) |  __/ |  \__ \ | |_| | |_| |  __/\__ \__ \ | | | | (_| | | |_| | (_| | | | | | |  __/
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|  |___/  \____|\__,_|\___||___/___/_|_| |_|\__, |  \____|\__,_|_| |_| |_|\___|
                                                                                |___/                              
"""


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0

def check_answer(guess, answer, turns):
    """Checks answer against guess, returns number of turns remaining."""
    if guess > answer:
        print("Too High!")
        return turns - 1
    elif guess < answer:
        print("Too Low!")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")

def set_difficulty():
    difficulty = input("Choose a difficulty. Enter 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number betwwen 1 and 100.")
    number = random.randint(1, 100)
    print(f"Psst, the correct answer is {number}")

    turns = set_difficulty()
    guess = 0
    while guess != number:
        print(f"You have {turns} remaining attempts to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, number, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != number:
            print("Guess again.")
            

game()