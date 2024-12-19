word = input("Please type in a string: ")
if "a" in word:
    print("a found")
else:
    print("a not found")

if "e" in word:
    print("e found")
else:
    print("e not found")

if "o" in word:
    print("o found")
else:
    print("o not found")


#####################################

string = input("Please type in a string: ")
vowels = "aeo"
index = 0
 
while index < len(vowels):
    vowel = vowels[index]
    if vowel in string:
        print(vowel, "found")
    else:
        print(vowel, "not found")
    index += 1
 