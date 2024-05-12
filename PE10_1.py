# Define a function printList() with one parameter p.
def printList(p):
    # print all the values in the list of p
    for value in p:
        print(value)

def main():
    # Create a list of strings called lst
    lst = ["apple", "banana", "cherry"]
    # Call the function printList() with lst as an argument
    printList(lst)

# Call main() function to initiate the tasks to be performed
main()