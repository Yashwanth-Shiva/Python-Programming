def howManyGames(p, d, m, s):
    count=0
    while p>m and s>m:
        count+=1
        s-=p
        p-=d
    count+=s//m
    return count

first_multiple_input = input().rstrip().split()
p = int(first_multiple_input[0])
d = int(first_multiple_input[1])
m = int(first_multiple_input[2])
s = int(first_multiple_input[3])
answer = howManyGames(p, d, m, s)
print(str(answer) + '\n')
