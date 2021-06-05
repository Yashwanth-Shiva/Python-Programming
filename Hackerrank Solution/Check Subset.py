n=int(input())
setA=set()
for i in range(n):
    n1=int(input())
    setA=set(map(int,input().split()))
    n2=int(input())
    setB=set(map(int,input().split()))
    print(setA.issubset(setB))
