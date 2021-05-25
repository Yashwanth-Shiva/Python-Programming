n=int(input())
s=[]
sol=[]

for i in range(n):
    s.append(input().split())

for i in range(n):
    if(s[i][0]=="insert"):
        sol.insert(int(s[i][1]),int(s[i][2]))
    elif(s[i][0]=="append"):
        sol.append(int(s[i][1]))
    elif(s[i][0]=="remove"):
        sol.remove(int(s[i][1]))
    elif(s[i][0]=="print"):
        print(sol)
    elif(s[i][0]=="sort"):
        sol=sorted(sol)
    elif(s[i][0]=="pop"):
        sol.pop()
    elif(s[i][0]=="reverse"):
        sol.reverse()
