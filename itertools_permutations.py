# Average
from itertools import permutations
str3 = ""
str,integer = input().split()
str2 = sorted(str, reverse=False)


for i in permutations(str2,int(integer)):
    for j in i:
        str3 += j
    print(str3)
    str3 = ""
    
"""
---BEST--
from itertools import permutations

s,k = input().split()

words = list(permutations(s,int(k)))
words = sorted(words, reverse=False)
for word in words:
    print(*word,sep='')
"""