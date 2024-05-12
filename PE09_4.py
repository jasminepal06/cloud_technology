# Modify the function, hello() above with a parameter
def hello():
    print("Hello World")

# Define the function, helloNo(n) with a loop to call hello() n times to the console.
def helloNo(n):
    # Use the parameter, n for the numbers of iterations in the loop.
    for _ in range(0, n):
        hello()

helloNo(3)