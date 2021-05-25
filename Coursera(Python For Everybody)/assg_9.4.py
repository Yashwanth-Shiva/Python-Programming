#Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. #
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.



fname = input("Enter file name: ")
fh = open(fname)
m_list=[]
for line in fh:
    line=line.split()
    if len(line)<3 or line[0]!="From":
        continue
    m_list.append(line[1])
mail_count=dict()
for i in m_list:
    mail_count[i]=mail_count.get(i,0)+1
c=None
w=None
for k,v in mail_count.items():
    if c==None or v>c:
        c=v
        w=k
print(w,c)
