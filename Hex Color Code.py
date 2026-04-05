n=int(input())
il=False
for i in range(n):
    line=input()
    if "{" in line:
        il=True
        continue
    if "}" in line:
        il=False
        continue
    if il:
        p=r"#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?"
        matches=re.findall(p,line)
        for i in matches:
            print(i)
