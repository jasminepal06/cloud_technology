fruits = ["apple", "pear", 'python',]
for item in fruits:
    print("{item.title()} is my favorite!") # because there is no f infront of the quote
    print(f"I want to have more {item}.\n")
numbers = [1,2,3,4,5]
for n in numbers:
    print(n)
    print("That’s all the numbers in the list.")
    print("numbers = ", numbers) # it shows the list because the variable is not inside of the quotes
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
for i in n:
    print(i, end = '\t')
count += 1
print(f"\nThere are {count} numbers in the list.") # because the quotes start with a f, which allows variables to be inside quotes
print("n = ", n) # because it is out of the quotes, which doesnt require to have a f infront
languages = ["c++", "java", "python"]
for code in languages:
    print(code.upper(), end = " | ")
else:
    print("Enjoy coding!") # waits for the code to finish the loop to then add the enjoy coding
n = -6, 7, 3, -2, 6, 3, 9
print(len(n), max(n), min(n), sum(n), sep = '\n')
print(n.count(3), n.index(3), n[-6:6], sep = '\n')
print(n, sorted(n), sep = '\n')

a = 2
b = 3
print(type(a+b)) # int, because a and b are ints 
print(type((a+b,))) # tuple, because the given argument is a tuple
print(type(())) # tuple, because the given argument is a tuple