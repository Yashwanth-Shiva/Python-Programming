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
