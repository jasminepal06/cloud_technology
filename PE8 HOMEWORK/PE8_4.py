# Create a dictionary, stuInfo with the keys name, gpa, and age. 
stuInfo = {
    'name': 'Jasmine Pal',
    'gpa': 3.456,
    'age': 17
}

# Use a loop and the items() method to print all keys and values
for key, value in stuInfo.items():
    print(f"{key.upper()}   {value}")

#  Use the update() method to change the gpa to 4.0.
stuInfo.update({'gpa': 4.0})
print()

# Use a loop and the keys() method to print all keys and values
for key, value in stuInfo.items():
    print(f"{key.upper()}   {value}")

print()

# Add a key major with the value to the dictionary
stuInfo['major'] = 'CSIS'

# Use a loop and the values() method to print all values
for value in stuInfo.values():
    print(value, end = '|')

# Use two different ways to delete gpa and age in the dictionary.
stuInfo.pop('gpa')
stuInfo.pop('age')

print()
# Print the updated dictionary.
print(stuInfo)