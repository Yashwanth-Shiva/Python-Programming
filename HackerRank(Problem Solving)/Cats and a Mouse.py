def catAndMouse(x, y, z):
    A=abs(x-z)
    B=abs(y-z)
    if A<B:
        return ("Cat A")
    elif A>B:
        return ("Cat B")
    else:
        return ("Mouse C")
    
q=int(input())
for i in range(q):
    x,y,z=map(int, input().split())
    res=catAndMouse(x, y, z)
    print(res)
