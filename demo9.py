#encoding: utf-8
import urllib2
from bs4 import BeautifulSoup
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
heades = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    'Referer':'http://www.mzitu.com',
}
all_url = 'http://www.mzitu.com/all' ##开始的ｕｒｌ
request = urllib2.Request(all_url,headers=heades)
start_html = urllib2.urlopen(request)
#print(start_html.read())

soup = BeautifulSoup(start_html,"lxml") #使用BeautifulSoup来解析我们获取到的网页（‘lxml’是指定的解析器
all_a = soup.find('div',class_ ='all').find_all('a')##意思是先查找 class为 all 的div标签，然后查找所有的<a>标签
for a in all_a:
    title = a.get_text() ##取出a标签的文本

    path = str(title).strip().replace('?','') ##去掉空格
    print(path)
    os.makedirs(os.path.join('/home/gwj/snap/demo/images/',path)) ##创建存放文件夹
    os.chdir("/home/gwj/snap/demo/images/"+path) ##切换到上述文件夹


    href = a['href']     ##取出a标签的href属性
    # #print(title)
    print(href)
    if href.find("old") != -1:
        continue
    request1 = urllib2.Request(href,headers=heades)
    html = urllib2.urlopen(request1)
    html_soup = BeautifulSoup(html,"lxml")
    list = html_soup.find_all('span')

    #关键，不判断容易报错停止
    if len(list):
        max_span = html_soup.find_all('span')[10].get_text()#＃取出所有<span>标签，获取第十个中文本，就是最好一个页面
    else:
        max_span='10'
    print(max_span)
    #for page in range(1,int(max_span)+1):
    for page in range(1,int(max_span)+1):  #如果list空了只要十页图片
        page_url = href + '/' +str(page)  #专辑编号加上页码
        print(page_url) #图片页面地址 会报错
        request2 = urllib2.Request(page_url,headers=heades)
        img_html = urllib2.urlopen(request2)

        img_soup = BeautifulSoup(img_html,"lxml")
        #img_url = img_soup.find('div',class_='main-image').find('img')['src']
        img_url = img_soup.find('img',alt = title)
        if img_url is None:
            continue
        else:
            img_url = img_url['src']
        ##print(img_url)
        name = img_url[-9:-4]##取URL 倒数第四至第九位 做图片的名字
        request3 = urllib2.Request(img_url,heades=heades)
        img = urllib2.urlopen(request3)
        f = open(name+'.jpg','ab')#写入多媒体文件必须要b这个参数
        f.write(img.read())
        f.close()