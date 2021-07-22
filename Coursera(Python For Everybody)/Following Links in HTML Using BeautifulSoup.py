import re
import urllib
from bs4 import BeautifulSoup

url=input("Enter : ")
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html, "html.parser")

tags=soup("a")
p=0
c=1
while c<8:
    for tag in tags:
        p+=1
        if p==18:
            url=tag.get("href",None)
            html=urllib.request.urlopen(url).read()
            soup=BeautifulSoup(html, "html.parser")
            tags=soup("a")
            c+=1
            p=0
            break
print(url)
x=re.findall("by_([^.]*)",url)
print(x[0])
