from itertools import combinations
str3 = ""
str,integer = input().split()
str2 = sorted(str, reverse=False)

for i in range(1,int(integer)+1):
    for i in combinations(str2,i):
        for j in i:
            str3 += j
        print(str3)
        str3 = ""