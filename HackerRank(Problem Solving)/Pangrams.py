def pangrams(s):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in alpha:
        if i not in s.lower():
            return "not pangram"
    return "pangram"

s = input()
print(pangrams(s))
