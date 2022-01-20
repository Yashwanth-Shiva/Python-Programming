def taumBday(b, w, bc, wc, z):
  #calculating the total cost
    total_cost=b*bc+w*wc
    # if cost of black is same as white or if coversion cost z is more than cost of white and black, then there is no need for conversion
    #simply return the total cost
    if (bc==wc or z>=max(bc,wc)):
        return total_cost
    #if z< (bc and wc) and if wc!=bc
    #finding the color with low cost and converting them and returning the min(total_cost,coversion_cost)
    x=min(bc,wc)
    if x==bc:
        return min(total_cost,(b+w)*bc+w*z)
    else:
        return min(total_cost,(b+w)*wc+b*z)

for i in range(int(input())):
    b,w=map(int, input().split())
    bc,wc,z=map(int,input().split())
    res=taumBday(b, w, bc, wc, z)
    print(res)
