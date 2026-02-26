a = int(input())
for i in range(a):
    try:
        x,y=map(int,input().split())  
        print(x//y)
    except ZeroDivisionError as t:
        print("Error Code:",t)
    except ValueError as y:
        print("Error Code:",y)
