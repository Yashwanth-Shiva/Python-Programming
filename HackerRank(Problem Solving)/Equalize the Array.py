def equalizeArray(arr):
    m=0
    elt=0
    for i in set(arr):
        x=arr.count(i)
        if x>m:
            m=x
    return len(arr)-m

n=int(input())
arr=list(map(int, input().split()))
res=equalizeArray(arr)
print(res)
