

def count_substring(string, sub_string):
    c=0
    l=len(string)
    m=len(sub_string)
    for i in range (0,l+1):
        if string[i:i+m]==sub_string:
            c+=1
     
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
