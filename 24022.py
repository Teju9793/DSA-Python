from collections import OrderedDict
a=int(input())
x=OrderedDict()
for i in range(a):
    w=input()
    if w in x:
        x[w]+=1
    else:
        x[w]=1
print(len(x))
print(*x.values())
