from itertools import combinations
a,b = input().split()
r=sorted(combinations(a,int(b)))
for i in r:
    a="".join(i)
    print(a)
