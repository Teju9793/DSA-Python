from collections import deque
a=deque()
x=int(input())
for i in range(x):
    data=input().split()
    p=data[0]
    if p=="append":
        a.append(data[1])
    elif p=="appendleft":
        a.appendleft(data[1])
    elif p=="pop":
        a.pop()
    elif p=="popleft":
        a.popleft()
print(*a)
