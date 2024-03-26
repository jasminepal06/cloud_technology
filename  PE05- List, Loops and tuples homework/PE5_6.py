fruits = ["apple", "banana", "cherry"]
for item in fruits: # missing :
 print(item)
for i in range (1, 4):
   print(str(i) + '\t' + str(2**i)) # have to convert everything to string to concate with another string
#Why is there no output when you run the code?
for j in range(1, 6, -1): # because range doesnt work with negative step value
   print(j)
#How to display all the elements in uppercase?
letters = ['a', 'b', 'c']
for i in range(len(letters)):
    letters[i] = letters[i].upper()
print(letters)
fruits = ('apple', 'banana', 'cherry')
print(fruits)
fruits = ('orange',) + fruits[1:]
print(fruits)
