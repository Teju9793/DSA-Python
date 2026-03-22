a = input().strip()
r = sorted(a, key=lambda x: (
    not x.islower(),
    not x.isupper(),
    x.isdigit() and int(x) % 2 == 0, 
    x.isdigit() and int(x) % 2 != 0,   
    x
))
print(''.join(r))
