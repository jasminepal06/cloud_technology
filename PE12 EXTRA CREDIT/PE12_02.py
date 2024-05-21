def create_file(filename, text):
    with open(filename, 'w') as file:
        file.write(text)

def create_file_2(filename, lines):
    with open(filename, 'w') as file:
        for line in lines:
            file.write(line + '\n')

create_file('file_created.txt', "George Washington\nJohn Adams")

create_file_2('file_created_2.txt', [
    "George Washington",
    "John Adams",
    "Thomas Jefferson"
])