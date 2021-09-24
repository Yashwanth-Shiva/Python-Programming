n=int(input())
l1=list(map(int,input().split()))
d1={}
#sorting the array before getting the count of each number
for i in sorted(l1):
    d1[i]=d1.get(i,0)+1
l2=[]
#sorting dict by dict values 
for i in sorted(d1, key=d1.get, reverse=True):
  #collecting all the key values in the required order
    l2.append(i)
#printing first element which is our answer
print(l2[0])
