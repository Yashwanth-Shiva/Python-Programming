def timeConversion(n):
    s=n.split(":")
    if s[0]=="12" and n[-2]=="A":
        print("00"+":"+s[1]+":"+s[2][0]+s[2][1])
    elif n[-2]=="A":
        print(s[0]+":"+s[1]+":"+s[2][0]+s[2][1])
    elif s[0]=="12":
        print("12"+":"+s[1]+":"+s[2][0]+s[2][1])
    else:
        print(str(int(s[0])+12)+":"+s[1]+":"+s[2][0]+s[2][1])
          
n=input()
timeConversion(n)

#Method 2
def timeConversion(n):
    s=n[0:-2]
    s=s.split(":")
    if s[0]=="12" and n[-2]=="A":
        s[0]="00"
    elif s[0]!="12" and n[-2]=="P":
        s[0]=str(int(s[0])+12)
    print((":").join(s))
    
          
n=input()
timeConversion(n)
