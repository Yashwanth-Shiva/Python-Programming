def kangaroo(x1, v1, x2, v2):
    if (x2>x1 and v2>=v1):
        return "NO"
    else:
        if ((x1-x2)%(v2-v1))==0: #or ((x1-x2)/(v2-v1)).is_integer()
                return "YES"
        return "NO"
    
x1,v1,x2,v2=map(int, input().split())
result=kangaroo(x1, v1, x2, v2)
print(result)
