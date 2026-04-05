import re
import email.utils

n = int(input())

for _ in range(n):
    line = input()
    
    name, email = email.utils.parseaddr(line)
    
    # regex for valid email
    if re.fullmatch(r'[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}', email):
        print(email.utils.formataddr((name, email)))
