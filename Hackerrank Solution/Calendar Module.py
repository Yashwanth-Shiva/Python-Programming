import calendar
m,d,y=map(int,input().split())
n=(calendar.weekday(y,m,d))
print(calendar.day_name[n].upper())
