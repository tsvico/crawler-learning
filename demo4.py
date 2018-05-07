#encoding: utf-8
#######
#
#获取Cookie保存到变量
#
######
import urllib2
import cookielib
#声明一个CookieJar对象实例来保存Cookie
cookie = cookielib.CookieJar();
#利用urllib库的HTTPCookieProcessor对象来创建cookie处理器
handle = urllib2.HTTPCookieProcessor(cookie)
#通过handle来个构建opener
opener = urllib2.build_opener(handle)
#此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open('http://www.baidu.com')
for item in cookie:
    print 'Name = '+item.name
    print 'Value = '+item.value