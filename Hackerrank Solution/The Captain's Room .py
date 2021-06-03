n=int(input())
list1=list(map(int,input().split()))
set1=set()
set2=set()
for i in list1:
    if i in set1:
        set2.add(i)
    else:
        set1.add(i)
x=set1.difference(set2)
print(list(x)[0])
