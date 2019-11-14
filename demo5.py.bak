#encoding: utf-8
#######
#
#从文件获取Cookie
#
######
import cookielib
import urllib2

#创建ＭozillaCookieJar实例对象
cookie = cookielib.MozillaCookieJar()
#从文件中读取Ｃｏｏｋｉｅ信息到变量
cookie.load('cookie.txt',ignore_expires=True,ignore_discard=True)
#创建请求的request
req = urllib2.Request("http://www.baidu.com")
#利用urllib2的ｂuild_opener方法创建一个ｏｐｅｎｅｒ
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
print response.read()