setA=set(map(int,input().split()))
n=int(input())
count=0
for i in range(n):
    setB=set(map(int,input().split()))
    if setA.issuperset(setB):
        count+=1
print(count==n)
