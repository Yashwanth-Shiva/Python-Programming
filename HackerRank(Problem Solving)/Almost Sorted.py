def almostSorted(n,arr):
    temp=arr.copy()
    res=arr.copy()
    res.sort()
    count=0
    for i in range(n):
        try:
            if temp[count]==res[count]:
                temp.pop(count)
                res.pop(count)
            else:
                count+=1
        except:
            pass
    if len(temp)==0:
        print("yes")
    else:
        if len(temp)==2 and temp[::-1]==res:
            print("yes\nswap",arr.index(temp[0])+1,arr.index(temp[-1])+1)
        elif temp[::-1]==res:
            print("yes\nreverse",arr.index(temp[0])+1,arr.index(temp[-1])+1)
        else:
            print("no")
    
n=int(input())
arr=list(map(int,input().split()))
res=almostSorted(n,arr)
