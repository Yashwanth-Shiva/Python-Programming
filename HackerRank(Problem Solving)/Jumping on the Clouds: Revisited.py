def jumpingOnClouds(c, k):
    i=0
    e=100
    while True:
        i+=k
        e=e-1
        if c[i%n]==1:
            e=e-2
        if (i%n)==0:
            break
    return e

n,k=map(int, input().split())
c=list(map(int, input().split()))
res=jumpingOnClouds(c, k)
print(res)
