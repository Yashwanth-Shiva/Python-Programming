for i in range(1,int(input())+1):
    print((10**i//9)**2)
"""
Example i=2
        (10**2//9)=11
        11**2=121
        i=3
        (10**3//9)=111
        111**2=12321
 similarly i=4
           10**4//8=1111
           1111**2=1234321
 """
        
#Other method but this is not accepted by Hackerrank
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    for k in range(i-1,0,-1):
        print(k,end="")
    print(end="\n")
