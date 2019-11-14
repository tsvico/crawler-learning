# encoding: utf-8
import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
value = {"username":"admin","password":"123456"}
data = urllib.parse.urlencode(value)
url = "http://host712244607.s316.pppf.com.cn/admin/login.php?type=login"
request = urllib.request.Request(url,data)
response = urllib.request.urlopen(request)
print(data)
print(response.read())