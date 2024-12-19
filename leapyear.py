year = int(input("Please type in a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("That year is a leap year.")
        else:
            print("That year is not a leap year.")
    else:
        print("That year is a leap year.")
else:
    print("That year is not a leap year.")

#The program first takes input from the user and stores it as an integer in the variable year. 
# It then checks whether the year is divisible by 4 using the modulo operator %. 
# If the year is not divisible by 4, the program prints "That year is not a leap year." and terminates. 
# If the year is divisible by 4, the program checks whether it is divisible by 100. 
# If it is, the program checks whether it is divisible by 400. 
# If the year is divisible by 400, it is a leap year and the program prints "That year is a leap year." 
# Otherwise, the program prints "That year is not a leap year." If the year is not divisible by 100, 
# it is a leap year and the program prints "That year is a leap year.