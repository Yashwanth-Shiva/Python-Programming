def viralAdvertising(n):
    p=5
    c=s=0
    for i in range(n):
       c=p//2
       s+=c
       p=c*3
    return s
n=int(input())
res = viralAdvertising(n)
print(res)
