def appendAndDelete(s, t, k):
    count=0
    while t[:len(s)]!=s:
        #print(t[:len(t)],s)
        if s=="":
            count+=len(t)
            if k<count:
              return "No"
            else:
              return "Yes"
        s=list(s)
        s.pop()
        s="".join(s)
        count+=1
    count+=len(t)-len(s)
    if count==k:
      return "Yes"
    elif count%2==1 and k%2==0 or count>k:
      return "No"
    else:
        return "Yes"

s = input()
t = input()
k = int(input().strip())
result = appendAndDelete(s, t, k)
print(result)
