def beautifulDays(i, j, k):
    c=0
    for x in range(i,j+1):
        y=str(x)
        y=int(y[::-1])
        if (abs(x-y)/k).is_integer():
            c+=1
    return c
    
i,j,k=map(int, input().split())
res=beautifulDays(i, j, k)
print(res)
