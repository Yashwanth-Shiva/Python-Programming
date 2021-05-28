#print even numbers
x=input("Enter the first number:")
x=int(x)
y=input("Enter the last number:")
y=int(y)
while(x<=y):
    if(x%2==0):
        print(x,end=",")
    x+=1