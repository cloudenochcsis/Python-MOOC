# Ask user for three letters
# We use the input() function to ask the user for three letters and store them in separate variables.
first_letter = input("1st letter: ")
second_letter = input("2nd letter: ")
third_letter = input("3rd letter: ")

# Put letters into a list and sort them alphabetically
# We create a list called letters and add the three letters to it.
# We then use the sort() method to sort the letters in alphabetical order.

letters = [first_letter, second_letter, third_letter]
letters.sort()

# Print out the middle letter
print("The letter in the middle is", letters[1])
