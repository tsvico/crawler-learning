#获取ip的信息
# 使用Xpath()
import requests
from lxml import etree
url = 'http://ip138.com/'
html=requests.get(url,allow_redirects=False)
text = html.text.encode(html.encoding).decode('gb2312')
html = etree.HTML(text)
html_data = html.xpath('//iframe/@src')
for i in html_data:
    print(i)
