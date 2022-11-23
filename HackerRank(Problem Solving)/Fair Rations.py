def fairRations(B):
    loaves_count = 0
    for i in range(len(B)-1):
        if B[i]%2 != 0:
            B[i] += 1
            B[i+1] += 1
            loaves_count += 2
    if(B[-1]%2 != 0):
        return 'NO'
    return str(loaves_count)
            

n = int(input())
B = list(map(int, input().split()))
print(fairRations(B))
