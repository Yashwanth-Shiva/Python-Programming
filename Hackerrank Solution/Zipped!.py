n, x = map(int, input().split()) 
list1 = []
for _ in range(x):
    list1.append( map(float, input().split()) )
for i in (zip(*list1)):
    print (sum(i)/x)
