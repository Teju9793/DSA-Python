from collections import namedtuple
l=int(input())
c=input().split()
marks=0
x= namedtuple("score",c)
for i in range(l):
    
    data=input().split()
    n=x(*data)
    marks += int(n.MARKS)
    

print(f"{marks/l:.2f}")
