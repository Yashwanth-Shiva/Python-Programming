# Enter your code here. Read input from STDIN. Print output to STDOUT
x=int(input())
s=set(map(int, input().split()))
n=int(input())
for i in range(n):
    cmd,x=input().split()
    getattr(s,cmd)(set(map(int,input().split())))
print(sum(s))
