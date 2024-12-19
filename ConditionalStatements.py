#number = int(input("Please enter a number:"))

#if number == 1984:
    #print("Orwell")

#number = int(input("Please enter a number: "))

#if number < 0:
    #print(f"The absolute value of this number is {number * (-1)} ")
#else:
    #print(f"The absolute value of this number {number}")

#name = input("Please tell me your name:")
#price_of_single_portion = 5.90

#if name != "Jerry":
  # portions_of_soup = int(input("How many portions of soup?"))
   #total_cost = portions_of_soup * price_of_single_portion
   #print(f"The total cost is {total_cost}")

#print ("Next Please!")



# Ask the user for an integer number
#number = int(input("Please type in a number: "))

# Determine the magnitude of the number and print out the appropriate message
#if number >= 1000:
 #   pass # no message needs to be printed for this case
#else:
#    print("This number is smaller than 1000")

#if number >= 100:
   # pass # no message needs to be printed for this case
#else:
  #  print("This number is smaller than 100")

#if number >= 10:
   # pass # no message needs to be printed for this case
#else:
   ### print("This number is smaller than 10")

# Print out a thank you message
#print("Thank you!")

#Second Solution 
#number = int(input("Please type in a number: "))
#if number < 1000:
   # print("This number is smaller than 1000")
 
#if number < 100:
    #print("This number is smaller than 100")
 
#if number < 10:
    #print("This number is smaller than 10")
 
#print("Thank you!")



# make clothing suggestion based on temperature

import math

# input values of a, b, and c
a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))

# calculate discriminant
discriminant = b**2 - 4*a*c

# calculate roots
root1 = (-b + math.sqrt(discriminant)) / (2*a)
root2 = (-b - math.sqrt(discriminant)) / (2*a)

# print roots
print("The roots are", root1, "and", root2)

#Module solution
from math import sqrt
 
a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))
 
discriminant = b**2 - (4 * a * c)
 
root1 = (-b + sqrt(discriminant)) / (2 * a)
root2 = (-b - sqrt(discriminant)) / (2 * a)
 
print(f"The roots are {root1} and {root2}")
# Let's take the square root of math-module in