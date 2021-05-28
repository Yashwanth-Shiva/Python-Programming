#maximum number
num_list=[]
num_list=input("Enter the numbers:").split(",")
num_list=[int(i) for i in num_list]
max1=None
for i in num_list:
    if max1== None or i>max1:
        max1=i
print(max1)
  

#other method
print(max(num_list))