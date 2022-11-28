def hackerrankInString(s):
    str1 = "hackerrank"
    idx = 0
    for i in range(len(s)):
        if s[i] == str1[idx]:
            idx += 1
            if idx == len(str1):
                return "YES"
    return "NO"

test_cases = int(input())
for _ in range(test_cases):
    print(hackerrankInString(input()))
