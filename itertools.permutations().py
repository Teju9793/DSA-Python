from itertools import permutations
a,b = input().split()
r=sorted(list(permutations(a,int(b))))
for i in r:
    a="".join(i)
    print(a)
