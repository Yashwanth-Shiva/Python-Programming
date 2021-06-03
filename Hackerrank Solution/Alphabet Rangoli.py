n=int(input())
mystr="abcdefghijklmnopqrstuvwxyz"[0:n]
list1=[]
list2=[]
z=0
k=n
#iterating mystring from backwords
for i in range(n,0,-1):
    """
    The below for loop for the 1st iteration gives 1st half of the middle line
    for example when size #3
           1st iteration gives c b a
           2nd iteration gives c b
           3rd iteration gives c
    """
    for j in range(0,k):
        print(mystr[n-1-j])
        list1.append(mystr[n-1-j])
    """
    The below for loop gives the 2nd half of the middle line
    for example for size #3 range becomes (0,2) as i am using k-1
          1st iteration gives  b c 
                                as i am using mystr[z+j(+1)]
          2nd iteration gives  c
    """
    for j in range(0,k-1):
        print(mystr[z+j+1])
        list1.append(mystr[z+j+1])
    """
    After completion of 1st iteration of both the for loops 
    list 1 contains c b a c b
    i am taking this into another list 2 as we can get each line seperately as 
    an element of list 2
    at last list2 contains:[['c', 'b', 'a', 'b', 'c'], ['c', 'b', 'c'], ['c']]
    """
    list2.append(list1)
    list1=[]
    k-=1
    z=z+1
""" 
Reversing the list and making it into a string using join and 
printing it in the centre by replacing " " by "-"
The 1st for loop gives :  ----c----
                          --c-b-c--
                          c-b-a-b-c  
The 2nd for loop gives :  --c-b-c--
                          ----c----
"""
for i in (list2[::-1]):
    print("-".join(i).center(4*n-3).replace(" ","-"))
for i in (list2[1:]):
    print("-".join(i).center(4*n-3).replace(" ","-"))
