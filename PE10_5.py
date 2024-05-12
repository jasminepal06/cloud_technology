# Define a function createUser() with an arbitrary dictionary parameter
def createUser(name, age, **kwargs):
    user = {'name': name, 'age': age}
    user.update(kwargs)
    return user

# Define a function printUser() with a parameter user which is a dictionary
def printUser(user):
    # This function prints the contents of the dictionary user
    print(f"name: {user['name']}")
    print(f"age: {user['age']}")
    for key, value in user.items():
        if key not in ['name', 'age']:
            print(f"{key.lower()}: {value}")

# Create and print the user: John, age 43, job Programmer, Hobby Biking
john = createUser('John', 43, job='Programmer', hobby='Biking')
printUser(john)

print()

#  Create and print the user: Sara, age 20, school QCC, major CSIS
sara = createUser('Sara', 20, school='QCC', major='CSIS')
printUser(sara)