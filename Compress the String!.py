# Enter your code here. Read input from STDIN. Print output to STDOUTf
from itertools import groupby
a = input()
x=[(len(list(j)),int(i)) for i,j in groupby(a)]
print(*x)
 
