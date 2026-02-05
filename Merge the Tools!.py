def merge_the_tools(string, k):
    l=len(string)
    for i in range(0,l,k):
        a=string[i:i+k]
        b=list(set(list(a)))
        x="".join(b)
        print(x)
  
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
