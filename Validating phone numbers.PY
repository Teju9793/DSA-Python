import re
n=int(input())
for i in range(n):
    ph=input()
    p=r"^[6789][0-9]{9}$"
    r=re.match(p,ph)
    if r:print("YES")
    else:print("NO")
