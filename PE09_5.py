from random import randint

# message(p1, p2) uses a loop to print the text stored in p1, p2 times to the console.
def message(p1, p2):
    for _ in range(0, p2):
        print(p1)

def main():
    # Request and print an input text from the console and print the text.
    text = input('Enter a text: ')
    print(f'text = {text}')

    # Get a random integer number, n, in the range (1, 10) and print n
    n = randint(1, 10)
    print(f'n = {n}')
    
    # Call message() function with arguments, text and n, Handle all input and output
    print('message(text, n) will print the following:')
    message(text, n)

#  Call main() function to initiate the tasks to be performed
main()