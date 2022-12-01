def caesarCipher(s, k):
    s_alpha = "abcdefghijklmnopqrstuvwxyz"
    b_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    for i in s:
        if i in s_alpha:
            res += s_alpha[(s_alpha.index(i)+k)%26]
        elif i in b_alpha:
            res += b_alpha[(b_alpha.index(i)+k)%26]
        else:
            res += i
    return res

n = int(input())
s = input()
k = int(input())
print(caesarCipher(s, k))
