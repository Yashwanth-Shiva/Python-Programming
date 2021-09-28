def getMoneySpent(keyboards, drives, b):
    cost=-1
    for i in keyboards:
        for j in drives:
            if (i+j<=b and i+j>cost):
                cost=i+j
    return cost

b,n,m=map(int, input().split())
keyboards=list(map(int, input().split()))
drives=list(map(int, input().split()))
res=getMoneySpent(keyboards, drives, b)
print(res)
