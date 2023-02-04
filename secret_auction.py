from os import system
def clear():
    system('clear')

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the secret auction! Best of luck!")

auction = {}

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    #Looping through the dict below 
    # bidder is key in dictionary 
    for bidder in bidding_record:
    # gives value from key being passed into dict below
        bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder 
    print(f"The winner is {winner} with the highest bid of ${highest_bid}")

still_bidding = True
while still_bidding:
    name = input("What is your name?\n")
    bid_amount = int(input("How much do you want to bid? $"))
    # adding to the dictionary below: 
    auction[name] = bid_amount
    more_bids = input("Are their any other users who want to bid? type 'yes' or 'no'.\n").lower()
    if more_bids == 'no':
        still_bidding = False
    else:
        clear()

find_highest_bidder(auction)