NY = {"BX":1.42, "MN":1.63, "QS":2.25, "BN":2.56, "SI": 0.47}
print((NY['QS'])) # 2.25
print(NY.get("QS")) # 2.25
print(NY.get("LI", "Not in")) # Not in
print(NY.get('SI', 'absent')) # 0.47
print(NY.setdefault('SI', 0.48)) # 0.47
print("LI" in NY) # False
print('MN' not in NY) # False
print(len(NY), min(NY), max(NY)) # 5 BN SI
print(len(NY.items()), max(NY.keys()), min(NY.values())) # 5 SI 0.47
print(round(NY['QS'])) # 2
NY['QS'] += .3
print(round(NY['QS'], 1)) # 2.5
print(NY.keys()) # ['BX', 'MN', 'QS', 'BN', 'SI']
print(list(NY.values())) # [1.42, 1.63, 2.55, 2.56, 0.47]
print(tuple(NY.items())) # ('BX', 1.42), ('MN', 1.63), ('QS', 2.55), ('BN', 2.56), ('SI', 0.47)
total = 0
for x in NY.values():
 total += x
print(f'{total:.1f}') # 8.6
total = 0
for x in NY:
 total += NY[x]
print(f'{total:.1f}') # 8.6
for x in sorted(NY) : print(x, end = '|') # BN|BX|MN|QS|SI|
for x in sorted(NY, reverse=True) : print(x, end = '|') # SI|QS|MN|BX|BN|
print(", ".join(f"{value:.2f}" for value in NY.values())) # 2.56, 2.25, 1.63, 1.42, 0.47
if "QS" in NY: print("Queens is the most diverse county in NY.") # ueens is the most diverse county in NY.
for x, y in NY.items():
 if y > 2.5: print(f"{x} is the Kings county!") # QS is the Kings county! | BN is the Kings county!
NY["SK"] = 1.49
print(NY) # {'BX': 1.42, 'MN': 1.63, 'QS': 2.55, 'BN': 2.56, 'SI': 0.47, 'SK': 1.49}
NY.update({"NU":1.34})
print(NY) # {'BX': 1.42, 'MN': 1.63, 'QS': 2.55, 'BN': 2.56, 'SI': 0.47, 'SK': 1.49, 'NU': 1.34}
NY.pop("QS")
NY.popitem()
print(NY) # {'BX': 1.42, 'MN': 1.63, 'BN': 2.56, 'SI': 0.47, 'SK': 1.49}
newYork = NY
del newYork['BN']
print(NY) # {'BX': 1.42, 'MN': 1.63, 'SI': 0.47, 'SK': 1.49}
print(newYork) # {'BX': 1.42, 'MN': 1.63, 'SI': 0.47, 'SK': 1.49}
newYork = dict(NY)
print(len(NY)) # 4
print(len(newYork)) # 4
NewYork = NY.copy()
NY.clear()
print(NY) # {}
print(NewYork) # {'BX': 1.42, 'MN': 1.63, 'SI': 0.47, 'SK': 1.49}
del NY
print(set(NewYork)) # {'SI', 'SK', 'MN', 'BX'}