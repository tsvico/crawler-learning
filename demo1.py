# encoding: utf-8
####
#有header
####
import requests
#mm = raw_input("输入参数1：")
header = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
          'host':'www.baidu.com'}
#头中多个数据用','相隔
url = "http://www.baidu.com/"
request = requests.get(url,headers=header)
print(request.text)
#打印响应头
print(request.headers)
#打印cookie
print(request.cookies)
