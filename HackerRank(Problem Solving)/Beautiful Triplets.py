def beautifulTriplets(d, arr):
    beautiful=0
    for i in arr:
        if d+i in arr[arr.index(i)+1:]:
            if 2*(d+i)-i in arr[arr.index(d+i)+1:]:
                beautiful+=1
    return beautiful

n,d=map(int,input().split())
arr=list(map(int,input().split()))
res=beautifulTriplets(d, arr)
print(res)
