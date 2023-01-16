# Task The provided code stub reads and integer,, from STDIN. For all non-negative integers , print.

# Example -The list of non-negative integers that are less than  is . Print the square of each number on a separate line.

# if __name__ == '__main__':
#     n = int(input())

# for i in range(n):
#     print(i**2)


# In the Gregorian calendar, three conditions are used to identify leap years:
# The year can be evenly divided by 4, is a leap year, unless:
    # The year can be evenly divided by 100, it is NOT a leap year, unless:
        # The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source

# Task - Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

# def is_leap(year):
#     leap = False
    
#     if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#         leap = True
#         return leap
#     else:
#         leap = False
#         return leap

# year = int(input())
# print(is_leap(year))

# The included code stub will read an integer, from STDIN.
# Without using any string methods, try to print the following:
# Note that "" represents the consecutive values in between.
# Example - Print the string.

# if __name__ == '__main__':
#     n = int(input())

# for i in range(1, n+1):
#     print(i, end="")
#     if i < n:
#         print("", end="")


# Map and Lamba Functions
# Let's learn some new Python concepts! You have to generate a list of the first  fibonacci numbers,  being the first number. Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.

# Concept
# The map() function applies a function to every member of an iterable and returns the result. It takes two parameters: first, the function that is to be applied and secondly, the iterables.
# Let's say you are given a list of names, and you have to print a list that contains the length of each name.
# Lambda is a single expression anonymous function often used as an inline function. In simple words, it is a function that has only one line in its body. It proves very handy in functional and GUI programming.
# Note: Lambda functions cannot use the return statement and can only have a single expression. Unlike def, which creates a function and assigns it a name, lambda creates a function and returns the function itself. Lambda can be used inside lists and dictionaries.

# cube = lambda x: x**3

# def fibonacci(n):
    # if n == 0:
    #     return []
    # elif n == 1:
    #     return [0]
    # else:
    #     fib_list = []
    #     fib_list.append(0)
    #     fib_list.append(1)
    #     for i in range(2, n):
    #         fib_list.append(fib_list[i-1] + fib_list[i-2])
    # return fib_list



# Validating Email Addresses With a Filter
