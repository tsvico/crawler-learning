#coding=utf-8
import urllib2
import urllib
from bs4 import BeautifulSoup
url = 'http://www.mzitu.com'
#头
heade = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}
data = urllib.urlencode('')
request = urllib2.Request(url,data,heade)
respons = urllib2.urlopen(request)
#print respons.read()
#解析
#使用自带的html.parser解析，速度慢但通用,这里用ｌｘｍｌ解析器
soup = BeautifulSoup(respons.read(),"lxml")
print soup.a
#实际上时第一个class = 'postlist'的div里的所有a标签
all_a = soup.find('div',class_ ='postlist').find_all('a',target='_blank')

for a in all_a:
    title = a.get_text() #提取文本
    print title