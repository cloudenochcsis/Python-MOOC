word = input("Please type in a word: ")
character = input("Please type in a character: ")
 
index = 0
 
while index + 3 <= len(word):
    if word[index] == character:
        print(word[index:index+3])
    index += 1