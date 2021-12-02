def countingValleys(steps, path):
    count=0
    x=0
    for i in path:
        if i=="U":
            x+=1
        elif i=="D":
            x-=1
        if x==0 and i=="U":
            count+=1
    return count

steps=int(input())
path=input()
res=countingValleys(steps, path)
print(res)
