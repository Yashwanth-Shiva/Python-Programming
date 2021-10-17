t=int(input())
for i in range(t):
    n,m,s=map(int, input().split())
    x=(m+s-1)%n
    if x==0:
        print(n)
    else:
        print(x)
