a=int(input())
b=set([int(i) for i in input().split()])
c=int(input())
d=set([int(i) for i in input().split()])
r=b.intersection(d) # or r=b&d
print(len(r))
