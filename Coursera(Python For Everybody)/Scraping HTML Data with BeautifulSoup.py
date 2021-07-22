import urllib
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input("Enter : ")
html=urllib.request.urlopen(url, context=ctx).read()
soup=BeautifulSoup(html, "html.parser")

count=0
sum=0
tags=soup("span")
for tag in tags:
    #print ('TAG:',tag)
    #print ('URL:',tag.get('href', None))
    #print ('Contents:',tag.contents[0])
    #print ('Attrs:',tag.attrs)
    sum+=int(tag.contents[0])
    count+=1
print(count)
print(sum)
