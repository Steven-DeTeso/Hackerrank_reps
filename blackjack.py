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

print(logo)
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  def cacluate_score(list_of_cards):
    """Take a list of cards and return a score calculated from the cards"""
    score = sum(list_of_cards)
    if len(list_of_cards) == 2 and score == 21:
      print("Blackjack!")
      return 0 
    if 11 in list_of_cards and score > 21:
      list_of_cards.remove(11)
      list_of_cards.append(1)
    return score
  
  for card in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not is_game_over:
    user_score = cacluate_score(user_cards)
    computer_score = cacluate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computers first card: {computer_cards[0]}")
    
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      deal_another = input("Type 'y' to get another card, type 'n' to pass: ").lower()
      if deal_another == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True
        
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = cacluate_score(computer_cards)
    
  
  
  print("\n\n")
  print(f"Your final hand is: {user_cards}, final score: {user_score}")
  print(f"Dealer final hand is: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))