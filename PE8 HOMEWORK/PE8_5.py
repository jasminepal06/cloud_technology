#  Create a dictionary
rank = {1: "Freshman", 2: "Sophomore", 3: "Junior", 4: "Senior"}

# Request a user input for a number of years.
num_years_input = input("Enter the # of years in the school <1-4>: ")
if not num_years_input.isdigit() or not (1 <= int(num_years_input) <= 4):
    # Print the error message if input is invalid.
    print('Invalid years.')
else:
    ranking = rank[int(num_years_input)]
    # Print the value of the matching key in the dictionary
    print(f'Year {num_years_input} - {ranking}')
