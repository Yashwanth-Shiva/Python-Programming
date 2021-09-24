def bonAppetit(bill, k, b):
    Anna=(sum(bill)-bill[k])/2
    if Anna==b:
        print("Bon Appetit")
    else:
        print(int(b-Anna))
        
n,k=map(int, input().split())
bill=list(map(int, input().split()))
b=int(input())
bonAppetit(bill, k, b)
