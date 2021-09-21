def breakingRecords(scores):
    n1=n2=scores[0]
    mx=0
    mn=0
    for i in scores:
        if i>n1:
            mx+=1
            n1=i
        elif i<n2:
            mn+=1
            n2=i
    print(mx,mn)

n=int(input())
scores=list(map(int,input().split()))
result = breakingRecords(scores)
