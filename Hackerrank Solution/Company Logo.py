s=input()
list1=sorted(list(s))
dict1=dict()
for i in list1:
    dict1[i]=dict1.get(i,0)+1
x=tuple(sorted(dict1.items(), key=lambda item: item[1],reverse=True))
for i in range(3):
    print(x[i][0],x[i][1])
