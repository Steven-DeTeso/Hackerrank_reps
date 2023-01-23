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

# def print_full_name(first, last):
#     print(f"Hello {first} {last}! You just delved into python.")

# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)

# Intro to sets - A set is an unordered collection of elements without duplicate entries.
# When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order. 
# Now, let's use our knowledge of sets and help Mickey. Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

def average(array):
    # your code goes here
    # grab the set into a var
    total = set(array)
    # sum the nums in the var and store in diff var
    sum_of_set = sum(total)
    # check the length of the set 
    len_of_set = len(total)
    # write function that divides var of sum by var of length 
    avg = sum_of_set / len_of_set
    # format to 3 decimle places
    round(avg, 3)
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)