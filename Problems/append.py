#append and extend
list_1=[]
n1=int(input("Enter number of elements of list_1:"))
for i in range(0,n1):
    list_1.append(input(i))
list_2=[]
n2=int(input("Enter number of elements of list_2:"))
for i in range(0,n2):
    list_2.append(input(i))
print(list_1)
print(list_2)

op=int(input("Enter the option:\n1.Add list_2 as a seperate element\n2.Add elements of list_2 to list_1\n"))
if(op==1):
    list_1.append(list_2)
    print(list_1)
elif(op==2):
    list_1.extend(list_2)
print(list_1)
    
list1=[1,2,3,4]
list2=[5,6,7,8]
print(list1+list2)