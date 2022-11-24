def happyLadybugs(b):
    l = list(b)
    if "_" not in l:
        if len(l) == 1:
            return "NO"
        if l[0] != l[1] or l[-1] != l[-2]:
            return "NO"
        for i in range(1, len(l)-1):
            if l[i] != l[i-1] and l[i] != l[i+1]:
                return "NO"
        else:
            return "YES"
        
    for i in set(b):
        if i != "_" and b.count(i) < 2:
            return "NO"
    return "YES"
    
test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    b = input()
    print(happyLadybugs(b))
