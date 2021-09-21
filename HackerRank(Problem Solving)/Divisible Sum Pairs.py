def divisibleSumPairs(n, k, ar):
    count=0
    x=1
    for i in ar:
        for j in ar[x:]:
            if (i+j)%k==0:
                count+=1
        x+=1
    print(count)

n,k=map(int, input().split())
ar=list(map(int, input().split()))
divisibleSumPairs(n, k, ar)
