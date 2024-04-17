import random

# Requesting an integer input for the numbers of grades in the list.
num_grades = int(input("Enter the number of grades in the list: "))

# Using a loop to generate random grades (1 – 100) in the list, grades.
grades = []
for _ in range(num_grades):
    grade = random.randint(1, 100)
    grades.append(grade)

# Requesting a user input for the passing grade.
passing_grade = int(input("Enter the passing grade: "))

# Use a loop to store all the passing grades into a new list, passGrades.
pass_grades = []
for grade in grades:
    if grade <= passing_grade:
        pass
    pass_grades.append(grade)

# Printing all the lists.
print("Updated List:", pass_grades)
print("Original List:", grades)