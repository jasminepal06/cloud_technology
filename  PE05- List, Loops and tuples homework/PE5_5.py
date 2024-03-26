range_input = int(input("Enter a range: "))
numbers_list = list(range(1, range_input + 1))
number_input = int(input("Enter an integer number: "))

print(f"\nMultiplication Table of {number_input}")
for num in numbers_list:
    result = num * number_input
    print(f"{num}    *    {number_input}    =    {result}")