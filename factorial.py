while True:
    number = int(input("Please type in a number: "))
    if number <= 0:
        break
 
    factorial = 1
    new = 1
    while new <= number:
        factorial = factorial * new
        new = new + 1
 
    print(f"The factorial of the number {number} is {factorial}")
 
print("Thanks and bye!")
