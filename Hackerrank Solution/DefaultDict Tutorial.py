from collections import defaultdict
n,m=map(int,input().split())
ln=defaultdict(list)
for i in range(1,n+1):
    ln[input()].append(i)
for i in range(m):
    x=input()
    if x in ln:
        print(" ".join(map(str,ln[x])))
    else:
        print("-1")
        
        
#without using defaultdict
n,m=map(int,input().split())
ln=[]
lm=[]
for i in range(n):
    ln.append(input())
for i in range(m):
    x=input()
    if x in ln:
        for ind,val in enumerate(ln):
            if val==x:
                print(ind+1,end=" ")
        print()
    else:
        print("-1")
