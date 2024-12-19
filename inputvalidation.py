from math import sqrt

while True:
    numbers = int(input("Please type in a number:"))
    if numbers < 0:
        print("Invalid number")
    elif numbers > 0:
        print(f"{sqrt(numbers)}")
    elif numbers == 0:
        break
print("Exiting...")