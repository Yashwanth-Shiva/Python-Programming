from itertools import permutations
A=input().split()
list1=sorted(list(A[0]))
i=(int(A[1]))
list2=list(permutations(list1,i))
for i in list2:
    print("".join(i))
