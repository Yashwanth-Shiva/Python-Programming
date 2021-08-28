a=list(map(int,input().split()))
a.sort()
s1=s2=0
for i in range(4):
    s1=s1+a[i]
a.reverse()
for i in range(4):
    s2=s2+a[i]
print(s1, s2)
