n,m=map(int,input().split())
sn=list(map(int,input().split()))
sA=set(map(int,input().split()))
sB=set(map(int,input().split()))
l1=[i for i in sn if i in sA]
l2=[i for i in sn if i in sB]
print(len(l1)-len(l2))
