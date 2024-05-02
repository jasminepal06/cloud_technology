dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}
copied_dict = dict1.copy()
dict1.copy().update(dict2)
print(copied_dict)