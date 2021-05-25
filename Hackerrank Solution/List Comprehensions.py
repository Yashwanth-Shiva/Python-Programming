x = int(input())
y = int(input())
z = int(input())
n = int(input())
list1=[]
list2=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if(i+j+k!=n):
                list1=[i,j,k]
                list2.append(list1)
print(list2)
