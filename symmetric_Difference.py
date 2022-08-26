M = int(input())
mset = set(map(int, input().split()))
N = int(input())
nset = set(map(int, input().split()))

mdef = mset.difference(nset)
ndef = nset.difference(mset)

output = mdef.union(ndef)

for i in sorted(list(output)):
    print(i)