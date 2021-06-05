from collections import OrderedDict
n=int(input())
dict1={}
sum1=0
list1=[]
for i in range(n):
    list1=input().split()
    b=list1[-1]
    a=" ".join(list1[0:-1])
    dict1[a]=dict1.get(a,0)+int(b)
for x,y in dict1.items():
    print(x,y)
