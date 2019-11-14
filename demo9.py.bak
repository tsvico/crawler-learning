#encoding: utf-8
import urllib2
from bs4 import BeautifulSoup
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
##请求模块
def request(url):
    heades = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        'Referer':'http://www.mzitu.com',
    }
    req = urllib2.Request(url,headers=heades)
    html = urllib2.urlopen(req)
    return html
#下载图片
def download(max_span):
    for page in range(1,int(max_span)+1):  #如果list空了只要十页图片
        page_url = href + '/' +str(page)  #专辑编号加上页码
        print(page_url) #图片页面地址 会报错

        img_html = request(page_url)

        img_soup = BeautifulSoup(img_html,"lxml")
        #img_url = img_soup.find('div',class_='main-image').find('img')['src']
        img_url = img_soup.find('img',alt = title)
        if img_url is None:
            continue
        else:
            img_url = img_url['src']
        ##print(img_url)
        name = img_url[-9:-4]##取URL 倒数第四至第九位 做图片的名字
        img = request(img_url)
        f = open(name+'.jpg','ab')#写入多媒体文件必须要b这个参数
        f.write(img.read())
        f.close()

path = "/home/gwj/snap/demo/images/"
all_url = 'http://www.mzitu.com/all' ##开始的ｕｒｌ
start_html = request(all_url)
#print(start_html.read())

soup = BeautifulSoup(start_html,"lxml") #使用BeautifulSoup来解析我们获取到的网页（‘lxml’是指定的解析器
all_a = soup.find('div',class_ ='all').find_all('a')##意思是先查找 class为 all 的div标签，然后查找所有的<a>标签
for a in all_a:
    title = a.get_text() ##取出a标签的文本
    if (title!=''):
        print ("爬取"+title)
        if(os.path.exists(path+title.strip().replace('?',''))):
            print "目录已存在"
        else:
            os.makedirs(path+title.strip().replace('?','')) ##创建存放文件夹
        os.chdir(path + title.strip().replace('?','')) ##切换到上述文件夹


        href = a['href']     ##取出a标签的href属性
    # #print(title)
        print(href)
        if href.find("old") != -1:
          continue

        html = request(href)
        html_soup = BeautifulSoup(html,"lxml")
        list = html_soup.find_all('span')

        #关键，不判断容易报错停止
        if len(list):
            max_span = html_soup.find_all('span')[10].get_text()#＃取出所有<span>标签，获取第十个中文本，就是最好一个页面
        else:
            max_span='10'
        print(max_span)
        #for page in range(1,int(max_span)+1):
        download(max_span)