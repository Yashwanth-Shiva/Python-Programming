def cutTheSticks(n,arr):
    while arr:
        ind=0
        lenOfCut=min(arr)
        print(len(arr))
        for i in range(len(arr)):
            x=arr[ind]-lenOfCut
            if x==0:
                arr.remove(arr[ind])
            else:
                arr[ind]=x
                ind+=1

n = int(input())
arr = list(map(int, input().split()))
res = cutTheSticks(n,arr)
