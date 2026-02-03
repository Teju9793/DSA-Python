def print_rangoli(size):
    s=[chr(i) for i in range(97,123)]
    n=size
    l=s[n-1:0:-1]+s[0:n]
    m=len(" ".join(l))
    for i in range(1,n):
        print(("-".join(s[n-1:n-i:-1]+s[n-i:n])).center(m,"-"))
    print(("-".join(s[n-1:0:-1]+s[0:n])).center(m,"-"))
    for i in range(n-1,0,-1):
        print(("-".join(s[n-1:n-i:-1]+s[n-i:n])).center(m,"-"))

    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
