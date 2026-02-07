m=int(input())
a={int(i) for i in input().split()}
n=int(input())
b={int(i) for i in input().split()}
r=sorted(list(a^b))
for i in r:
    print(i)
