def alnum(S):
    for i in S:
        if i.isalnum():
            return True
    return False
def alpha(S):
    for i in S:
        if i.isalpha():
            return True
    return False
def digit(S):
    for i in S:
        if i.isdigit():
            return True
    return False
def lower(S):
    for i in S:
        if i.islower():
            return True
    return False
def upper(S):
    for i in S:
        if i.isupper():
            return True
    return False
S=input()
print(alnum(S))
print(alpha(S))
print(digit(S))
print(lower(S))
print(upper(S))
