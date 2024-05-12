# Define a function nameFormat() with parameter first, last and middle where middle is an optional parameter
def nameFormat(first, last, middle=None):
    # If all three names are provided return: Last, First, M.
    if middle:
        return f"{last.capitalize()}, {first.capitalize()}, {middle.capitalize()[0].upper()}."
    
    # If only first and last are provided return: Last, First
    return f"{last.capitalize()}, {first.capitalize()}"

def main():
    # Call the function with keyword arguments for the name: james bond
    result1 = nameFormat(first="james", last="bond")
    #  Call the function with keyword arguments for the name: henry indiana jones
    result2 = nameFormat(first="henry", last="jones", middle="indiana")
    
    # Print the results of the function calls.
    print(result1)
    print(result2)

# Call main() function to initiate the tasks to be performed
main()