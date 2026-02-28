from itertools import combinations_with_replacement
s,n=input().split()
n=int(n)
s=sorted(s)
x= list(combinations_with_replacement(s,n))
for i in x:
    print("".join(i))
