from itertools import combinations
x=int(input())
y=input().split()
k=int(input())
a=0
co=list(combinations(y,k))
for i in co:
    if "a" in i:
        a+=1
print(a/len(co))
