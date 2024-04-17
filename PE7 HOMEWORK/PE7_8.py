# Request two numbers, n1 and n2 from the console
n1 = int(input("Enter a number n1: "))
n2 = int(input("Enter a number n2: "))

if n1 < n2:
    i = n1
    # Using a while loop to horizontally print n1 to n2 with increment by 1 if n1 is smaller than n2
    while i <= n2:
        print(i, end="|")
        i += 1
    print()

elif n1 > n2:
    # Using a for loop to horizontally print n1 to n2 with decrement by 1 if n1 is greater than n2
    for i in range(n1, n2 - 1, -1):
        print(i, end="|")
    print()

else:
    # Printing a message, “n1 = n2” if n1 is equal to n2
    print(f"n1 = n2")