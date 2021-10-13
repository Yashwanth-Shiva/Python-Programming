def hurdleRace(k, height):
    x=max(height)
    if x<k:
        return 0
    else:
        return(x-k)
    
n,k=map(int, input().split())
height=list(map(int, input().split()))
res=hurdleRace(k, height)
print(res)
