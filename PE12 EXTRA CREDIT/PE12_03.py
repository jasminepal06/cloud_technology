def append_to_file(filename, lines):
    with open(filename, 'a') as file:
        for line in lines:
            file.write(line + '\n')

lines_to_append = [
    "James Madison",
    "James Monroe",
    "John Quincy Adams"
]

filename = 'file_created_2.txt'

append_to_file(filename, lines_to_append)