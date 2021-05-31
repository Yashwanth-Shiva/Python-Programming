n1=int(input())
myset1=set(map(int,input().split()))
n2=int(input())
myset2=set(map(int,input().split()))

#union - intersection gives the difference elements
list1=myset1.union(myset2) - myset1.intersection(myset2)

for i in sorted(list(list1)):
    print(i)
