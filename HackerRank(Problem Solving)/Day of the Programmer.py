def dayOfProgrammer(year):
    if year<1918:
        if year%4==0:
            date=12
        else:
            date=13
    elif year>1918:
        if (year%400==0 or year%4==0 and year%100!=0):
            date=12
        else:
            date=13
    elif year==1918:
        date=26
    return(str(date)+".09."+str(year))

year=int(input())
r=dayOfProgrammer(year)
print(r)
