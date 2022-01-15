def nonDivisibleSubset(k, l1):
    #finding the remainders
    #if (A+B)%k==0, then A%k+B%k==k
    l1=[i%k for i in l1]
    #print(l1)
    l2=[]
    temp=set(l1)
    count=0
    if k==1:
        return 1
    for i in temp:
        #l2 is a list to store all read elements i.e. A and it's pair B=(K-A) so that we don't repeat reading the same elements 
        #Example: A=3 K=5 then there is only one B=2 where A+B==K
        #Therefore if we read any one of A or B we can neglect the next A or B
        if i not in l2:
            #Ex: if A=5 B=15 A%k==0 B%k==0, then we take it's count only once bcoz if we take both A & B it's (5+15)%5==0 which is not required
            #Also if A=2  B=2 and K=4, then A+B is divisible by K. So we read it only once either A or B
            if i==0 or (k-i)==i:
                count+=1
                l2.append(i)
                l2.append(k-i)
                continue
            #if B in l1  
            if k-i in l1:
                #we take the count of max(count(A),count(B)) bcoz we require max length
                if l1.count(i)>=l1.count(k-i):
                    count+=l1.count(i)
                else:
                    count+=l1.count(k-i)
            #if B not in l1 then we can simply take count of all As, i,e A=3 in l1 and B=2 not in l1 (k=5)
            else:
                count+=l1.count(i) 
        l2.append(i)
        l2.append(k-i)  
    return(count)
                    
        

n,k=map(int,input().split())
l1=list(map(int,input().split()))
res=nonDivisibleSubset(k, l1)
print(res)
