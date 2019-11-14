#encoding: utf-8
#######
#
#获取Cookie保存到文件
#
######
import cookielib
import urllib2

#设置保存cookie的文件
filenme = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filenme)
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handle = urllib2.HTTPCookieProcessor(cookie)
#通过handle来构建opener
opener = urllib2.build_opener(handle)
#此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open('http://www.baidu.com')
#保存cookie到文件
cookie.save(ignore_discard=True,ignore_expires=True)
#关于最后save方法的两个参数在此说明一下：
#官方解释如下：
#ignore_discard: save even cookies set to be discarded.
#ignore_expires: save even cookies that have expiredThe file is overwritten if it already exists
#由此可见，ignore_discard的意思是即使cookies将被丢弃也将它保存下来，
#ignore_expires的意思是如果在该文件中 cookies已经存在，则覆盖原文件写入，
#在这里，我们将这两个全部设置为True。运行之后，cookies将被保存到cookie.txt文件中
#

