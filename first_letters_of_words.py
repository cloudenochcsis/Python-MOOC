sentence = input("Please type in a sentence: ")
 
# Add a space at the start, to make handling sentence easier
sentence = " " + sentence
 
# Searching for indexes which are preceded by spaces
index = 1
while index < len(sentence):
    if sentence[index-1] == " " and sentence[index] != " ":
        print(sentence[index])
    index += 1