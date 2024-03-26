multiples_of_4 = [num * 4 for num in range(0, 11)]
print(multiples_of_4)
multiples_of_2 = []
for num in multiples_of_4:
    multiples_of_2.append(num // 2)
print(multiples_of_2)
numbers_0_to_10 = multiples_of_2[:]
for i in range(len(numbers_0_to_10)):
    numbers_0_to_10[i] //= 2
print(numbers_0_to_10)