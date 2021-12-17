import re
n=int(input())
for i in range(n):
    regex=input()
    try:
        x=re.compile(regex)
        print("True")
    except:
        print("False")
