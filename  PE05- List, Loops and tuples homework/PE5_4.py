months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
print("Original list:")
print(months)

abbreviated_months = []
for month in months:
    abbreviated_months.append(month[:3].upper())

print("\nThree-letter abbreviation 1 - 12:")
print('|'.join(month.upper()[:3] for month in months))

newList = []
for month in months:
    newList.append(month[:3].capitalize())
print("\nNew list:")
print(newList)