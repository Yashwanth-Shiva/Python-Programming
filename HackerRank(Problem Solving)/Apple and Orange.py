s,t=map(int,input().split())
a,b=map(int,input().split())
m,n=map(int,input().split())
m1=list(map(int,input().split()))
n1=list(map(int,input().split()))

c1=0
c2=0
for i in m1:
    x1=a+i
    if x1 in range(s,t+1):
        c1+=1
for j in n1:
    x2=b+j
    if x2 in range(s,t+1):
        c2+=1
print(c1)
print(c2)
