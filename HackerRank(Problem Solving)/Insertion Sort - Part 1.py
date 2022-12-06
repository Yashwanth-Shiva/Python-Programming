def insertionSort1(n, arr):
    num = arr[-1]
    for i in range(n-2, -1, -1):
        if num < arr[i]:
            arr[i+1] = arr[i]
            if i==0:
                print_arr(arr)
                arr[i] = num
                print_arr(arr)
                break
        else:
            arr[i+1] = num
            print_arr(arr)
            break
        print_arr(arr)
 
def print_arr(arr):
    for i in arr:
        print(i, end=" ")    
    print()
                

n = int(input())
arr = list(map(int, input().split()))
insertionSort1(n, arr)
