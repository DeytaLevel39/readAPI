import urllib.request, json
url = "http://127.0.0.1:8000/"
fp = urllib.request.urlopen(url)
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

parsed = json.loads(mystr)
print(json.dumps(parsed,indent=4))
