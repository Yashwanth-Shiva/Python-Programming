def minimumNumber(n, password):
    return max(6-n, sum((
        0 if re.search('[0-9]', password) else 1,
        0 if re.search('[a-z]', password) else 1,
        0 if re.search('[A-Z]', password) else 1,
        0 if re.search('[@!#$%^&*()+-]', password) else 1
    )))
    
    

n = int(input())
password = input()
print(minimumNumber(n, password))
