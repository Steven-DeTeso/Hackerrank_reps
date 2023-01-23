# String split and join - In Python, a string can be split on a delimiter.
# Task -You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

# def split_and_join(line):
#     x = line 
#     x = x.split(" ")
#     x = "-".join(x)
#     return x

# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)

# What's your name? 
# You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following: Hello firstname lastname! You just delved into python.

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)