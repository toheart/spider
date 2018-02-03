import urllib2 
try:
    response = urllib2.urlopen('http://www.google.com')
    print(response)
except urllib2.HTTPError as e:
    if hasattr(e, 'code'):
        print("ERror code:", e.code)
