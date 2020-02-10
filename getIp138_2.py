#获取ip的信息
# 使用Xpath()
import requests
from lxml import etree
url = 'http://ip138.com/'
result = requests.get(url,allow_redirects=False)
text = result.text.encode(result.encoding).decode('gb2312')
html = etree.HTML(text)
html_data = html.xpath('//iframe/@src')
for i in html_data:
    print(i)
    res = requests.get(i,allow_redirects=False)
    dhtml = etree.HTML(res.text)
    dhtml_data = dhtml.xpath('/html/body/p[1]')
    # 打印提取到的结果
    for item in dhtml_data:
        print(item.text)