def serviceLane(width, cases):
    lst=[]
    for i in cases:
        lst.append(min(width[i[0]:i[1]+1]))
    return lst

n,t=map(int,input().split())
width=list(map(int,input().split()))
cases=[]
for _ in range(t):
    cases.append(list(map(int,input().split())))
res=serviceLane(width,cases)
print(*res,sep="\n")
