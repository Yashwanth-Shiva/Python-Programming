import re
def Regcheck(s):
    if re.match('[+-]?[0-9]*[.][0-9]+$',s):
        return "True"
    return "False"
    
n=int(input())
for i in range(n):
    s=input()
    res=Regcheck(s)
    print(res)
