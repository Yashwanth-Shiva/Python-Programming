def designerPdfViewer(h, word):
    alpha="abcdefghijklmnopqrstuvwxyz"
    l=[]
    for i in word.lower():
       x=alpha.find(i)
       l.append(h[x])
    n=max(l)
    return (n*len(word))
    

h=list(map(int, input().split()))
word=input()
res=designerPdfViewer(h, word)
print(res)
