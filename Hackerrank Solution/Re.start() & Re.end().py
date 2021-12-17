import re
s=input()
k=input()
regex=re.compile(k)
r=regex.search(s)
if not r:
    print("(-1, -1)")
while r:
    print("("+str(r.start())+", "+str(r.end()-1)+")")
    r=regex.search(s,r.start()+1)
