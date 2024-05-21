def using_loop(filename):
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())

def using_list(filename):
    with open(filename, 'r') as file:
        presidents = file.readlines()
        for president in presidents:
            print(president.strip())

filename = 'Presidents.txt'

print("Using Loop ------")
using_loop(filename)

print("Using List ------")
using_list(filename)