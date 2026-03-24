i=input()
for j in range(len(i)-1):
    if i[j].isalnum() and i[j]==i[j+1]:
        print(i[j])
        break
else:
    print(-1)
