input_string = input("Please type in a string:")
index = -1
while index >= -len(input_string):
    print(input_string[index])
    index = index - 1


# Ask user for input string
input_string = input("Enter a string: ")

# Reverse the input string using slicing
reverse_string = input_string[::-1]

# Print each character in the reversed string on a separate line
for char in reverse_string:
    print(char)