import numpy

def arrays(arr):
    r=numpy.array(arr[::-1],float)
    return r
arr = input().strip().split(' ')
result = arrays(arr)
print(result)
