import json
import urllib

fn=urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_1239025.json")
fh=fn.read()

data=json.loads(fh)
l1=data["comments"]
s=0
for i in l1:
    s=s+i["count"]
print(s)
