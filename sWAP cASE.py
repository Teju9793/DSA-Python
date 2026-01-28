def swap_case(s):
    nl=""
    for l in s:
        if l.isupper():
            nl+=l.lower()
        elif l.islower():
            nl+=l.upper()
        else:
            nl+=l
            
    return nl

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)



    
             # Or 






    
    def swap_case(s):
    r=[]
    for l in s:
        if l.isupper():
            r.append(l.lower())   
        elif l.islower():
            r.append(l.upper())    
        else:
            r.append(l)
           
    return "".join(r)
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)



          # 0r

def swap_case(s):
     return s.swapecase()
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
