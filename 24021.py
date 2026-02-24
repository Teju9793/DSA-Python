from collections import OrderedDict
a=int(input())
dic=OrderedDict()
for i in range(a):
    data =input().split()
    q=int(data[-1])
    item= " ".join(data[:-1])
    if item in dic:
        dic[item]+=q
    else:
        dic[item]=q
for key ,vlaue in dic.items():
    print(key,vlaue)
    
