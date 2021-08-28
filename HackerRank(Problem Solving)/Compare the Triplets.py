l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
c1=c2=0
for i in range(len(l1)):
    if l1[i]>l2[i]:
        c1+=1
    elif l1[i]<l2[i]:
        c2+=1
print(c1, c2)
