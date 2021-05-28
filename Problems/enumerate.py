list1=[]
list2=[]
dict1={}
for ix,i in enumerate("Yashwanth S"):
    print((ix,i))
    list1.append(i)
print("list1=",list1)
str1="i am a good boy.i am in bangalore.i am very obedient."
str1=str1.replace(".", " ")   
words=str1.lower().split()
unq=set(words)
for i in unq:
    dict1[i]=words.count(i)
print(dict1)
    