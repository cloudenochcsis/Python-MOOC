string = input("Please type in a string: ")
substring = input("Please type in a substring: ")
 
index1 = string.find(substring)
index2 = -1
if index1 != -1:
    string = string[index1+len(substring):]
    index2 = string.find(substring)
 
if index2 == -1:
    print("The substring does not occur twice in the string.")
else:
    print("The second occurrence of the substring is at index " + str(index1+len(substring)+index2) +  ".")