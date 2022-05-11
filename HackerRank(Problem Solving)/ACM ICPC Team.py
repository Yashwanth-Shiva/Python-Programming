def acmTeam(topic):
    count_1=0
    m=0
    d={}
    for i in range(len(topic)-1):
        for j in range(i+1,len(topic)):
            """converting to decimal and performing BIWISE OR operation and 
            conveting it back to binary"""
            x=str(bin(int(topic[i],2)|int(topic[j],2)))[2:]
            if x.count("1")>count_1:
                count_1=x.count("1")
                m=1
            elif x.count("1")==count_1:
                m+=1
    return(count_1,m)
        
            
    
topic=[]
n,m=map(int,input().split())
for i in range(n):
    topic.append(input())
res=acmTeam(topic)
print(res[0],res[1],sep="\n")
