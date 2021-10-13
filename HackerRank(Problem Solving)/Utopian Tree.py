def utopianTree(n):
    x=1
    for i in range(1,n+1):
        if (i==1 or i%2==0):
            x=x+1
        else:
            x=x*2
    return(x)

t=int(input())
for i in range(t):
    n=int(input())
    res=utopianTree(n)
    print(res)
