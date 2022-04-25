d={}
for i in range(int(input())):
    s=input()
    d[s]=d.get(s,0)+1
print(len(d))
print(" ".join([str(i) for i in d.values()]))
