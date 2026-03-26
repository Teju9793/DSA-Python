import re

s = input()
v = "aeiou"
c = "bcdfghjklmnpqrstvwxyz"

pattern = r'(?<=[%s])([%s]{2,})(?=[%s])' % (c, v, c)

matches = re.findall(pattern, s, flags=re.IGNORECASE)

if matches:
    for i in matches:
        print(i)
else:
    print(-1)
