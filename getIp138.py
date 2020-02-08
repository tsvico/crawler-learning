#获取ip的信息
#使用BeautifulSoup
import requests
from bs4 import BeautifulSoup #BeautifulSoup4库

url = 'http://ip138.com/'
html=requests.get(url,allow_redirects=False)
text = html.text.encode(html.encoding).decode('gb2312')
#print(text)#获取的网页文本
soup = BeautifulSoup(text, features='lxml')  #把html以lxml的方式解析加载进beautifulsoup,然后soup中有着html的所有信息
iframe_div = soup.select('.mod-ip > iframe')
print(iframe_div[0]['src'])
