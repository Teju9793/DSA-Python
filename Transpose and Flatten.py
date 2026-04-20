import numpy
N,M = list(map(int,input().split()))
li=[]
for i in range(N):
    li.append(list(map(int,input().split())))
ar=numpy.array(li)
print(numpy.transpose(li))
print(ar.flatten())
