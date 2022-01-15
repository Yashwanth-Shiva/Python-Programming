def nonDivisibleSubset(k, l1):
    l1=[i%k for i in l1]
    #print(l1)
    l2=[]
    temp=set(l1)
    count=0
    if k==1:
        return 1
    for i in temp:
        if i not in l2:
            if i==0 or (k-i)==i:
                count+=1
                l2.append(i)
                l2.append(k-i)
                continue
            if k-i in l1:
                if l1.count(i)>=l1.count(k-i):
                    count+=l1.count(i)
                else:
                    count+=l1.count(k-i)
            else:
                count+=l1.count(i) 
        l2.append(i)
        l2.append(k-i)  
    return(count)
                    
        

n,k=map(int,input().split())
l1=list(map(int,input().split()))
res=nonDivisibleSubset(k, l1)
print(res)
