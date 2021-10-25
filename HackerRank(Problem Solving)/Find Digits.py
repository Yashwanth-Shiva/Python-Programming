def findDigits(n):
    a=[int(i) for i in n]
    c=0
    for i in a:
        try:
            if int(n)%i==0:
                c+=1
        except:
            pass
    return c

t=int(input())
for i in range(t):
    n=input()
    res=findDigits(n)
    print(res)
