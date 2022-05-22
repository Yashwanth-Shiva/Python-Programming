def workbook(n, k, arr):
    special=0
    page=1
    for prob in arr:
        for pg in range(1,prob+1):
            if pg==page:
                special+=1
            if pg%k==0:
                page+=1
        if pg%k!=0:
            page+=1
    return special
    
    
n,k=map(int,input().split())
arr=list(map(int,input().split()))
res=workbook(n,k,arr)
print(res)
