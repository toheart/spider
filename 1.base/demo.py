import urllib2
response = urllib2.urlopen('http://www.zhihu.com')

html = response.read()
print(html)
