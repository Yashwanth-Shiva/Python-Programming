mport urllib
import xml.etree.ElementTree as ET

fn=urllib.request.urlopen(" http://py4e-data.dr-chuck.net/comments_1239024.xml")
fh=fn.read()
s=0

tree=ET.fromstring(fh)
for i in tree.findall(".//count"):
    x=int(i.text)
    s=s+x
print(s)
