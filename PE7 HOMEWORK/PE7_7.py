numbers = []

# Implementing a while loop to request numbers from the console and insert them into a list. 
while True:
    num = input("Enter a number or 0 to stop: ")
    # Stop requesting values if the user input is a zero
    if num == '0':
        break
    
    try:
        # Inserting all the numbers into a list
        num = float(num)
        numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Printing all elements of the list, sum and average
sum_numbers = sum(numbers)
print("Sum = ", sum_numbers)

if numbers:
    average = sum_numbers / len(numbers)
    print("Average = ", average)
else:
    print("Average = 0")

print("Number(s) entered: \n", numbers)
