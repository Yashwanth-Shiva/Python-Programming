from itertools import combinations
A=input().split()
list1=sorted(list(A[0]))
list2=[]
x=(int(A[1]))
for i in range(1,x+1):
    list2.extend(list(combinations(list1,i)))
for j in list2:
    print("".join(j))
