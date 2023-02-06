import random
from os import system


logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

"""Functions to make the game run properly"""
def clear():
    system('clear')

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def compare(user_score, computer_score):
  """Compares user and computer score and returns outcome to terminal."""
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "Blackjack for dealer! You Lose :("
  elif user_score == 0: 
    return "Blackjack for you! You win!"
  elif user_score > 21:
    return "You went over. You lose :("
  elif computer_score > 21:
    return "Dealer went over, You Win!"
  elif user_score > computer_score:
    return "You Win!"
  else: 
    return "You Lose :("