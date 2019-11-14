#encoding: utf-8
#######
#
#从文件获取Cookie
#
######
import http.cookiejar
import urllib.request, urllib.error, urllib.parse

#创建ＭozillaCookieJar实例对象
cookie = http.cookiejar.MozillaCookieJar()
#从文件中读取Ｃｏｏｋｉｅ信息到变量
cookie.load('cookie.txt',ignore_expires=True,ignore_discard=True)
#创建请求的request
req = urllib.request.Request("http://www.baidu.com")
#利用urllib2的ｂuild_opener方法创建一个ｏｐｅｎｅｒ
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
response = opener.open(req)
print(response.read())