from itertools import combinations_with_replacement
str3 = ""
str,integer = input().split()
str2 = sorted(str, reverse=False)

for i in combinations_with_replacement(str2, int(integer)):
    for j in i:
        str3 += j
    print(str3)
    str3 = ""