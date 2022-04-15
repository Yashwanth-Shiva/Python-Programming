def minimumDistances(a):
    m=10000
    for i in set(a):
        if a.count(i)>1:
            ind1=a.index(i)
            ind2=a.index(i,ind1+1)
            if ind2-ind1<m:
                m=ind2-ind1
    if m==10000:
        return -1
    else:
        return m

n = int(input().strip())
a = list(map(int, input().rstrip().split()))
result = minimumDistances(a)
print(str(result) + '\n')
