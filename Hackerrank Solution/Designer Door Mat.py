m,n=map(int,input().split())
list1=[]
for i in range(1,(m//2)+1):
   list1.append(".|."*(2*i-1))
#print(list1)
for i in list1:
    print("".join(i).center(n).replace(" ","-"))
print("WELCOME".center(n).replace(" ","-"))
for i in list1[::-1]:
    print("".join(i).center(n).replace(" ","-"))
