

name = input("Enter your name: ")
age = int(input("Enter your age: "))

mark1 = int(input("Enter marks for Subject 1: "))
mark2 = int(input("Enter marks for Subject 2: "))
mark3 = int(input("Enter marks for Subject 3: "))

average = (mark1 + mark2 + mark3) / 3

print("\n--- Student Details ---")
print("Name:", name)
print("Age:", age)
print("Average Marks:", average)