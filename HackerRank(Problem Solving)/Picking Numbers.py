def pickingNumbers(a):
    l1=[]
    l2=[]
    x=0
    for i in sorted(a):
        for j in sorted(a):
            if j==i or j==i-1: 
                l1.append(j)
            if j==i or j==i+1: 
                l2.append(j)
        if len(l1)>x or len(l2)>x:
            x=max(len(l1),len(l2))
        l1=[]
        l2=[]
    return x
  
n=int(input())
a=list(map(int, input().split()))
res=pickingNumbers(a)
print(res)

#Method 2

"""
def pickingNumbers(a):
    x=y=z=0
    for i in sorted(a):
        x=a.count(i)
        y=a.count(i-1)
        if (x+y)>z:
            z=x+y
    return z
    """
