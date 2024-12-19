attempts = 0
pin = input("PIN:")
correct_pin = "4321"
while pin != correct_pin:
    print("Wrong")
    attempts += 1
    pin = input("PIN:")
print(f"Correct! it took you {attempts} attempts") 

####################################################ChatGpt

pin = "4321"
count = 0
while True:
    attempt = input("PIN: ")
    count += 1
    if attempt == pin:
        if count == 1:
            print("Correct! It only took you one single attempt!")
        else:
            print("Correct! It took you", count, "attempts")
        break
    else:
        print("Wrong")
#############################################################Model Solution

attempts = 1
while True:
    pin = input("PIN: ")
    if pin == "4321":
        break
    print("Wrong")
    attempts += 1
 
if attempts == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempts} attempts")
 