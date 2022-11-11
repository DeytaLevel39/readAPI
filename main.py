import urllib.request, json
format="json"
type=""
url = "http://127.0.0.1:8000/"+type+"?format="+format
fp = urllib.request.urlopen(url)
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

if format=="json":
    parsed = json.loads(mystr)
    print(json.dumps(parsed,indent=4))
else:
    print(mystr)
