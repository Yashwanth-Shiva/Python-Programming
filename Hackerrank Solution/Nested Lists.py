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
