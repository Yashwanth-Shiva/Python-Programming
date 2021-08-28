n=int(input())
arr=[]
s1=s2=x=0
for i in range(n):
    arr.append(list(map(int,input().split())))
for i in range(n):
    s1=s1+arr[i][i]
for i in range(n-1,-1,-1):
    s2=s2+arr[x][i]
    x+=1
print(abs(s1-s2))
