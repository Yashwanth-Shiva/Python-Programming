def stones(n, a, b):
    l = []
    if a==b:
        return [(n-1)*(a)]
    for i in range(n):
        last_stone = i*b+(n-1-i)*a
        l.append(last_stone)
    l.sort()
    return l


test_cases = int(input())
for i in range(test_cases):
    n = int(input())
    a = int(input())
    b = int(input())
    res = stones(n, a, b)
    print(' '.join(map(str, res)))
