# encoding: utf-8
#有header
import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
#mm = raw_input("输入参数1：")
value = {}#如果提交数据中需要传参，在这里填入
header = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
          'host':'www.baidu.com'}
#头中多个数据用','相隔
url = "http://www.baidu.com/"
data = urllib.parse.urlencode(value)
request = urllib.request.Request(url,data,header)
#异常处理
try:
    response = urllib.request.urlopen(request)
except urllib.error.URLError as e:
    print(e.code)
    print(e.reason)
print(data)
print(response.read())
