input_string = input("Please type in a string:")

if input_string[1] != input_string[-2]:
    print ("The second and the second to last characters are different")
elif input_string[1] == input_string[1]:
    print (f"The second and the second to last characters are {input_string[1]}") 

#model solution 
word = input("Please type in a string: ")
 
# Check also that the word is at least two characters long,
# so that the second and second to last characters exist
if len(word) > 1 and word[1] == word[-2]:
    print("The second and the second to last characters are " + word[1])
else:
    print("The second and the second to last characters are different")