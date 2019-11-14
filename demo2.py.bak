# encoding: utf-8
import urllib
import urllib2
value = {"username":"admin","password":"123456"}
data = urllib.urlencode(value)
url = "http://host712244607.s316.pppf.com.cn/admin/login.php?type=login"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print data
print response.read()