import urllib
import json

surl="http://py4e-data.dr-chuck.net/json?"
api_key = 42

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url=surl+urllib.parse.urlencode({"address":address,"key":42})

    
    print("Retrieving",url)
    uh=urllib.request.urlopen(url)
    data=uh.read().decode()
    print("Retrieved",len(data),"characters")
    print(data)
    
    try:
        js=json.loads(data)
    except:
        js=None
    
    if not js or "status" not in js or js["status"]!="OK":
      print("Data retrivial failed")
      print(data)
      continue
    
    #print(json.dumps(js, indent=4))
    
    place_id=js["results"][0]["place_id"]
    print(place_id)
    
