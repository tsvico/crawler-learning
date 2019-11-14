import urllib.request, urllib.error, urllib.parse
request = urllib.request.Request("http://www.baidu.com")
respons=urllib.request.urlopen(request)
print(respons.read())