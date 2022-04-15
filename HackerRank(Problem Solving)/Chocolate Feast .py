def chocolateFeast(n, c, m):
    NoOfChoco=n//c
    NoOfWraps=NoOfChoco
    while(NoOfWraps>=m):
        NewChoc=NoOfWraps//m
        NoOfChoco+=NewChoc
        NoOfWraps=NewChoc+NoOfWraps%m
    return NoOfChoco

t = int(input().strip())
for t_itr in range(t):
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    c = int(first_multiple_input[1])
    m = int(first_multiple_input[2])
    result = chocolateFeast(n, c, m)
    print(str(result))
