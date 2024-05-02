# Create three stuInfo dictionaries with the keys: name and value: gpa. 
stuInfo1 = {'name': 'tom cat', 'gpa': 3.456}
stuInfo2 = {'name': 'jerry mouse', 'gpa': 4.0}
stuInfo3 = {'name': 'sponge bob', 'gpa': 3.99}

# Create a list stuClass, add all dictionaries to this list, and print the list.
stuClass = [stuInfo1, stuInfo2, stuInfo3]
print('All students in list:')
print(stuClass)

print('All students information:')
# Use a loop to print all students from the list of stuClass
for index, student in enumerate(stuClass, 1):
    print(f"student {index} {student}")

print('All gpa information:')
# Use a loop to print all the gpa.
for student in stuClass:
    print(student['gpa'], end='|')

# Change the last student’s gpa to 4.0.
stuClass[-1]['gpa'] = 4.0

# Add a new student info to the list.
new_student = {'name': 'David', 'gpa': 3.7}
stuClass.append(new_student)

print('All the updated information:')
# Use a loop to print all the names and gpa with proper format as the output below.
for student in stuClass:
    print(f'{student['name']}    {student['gpa']}')
