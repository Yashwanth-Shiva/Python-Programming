import math

def encryption(s):
    l=[]
    res=[]
    s=s.replace(" ","")
    row=math.floor(math.sqrt(len(s)))
    col=math.ceil(math.sqrt(len(s)))
    for i in range(0,len(s),col):
        l.append(s[i:i+col])
    #chillprint(l)
    for i in range(row+1):
        s1=""
        for j in l:
            try:
                s1+=j[i]
            except:
                pass
        res.append(s1)
    return res
    
     
s=input()
result=encryption(s)
print(" ".join(result))
