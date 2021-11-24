# Enter your code here. Read input from STDIN. Print output to STDOUT
def pileup(l):
    for i in range(len((l))-1):
        num=l.pop(0) if l[0]>l[-1] else l.pop(-1)
        if num<l[0] or num<l[-1]:
            return "No"
    return "Yes"

T=int(input())
for i in range(T):
   n=int(input())
   l=list(map(int, input().split()))
   res=pileup(l) 
   print(res)
