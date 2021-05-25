n=int(input())
marks=input().split()
marks=[int(i) for i in marks]
print(sorted(set(marks))[-2])
