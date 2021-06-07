#using function
def even_odd(x):
    if x%4==0:
        print(x,"is a multiple of 4")
    else:
        print(x,"is not a multiple of 4")
n=int(input("Enter any number:"))
even_odd(n)


#using return
def even_odd(x):
    if x%4==0:
        return True
    else:
        return False
n=int(input("Enter any number:"))
z=even_odd(n)
"""
If the numbr is odd the function returns z becomes True
else z becomes false.
In the same way u can also return value
"""
if z:
    print(n,"is a multiple of 4")
else:
    print(n,"is not a multiple of 4")
