def permutationEquation(p):
    for i in range(1,n+1):
        x=p.index(i)
        print((p.index(x+1))+1)

n=int(input())
p=list(map(int, input().split()))
permutationEquation(p)
