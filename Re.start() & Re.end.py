import re

s = input()
ss = input()

found = False

for m in re.finditer(f'(?={ss})', s):
    print((m.start(), m.start() + len(ss) - 1))
    found = True

if not found:
    print((-1, -1))
