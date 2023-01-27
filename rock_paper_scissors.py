import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
shoot = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer = random.randint(0,2)

if shoot == 0:
  print(rock)
if shoot == 1:
  print(paper)
if shoot == 2:
  print(scissors)

print("Computer choose:")

if computer == 0:
  print(rock)
if computer == 1:
  print(paper)
if computer == 2:
  print(scissors)

if shoot == computer:
  print("It's a draw!")
elif shoot == 0 and computer == 2:
  print("Rock beats scissors: You Win!")
elif shoot == 0 and computer == 1:
  print("Rock doesn't beat paper: You Lose!")
elif shoot == 1 and computer == 0:
  print("Paper beats rock: You Win!")
elif shoot == 1 and computer == 2:
  print("Paper doesn't beat scissors: You Lose!")
elif shoot == 2 and computer == 0:
  print("Scissors doesn't beat Rock: You Lose!")
elif shoot == 2 and computer == 1:
  print("Scissors beats paper: You win! ")