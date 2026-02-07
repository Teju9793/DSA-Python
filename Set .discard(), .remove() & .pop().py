n = int(input())
s = set(map(int, input().split()))
m=int(input())
a=[]
for i in range(m):
    a.append(input().split())
for cmd in a:
    if len(cmd)==1:
        f=cmd[0]
        n=0
        s.pop()
        
    else:
        f=cmd[0]
        n=int(cmd[1])
        if f=="discard":
            s.discard(n)
        elif f=="remove":
            s.remove(n)
print(sum(s))
    
        

    
