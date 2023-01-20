print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
split = int(input("How many people should split the bill? "))

tip_percent = tip / 100 + 1

each_pay = (total / split) * tip_percent
round_each_pay = "{:.2f}".format(each_pay)

print(f"Each person should pay: ${round_each_pay}")