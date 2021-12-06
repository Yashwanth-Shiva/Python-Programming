def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1>y2:
        return 10000
    elif y1<y2:
        return 0
    elif m1>m2:
        return (m1-m2)*500
    elif m1<m2:
        return 0
    elif d1>d2:
        return (d1-d2)*15
    else:
        return 0


d1,m1,y1=map(int, input().split())
d2,m2,y2=map(int, input().split())
res=libraryFine(d1, m1, y1, d2, m2, y2)
print(res)
