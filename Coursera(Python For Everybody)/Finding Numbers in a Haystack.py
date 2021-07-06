#In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers. 
import re
fn=input("Enter file name:")
list1=[]
sum=0
fh=open(fn)
for line in fh:
    y=re.findall("[0-9]+",line)
    list1.extend(y)
for i in list1:
    sum=sum+int(i)
print(sum)
