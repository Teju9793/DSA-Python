from collections import Counter
a=int(input())
b=[int(i) for i in input().split()]
for r,co in Counter(b).items():
    if co==1:
        print(r)
