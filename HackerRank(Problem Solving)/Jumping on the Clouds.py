def jumpingOnClouds(c):
    count=0
    k=0
    while k<=len(c)-1:
        #if index equals no. of elts then break
        if k==len(c)-1:
            break
        #if index+2 < no. of elts and c[index]!=1 then k=k+2 else k=k+1
        elif k+2<=len(c)-1 and c[k+2]!=1:
            k+=2
        else:
            k+=1
        count+=1
    return count
            
n=int(input())
c=list(map(int, input().split()))
res=jumpingOnClouds(c)
print(res)
