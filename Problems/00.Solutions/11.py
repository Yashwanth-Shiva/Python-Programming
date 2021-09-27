list1=[]
list2=[]
n1=int(input("Enter elements in list 1:"))
print("Enter elements of list 1:")
for i in range(n1):
    list1.append(input())
n2=int(input("Enter elements in list 2:"))
print("Enter elements of list 2:")
for i in range(n2):
    list2.append(input())
"""
If u want to add list 2 as a seperate element use append
If u want to combine both the lists into a single list use extend
"""
list1.extend(list2)
print(list1)
