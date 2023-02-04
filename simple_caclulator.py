logo = """
______________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

""" Definitions of simple calculations below"""

# add
def add(n1, n2):
    return n1 + n2

# subtract 
def subtract(n1, n2):
    return n1 - n2

# multiple 
def multiply(n1, n2):
    return n1 * n2

# divide 
def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

# example of recurion inbetted below here. Need to set flag for while loop to avoid infinate loop.
def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for key in operations:
    print(key)
    
  should_continue = True
  while should_continue:
      
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculator_function = operations[operation_symbol]
    answer = calculator_function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue to calculating with {answer} or 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      # example of recurions here because function call is imbedded in itself.
      calculator()

calculator()