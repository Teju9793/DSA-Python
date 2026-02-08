from itertools import product
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
ab=list(product(a,b))
for i in ab:
    print(i,end=" ")
