def angryProfessor(k, a):
    c=0
    for i in a:
        if i<=0:
            c+=1
    if c>=k:
        return "NO"
    else:
        return "YES"

t=int(input())
for i in range(t):
    n,k=map(int, input().split())
    a=list(map(int, input().split()))
    res=angryProfessor(k, a)
    print(res)
