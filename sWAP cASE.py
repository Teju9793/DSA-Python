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
