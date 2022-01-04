list1=[]
list2=[]
max2=None
for _ in range(int(input())):
    name = input()
    score = float(input())
    list1=[name,score]
    list2.append(list1)
sec_high=sorted(set([score for name,score in list2]))[1]
print("\n".join(sorted([name for name,score in list2 if score==sec_high])))




l1=[]
l2=[]
for i in range(int(input())):
    name=input()
    score=float(input())
    l1=[name,score]
    l2.append(l1)
    
second_highest=sorted(list(set(score for name,score in l2)))[1]
for x,y in sorted(l2):
    if y==second_highest:
        print(x)
