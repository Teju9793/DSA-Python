import re
n=int(input())
l=[]
p=r"^[+-]?[0-9]*\.[0-9]+$"
for i in range(n):
    k=input()
    print(bool(re.match(p,k)))
    
