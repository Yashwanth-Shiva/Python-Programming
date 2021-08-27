n=int(input())
marks1=[]
for i in range(n):
    marks1.append(input())
for x in marks1:
    x=int(x)
    if x<38:
        x=x
    elif x%5>2:
        if x%5==3:
            x=x+2
        else:
            x=x+1
    print(x)
