# Take input from the user
limit = int(input("limit: "))

# Initialize variables
current_sum = 0
next_num = 1

# Loop until the sum is at least equal to the limit
while current_sum < limit:
    current_sum += next_num
    next_num += 1

# Print the result
print(current_sum)
