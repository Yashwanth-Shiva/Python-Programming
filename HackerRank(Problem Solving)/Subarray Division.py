def birthday(s, d, m):
    count=0
    for i in range(0,len(s)):
        if sum(s[i:i+(m)])==d:
            count+=1
    print(count)

n=int(input())
s=list(map(int, input().split()))
d,m=map(int, input().split())
birthday(s, d, m)
