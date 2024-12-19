# Write your solution here
story = ""
previous = ""
while True:
    word = input("Please type in a word: ")
    if word == "end" or word == previous:
        break
    story = story + word + " "
    previous = word
 
print(story)