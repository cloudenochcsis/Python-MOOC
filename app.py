
#Asking the user for input
num_students = int(input("How many students on the course?"))
group_size = int(input("Desired group size?"))

#Calculate the the number of groups formed

number_of_groups = num_students // group_size
remainder = num_students % group_size

#print the result
if remainder == 0:
    print(f"Number of groups formed: {number_of_groups}")
else:
    print(f"Number of groups formed {number_of_groups + 1}")