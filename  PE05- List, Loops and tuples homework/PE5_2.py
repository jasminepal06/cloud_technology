even_numbers = []
for num in range(0, 101):
    if num % 2 == 0:
        even_numbers.append(num)
first_five_even = even_numbers[:5]
print(first_five_even)
last_five_even = even_numbers[-5:]
print(last_five_even)
between_20_and_30 = even_numbers[10:16]
print(between_20_and_30)