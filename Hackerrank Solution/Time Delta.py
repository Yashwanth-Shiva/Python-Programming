from datetime import datetime

def time_delta(t1, t2):
    t1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    return str(int(abs((t1-t2).total_seconds())))
n=int(input())
for i in range(n):
    s1=input()
    s2=input()
    res=time_delta(s1,s2)
    print(res)
