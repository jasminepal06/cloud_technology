a = list(range(5))
print(a) # [0, 1, 2, 3, 4]
b = []
for i in range (5):
 b.append(i)
print(b) # [0, 1, 2, 3, 4]
x = list(range(-10, 10))
print(x) # [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(min(x), max(x), sum(x)) # -10 9 -10
even_num = list(range(2, 11, 2))
print(even_num[0], even_num[-1]) # 2 10
odd_num = []
for num in range(1, 10):
    if num % 2 != 0:
        odd_num.append(num)
print(odd_num) # [1, 3, 5, 7, 9]
cubes = []
for num in range(1, 11):
    cube = num ** 3
    cubes.append(cube)
for cube in cubes:
    print(cube)
cubes = [num ** 3 for num in range(1, 11)]
for cube in cubes:
    print(cube, end='|') # 1|8|27|64|125|216|343|512|729|1000|
print()