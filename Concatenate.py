import numpy as np
l1=[]
l2=[]
n,m,p=list(map(int,input().split()))
for i in range(n):
    e=list(map(int,input().split()))
    l1.append(e)
for j in range(m):
    e=list(map(int,input().split()))
    l2.append(e)
ar1=np.array(l1)
ar2=np.array(l2)
print(np.concatenate((ar1,ar2)))
