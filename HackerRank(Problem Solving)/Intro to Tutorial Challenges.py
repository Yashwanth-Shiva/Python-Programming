def introTutorial(V, arr):
    return arr.index(V)

V = int(input())
n = int(input())
arr = list(map(int, input().split()))
print(introTutorial(V, arr))
