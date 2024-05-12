# Define a function nameFormat() with parameters first, middle, and last
def nameFormat(first, middle, last):
    # This function prints the first name, the middle initial and the last name using proper title format
    print(f"{first.capitalize()} {middle.capitalize()[0]}. {last.capitalize()}")

def main():
    # Call the function nameFormat with these positional arguments: john stu smith
    nameFormat("john", "stu", "smith")

    # Call the function nameFormat with these keyword arguments: last = ‘kennedy’, first = ‘john’, middle = ‘fitzgerald’
    nameFormat(last="kennedy", first="john", middle="fitzgerald")

# Call main() function to initiate the tasks to be performed
main()