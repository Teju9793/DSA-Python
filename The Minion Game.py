def minion_game(string):
    l=len(string)
    k=0
    s=0
    v=list(("aeiou").upper())
    for i in range(l):
        if string[i] in v:
            k+=l-i
        else:
            s+=l-i
    if k>s:
        print("Kevin",k)
    elif s>k:
        print("Stuart",s)
    else:
        print("Draw")
        
       
  
    
if __name__ == '__main__':
    s = input()
    minion_game(s)
