if __name__ == '__main__':
    list=[]
    n = int(input())
    for i in range(n):
        ip=input().split()
        cmd=ip[0]
        
        if cmd == "insert":
            list.insert(int(ip[1]),int(ip[2]))
        elif cmd=="print":
            print(list)
        elif cmd=="remove":
            list.remove(int(ip[1]))
        elif cmd == "append":
            list.append(int(ip[1]))
        elif cmd == "sort":
            list.sort()
        elif cmd == "pop":
            list.pop()
        else:
            list.reverse()
            
