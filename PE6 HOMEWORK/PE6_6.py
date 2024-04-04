n = eval(input("Enter a number: "))
if n == 7: # double equals are required to compare
    print("The square is", n*2)

n = 6
if n > 5 and n < 9: # You have to rewrite the variable you are trying to see is greater or less than
    print("Yes")
else:
    print("No")

major = "Computer Science"
if major == "Engineering Technology" or "Computer Technology": # you need a lowercase o inside or and 
    print("Yes")

a, b = 1, 1.0
if a == b: # when comparing you have to use double equals
    print("same")