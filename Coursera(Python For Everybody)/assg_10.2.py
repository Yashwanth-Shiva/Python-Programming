"""
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""


fn=input("Enter file name:")
fh=open(fn)
date_list=[]
for line in fh:
    line=line.split()
    if(len(line)<6 or line[0]!="From"):
        continue
    list1=line[5].split(":")
    date_list.append(list1[0])
#print(date_list)

dict1=dict()
for i in date_list:
    dict1[i]=dict1.get(i,0)+1
tup=[]
for k,v in dict1.items():
    tup.append((k,v))

for i,j in sorted(tup):
    print(i,j)
