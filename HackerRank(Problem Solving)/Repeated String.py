def repeatedString(s, n):
  #count of a in strings repeated except the last repetition
    x1=s.count("a") * (n // len(s))
  #count of a in the last repetition
    x2=s[:n%len(s)].count("a")
    return  x1+x2

s=input()
n=int(input())
res=repeatedString(s, n)
print(res)
