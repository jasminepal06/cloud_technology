# Define a function average() with a parameter grades that can accept an arbitrary number of integer values
def average(*grades):
    # This function returns the average of all values
    if len(grades) == 0:
        return 0.0
    return sum(grades) / len(grades)

# Main function to perform the specified tasks
def main():
    # Call the average() function with the following arguments: 95,87,83,74
    grades1 = [95, 87, 83, 74]
    result1 = average(*grades1)
    print(f"Average of {', '.join(map(str, grades1))}: {result1:.2f}")

    # Create two random integers, x and y. x is from range -100 to 0, and y is range from 0 to 100 inclusively.
    x = -41
    y = 67
    # Call the average() function with x and y
    result2 = average(x, y)
    # Print al the results with the average computed to two decimal places.
    print(f"Average of any two random numbers, {x}, {y}: {result2:.2f}")

# Call main() function to initiate the tasks to be performed
main()
