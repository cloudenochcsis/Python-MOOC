word = input("Please type in a string: ")
i = 0
sum = ""
while i < len(word):
    sum += word[i]
    print(sum)
    i += 1


#########

string = input("Please type in a string: ")
 
length = 1
while length <= len(string):
    print(string[0:length])
    length += 1
