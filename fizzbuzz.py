number = int(input("Number:"))
if number % 3 == 0 and number % 5 == 0:
    print (f"FizzBuzz")
elif number % 3 == 0:
    print (f"Fizz")
elif number % 5 == 0:
    print(f"Buzz")
print(f"Number: %d" % number)