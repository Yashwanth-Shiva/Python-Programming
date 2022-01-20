def kaprekarNumbers(p, q):
    c=0
    for i in range(p,q+1):
        if i==1:
            print(i,end=" ")
            c+=1
            continue
        sqr=str(i**2)
        x=sqr[0:len(sqr)//2]
        y=sqr[(len(sqr)//2):]
        try:
          if int(x)+int(y)==i:
            print(i,end=" ")
            c+=1
        except:
           pass
    if c==0:
        print("INVALID RANGE")       


p=int(input())
q=int(input())
kaprekarNumbers(p, q)
