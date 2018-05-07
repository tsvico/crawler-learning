# encoding: utf-8
#有header
import urllib
import urllib2
mm = raw_input("input music :")
value = {"input":mm,
         "filter":"name",
         "type":"netease",
         "page":"1"}
X = 'XMLHttpRequest'
header = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
          'X-Requested-With':X
          }
url = "http://host712244607.s316.pppf.com.cn/yy/index.php"
data = urllib.urlencode(value)
request = urllib2.Request(url,data,header)
#异常处理
try:
    response = urllib2.urlopen(request)
except urllib2.URLError,e:
    print e.code
    print e.reason
print data
print response.read()