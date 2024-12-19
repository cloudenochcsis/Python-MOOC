# Ask user for the value of the gift received
gift_value = float(input("Value of gift: "))

# Determine the amount of tax to be paid based on the gift value and tax table
if gift_value < 5000:
    gift_tax = "No tax!"
elif gift_value < 25000:
    gift_tax = 100 + (gift_value - 5000) * 0.08
elif gift_value < 55000:
    gift_tax = 1700 + (gift_value - 25000) * 0.1
elif gift_value < 200000:
    gift_tax = 4700 + (gift_value - 55000) * 0.12
elif gift_value < 1000000:
    gift_tax = 22100 + (gift_value - 200000) * 0.15
else:
    gift_tax = 142100 + (gift_value - 1000000) * 0.17

# Print out the amount of gift tax to be paid
print("Amount of tax:", gift_tax, "euros")


################################################################

value = int(input("Value of gift: "))
 
if value < 5000:
    tax = 0
elif value <= 25000:
    tax = 100 + (value - 5000) * 0.08
elif value <= 55000:
    tax = 1700 + (value - 25000) * 0.10
elif value <= 200000:
    tax = 4700 + (value - 55000) * 0.12
elif value <= 1000000:
    tax = 22100 + (value - 200000) * 0.15
else:
    tax = 142100 + (value - 1000000) * 0.17
 
if tax == 0:
    print("No tax!")
else:
    print(f"Amount of tax: {tax} euros")


