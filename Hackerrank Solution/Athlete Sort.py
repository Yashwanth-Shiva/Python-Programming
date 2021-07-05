n, x = map(int, input().split()) 
list1 = []
for _ in range(n):
    list1.append(list(map(float, input().split())))
y=int(input())
#zipping the elements 
list2=(list(zip(*list1)))
#Accessing the elements in respective postion, sorting them and removing the duplicates
list3=set(sorted(list2[y]))
#Going back to the original list and printing the elements in the order obtained in list3
for i in list3:
    for k in list1:
            if i==k[y]:
                for j in k:
                    print(int(j),end=" ")
                print()
