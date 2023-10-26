print("^^^^^^^^^^^^^^^^^^^^^^^^")
bill = input("Welcome to the tip calculator. How much was the bill?")
tip = input("How much would you like to tip?")
print(f"Your suggested tip amount is {round(int(bill) * (int(tip) / 100),2)}")
