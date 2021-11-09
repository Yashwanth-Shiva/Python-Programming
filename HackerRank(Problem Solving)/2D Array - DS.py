def hourglassSum(arr):
    s=-9999
    for i in range(4):
        for j in range(4):
            x=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            if x>s:
                s=x
    return s

arr=[]
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))
result = hourglassSum(arr)
print(result)
