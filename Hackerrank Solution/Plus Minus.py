a=int(input())
arr=list(map(int,input().split()))
p=n=z=0
for i in arr:
    if i<0:
        n+=1
    elif i>0:
        p+=1
    else:
        z+=1
print('%.6f'%(p/a))
print('%.6f'%(n/a))
print('%.6f'%(z/a))
