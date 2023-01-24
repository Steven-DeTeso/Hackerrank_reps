# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# concatenate strings together into one string
combined_string = name1 + name2

# convert combined string to lower case 
lower_case_string = combined_string.lower()

# count each letter of the string and add to variables
t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')

true = t + r + u + e 

l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')

love = l + o + v + e 

# combine totals for each name into a 2 digit number 
love_score = str(true) + str(love)

# if check if score is less than 10 or greater than 90. specific message
if int(love_score) < 10 or int(love_score) > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")

# if check if score is between 40 and 50 
elif int(love_score) < 50 and int(love_score) > 40:
    print(f"Your score is {love_score}, you are alright together.")

# else final message for all other caes. 
else:
    print(f"Your score is {love_score}.")