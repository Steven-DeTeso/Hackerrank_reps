import random

logo = """
  _   _                 _                      ____                     _                ____                      
 | \ | |_   _ _ __ ___ | |__   ___ _ __ ___   / ___|_   _  ___  ___ ___(_)_ __   __ _   / ___| __ _ _ __ ___   ___ 
 |  \| | | | | '_ ` _ \| '_ \ / _ \ '__/ __| | |  _| | | |/ _ \/ __/ __| | '_ \ / _` | | |  _ / _` | '_ ` _ \ / _ \
 | |\  | |_| | | | | | | |_) |  __/ |  \__ \ | |_| | |_| |  __/\__ \__ \ | | | | (_| | | |_| | (_| | | | | | |  __/
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|  |___/  \____|\__,_|\___||___/___/_|_| |_|\__, |  \____|\__,_|_| |_| |_|\___|
                                                                                |___/                              
"""

number = random.randint(1, 100)
attempts = 0

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number betwwen 1 and 100.")
print(f"Psst, the correct answer is {number}")
difficulty = input("Choose a difficulty. Enter 'easy' or 'hard': ").lower()

if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5

is_game_over = False

while not is_game_over:
    print(f"You have {attempts} remaining attempts to guess the number.")
    if attempts > 0:
        guess = int(input("Make a guess: "))
        if number > guess:
            attempts -= 1
            print("Too low")
            print("Guess again.")
        elif number < guess:
            attempts -= 1
            print("Too high")
            print("Guess again.")
        elif number == guess:
            print("You guessed it! You win!")
            is_game_over = True
    elif attempts == 0:
        print("Game Over. You Lose")
        is_game_over = True