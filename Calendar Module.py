import calendar
m,d,y = map(int,input().split())
da=list(calendar.day_name)
i = calendar.weekday(y,m,d)
print(da[i].upper())
