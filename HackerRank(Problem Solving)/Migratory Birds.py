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


#Method 2
def migratoryBirds(arr):
    c=n=0
    for i in set(arr):
        x=arr.count(i)
        if x>c:
            n=i
            c=x
    return n
        
n=int(input())
arr=list(map(int, input().split()))
res=migratoryBirds(arr)
print(res)
