# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=int(input())
for i in range(n):
    s=input()
    while(" && " in s or " || " in s):
        s=re.sub(" && "," and ",s)
        s=re.sub(" \|\| "," or ",s)
    print(s)
