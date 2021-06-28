from itertools import combinations_with_replacement
A=input().split()
list1=sorted(list(A[0]))
list2=[]
x=(int(A[1]))
list2.extend(list(combinations_with_replacement(list1,x)))
for j in list2:
    print("".join(j))
