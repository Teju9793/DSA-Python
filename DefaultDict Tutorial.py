from collections import defaultdict
n,m =map(int,input().split())
A=[]
B=[]
for i in range(n):
    A.append(input())
for j in range(m):
    B.append(input())
k=defaultdict()

for b in B:
    if b in A:
        position=[i for i,x in enumerate(A,start=1) if x==b]
        k[b]=position
        print(" ".join(map(str,k[b])))
    else:
        print(-1)
    
