import numpy
numpy.set_printoptions(legacy='1.13') 
n,m=list(map(int,input().split()))
r=numpy.eye(n,m,dtype=float)
print(r)
