n,k,q=map(int, input().split())
a=list(map(int, input().split()))
k=k%n
a=a[-k:]+a[0:-k]
for i in range(q):
    queries=int(input())
    print(a[queries])
