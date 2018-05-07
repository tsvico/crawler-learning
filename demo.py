import urllib2
request = urllib2.Request("http://www.baidu.com")
respons=urllib2.urlopen(request)
print respons.read()