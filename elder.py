print("Person 1:\n")
first_person = (input("Name:"))
age_of_person1 = int(input("Age:"))

print("Person 2:\n")
second_person = (input("Name:"))
age_of_person2 = int(input("Age:"))

if age_of_person1 > age_of_person2:
    print(f"The elder is {first_person}")
elif age_of_person1 == age_of_person2:
    print(f"{first_person} and {second_person} are the same age")
else:
    print(f"The elder is {second_person}")
