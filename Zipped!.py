n,x=map(int,input().split())
l=[]
for i in range(x):
    marks=list(map(float,input().split()))
    l.append(marks)
r=list(zip(*l))
for i in r:
    result=sum(i)/x
    print(result)
