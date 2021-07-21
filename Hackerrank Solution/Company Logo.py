s=input()
list1=list(s)
dict1=dict()
dict2=dict()
for i in list1:
    dict1[i]=dict1.get(i,0)+1
#First sorting it in alphabetical order and then based on occurence
dict2=dict(sorted(dict1.items(), key=lambda item: item[0]))
x=tuple(sorted(dict2.items(), key=lambda item: item[1],reverse=True))
for i in range(3):
    print(x[i][0],x[i][1])
