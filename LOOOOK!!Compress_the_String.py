from itertools import groupby
data = input()
groups = []
uniquekeys = []
data = sorted(data)
for k, g in groupby(data):
    groups.append(list(g))      
    uniquekeys.append(k)
print(groups,uniquekeys)