# Requesting the lower bound, lower and the upper bound, upper from the console.
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

# Requesting an increment value incVal from the console.
incVal = int(input("Enter the increment value: "))

print("USING WHILTE LOOP")
# Use a while loop to increment from lower to upper by increments of incVal
while lower <= upper:
    print(lower, end="\n")
    temp = lower + incVal
    # Using a while loop to vertically print all values in between each increment
    while lower < temp <= upper:
        print(temp, end="\n")
        temp += incVal
    print()
    lower += incVal

print("\nUSING FOR LOOP")
# Using a for loop to vertically print all values in between each increment
for num in range(lower, upper + 1, incVal):
    print(num, end="\n")
    for temp in range(num + incVal, min(num + 2 * incVal, upper + 1), incVal):
        print(temp, end="\n")
    print()