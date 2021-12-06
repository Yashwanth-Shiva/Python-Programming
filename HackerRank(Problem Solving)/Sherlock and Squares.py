import math
def squares(a, b):
    count=0
    x=int(math.sqrt(a))
    while x**2<=b:
        if x**2 in range(a,b+1):
            count+=1
        x+=1
    return count

q=int(input())
for i in range(q):
    a,b=map(int, input().split())
    res=squares(a,b)
    print(res)
