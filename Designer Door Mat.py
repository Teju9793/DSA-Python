n,m=map(int,input().split())

for i in range(1,n,2):
    p=".|."*i
    print(p.center(m,"-"))
print("WELCOME".center(m,"-"))
for i in range(n-2,0,-2):
     p=".|."*i
     print(p.center(m,"-"))
