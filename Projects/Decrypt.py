"""
Decrypting msg which is encoded by corresponding 1 alphabet to another alphabet
Ex: if a corresponds to p then b corresponds to q, c corresponds to r and so on
"""
s="abcdefghijklmnopqrstuvwxyz"
s1=s
mystr="iyvaopzpzrpukvmdvyrpun"
for a in range(25):
    s1=s1[1:]+s1[0]
    print("s1 =",s1)
    for i in mystr:
        x=s.index(i)
        print(s1[x],end="")
    print()
