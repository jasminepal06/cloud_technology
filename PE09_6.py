from random import randint

def middle(l):
    return l[1:-1]

def main():
    # Get a random integer, n, in the range (1, 10).
    n = randint(1, 10)
    # Create a list, numList with n numbers in the list.
    numList = list(range(1, n + 1))
    print(f'List length = {n}')

    print(numList)

    # Call middle(numList) function and print the returned list.
    middle_list = middle(numList)
    print(middle_list)

# Call main() function to initiate the tasks to be performed.
main()