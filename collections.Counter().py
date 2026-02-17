from collections import Counter
x=int(input())
size=list(map(int,input().split()))
cstmr=int(input())
sa=Counter(size)
ammount=0
for i in range (cstmr):
    size,pay =map(int,input().split())
    if size in sa.keys() and sa[size]>0:
        ammount+=pay
        sa[size]-=1

print(ammount)       
        
