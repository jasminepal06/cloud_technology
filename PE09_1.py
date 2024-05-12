from math import fmod

# Use input() function to request any two numbers.
numerator = input("Enter a numerator: ")
denominator = input("Enter a denominator: ")
# Implement the validation of denominator to be a non-zero number in a sentinel-controlled loop.
if denominator != 0:
    # Use math module, fmod() to return the remainder of the user input.
    mod = fmod(int(numerator), int(denominator))
    # Print out the result as an integer
    print(f"{numerator} mod {denominator} {int(mod)}")
else:
    print("Denominator cannot be zero. Try again.")