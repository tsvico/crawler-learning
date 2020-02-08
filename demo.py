####
#最简单的请求
####
import requests
url = "http://www.baidu.com"
request = requests.get(url)
print(request.text)