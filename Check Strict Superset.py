a={int(i) for i in input().split()}
n=int(input())
r=True
for i in range(n):
    x={int(i) for i in input().split()}
    if not(a > x):
        r=False
print(r)
        
