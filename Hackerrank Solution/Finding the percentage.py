mark_list=dict()
n=int(input())
for i in range(n):
    name,m1,m2,m3=input().split()
    m1=float(m1)
    m2=float(m2)
    m3=float(m3)
    list1=[m1,m2,m3]
    mark_list[name]=list1
name1=input()
for i in mark_list:
    if(i==name1):
     avg=sum(mark_list[i])/3
print("{0:.2f}".format(avg))
