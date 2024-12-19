input_string = input("Please type in a string:")
 
if len(input_string) < 20:
    num_stars = 20 - len(input_string)
    print("*" * num_stars + input_string)
else:
    print(input_string[:20]) 

#model solution
word = input("Please type in a string: ")
 
aligned = (20 - len(word)) * "*" + word
 
print(aligned)