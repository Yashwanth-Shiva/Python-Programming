from collections import Counter
x=int(input())
size=list(map(int,input().split()))
size=Counter(size)
n=int(input())
cost=0
for i in range(n):
    a,b=map(int,input().split())
    if size[a]:
        cost+=b
        size[a]-=1
print(cost)

#without using collections
x=int(input())
size=list(map(int,input().split()))
n=int(input())
list1=[]
for i in range(n):
    a,b=map(int,input().split())
    if a in size:
        list1.append(b)
        size.remove(a)
print(sum(list1))
