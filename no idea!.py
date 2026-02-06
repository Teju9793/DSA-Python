m,n=input().split()
a=[int(i) for i in input().split()]
sa={int(i) for i in input().split()}
sb={int(i) for i in input().split()}
h=0
for i in a:
    if i in sa:
        h+=1
    elif i in sb:
        h-=1
    else:
        h+=0
print(h)
