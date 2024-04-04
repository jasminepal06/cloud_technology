a, b, c = 2, 3, 0
print(a**b == b**a) # False
print(a < b or b < a) # True
print("dog" > "cat" + "mouse") # True
print("Car" < "Train") # True
print((a == b) and ((a * a < b * b) or (b < a) and (2 * a < b))) # False
print((a <= b) or ((a * a < b * b) or (b < a) and (2 * a < b))) # True
print(not ((a < b) and (a < (b + a)))) # False
print("small" > "large" and (not c)) # True
print(isinstance(c, int)) # True
print(isinstance(3.14, float)) # True
if a < b < c:
    b = c + a
else:
    b = c * a
print(b) # 0 
if "A" in "apple":
    print("A as apple.")
else:
    print("Oops, not there.") # printed since uppercase A is not in apple
x = 6
if x < 0:
    print("negative")
else:
    if x == 0:
        print("zero")
    else:
        print("positive") # printed as x is 6
n = 1
if n <= 9:
    print("Less than ten.") # printed because n is 1
elif n == 1:
    print("Equal to one.")
let = input("Enter A, B or C: \n")
let = let.upper()
if let == "A":
    print("\nA, my name is Alice.")
elif let == "B":
    print("\nTo be, or not to be.")
elif let == "C":
    print("\nOh, say, can you see.")
else:
    print("\nInvalid letter.")
