#encoding: utf-8
#######
#
#利用cookie模拟网站登录(不能有验证码）
#
######
import urllib2
import urllib
import cookielib

filename = 'cookie.txt'
#声明一个ＭozillCookieJar对象实例来保存ｃｏｏｋｉｅ，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
value = {'username':'sdssasad','password':'hello'}
postdata = urllib.urlencode(value)
#登录教务系统的URL
loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login'
#模拟登录，并把cookie保存到变量
result = opener.open(loginUrl,postdata)
#保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
#利用cookie请求访问另一个网址，此网址是成绩查询网址
gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
#请求访问成绩查询网址
result = opener.open(gradeUrl)
print result.read()