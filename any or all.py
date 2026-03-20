n=int(input())
l=list(map(int,input().split()))
r=all(i>0for i in l) and any(str(i) == str(i)[::-1]for i in l)
print(r)
