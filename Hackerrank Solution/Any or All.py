N=int(input())
list1=input().split()
print(all([int(i)>0 for i in list1]) and any([j==j[::-1] for j in list1]))
