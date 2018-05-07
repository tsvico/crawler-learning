# -*- coding: utf-8 -*-
import urllib2
import os
import sys
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf8')
url = 'http://www.mzitu.com'
#头
heade = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    'Referer':'http://www.mzitu.com',
}

request = urllib2.Request(url,headers=heade)
#########
#get方式提交的另一种方法
#request.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36')
#request.add_header('Referer','http://www.mzitu.com/')
######
respons = urllib2.urlopen(request)
path = "/home/gwj/snap/demo/image/"
#print respons.read()


#解析
#使用自带的html.parser解析，速度慢但通用,这里用ｌｘｍｌ解析器
soup = BeautifulSoup(respons.read(),"lxml")
print soup.a
#最大页数在span标签中的第１0个
page = soup.find_all('a',class_ = 'page-numbers')
max_page = page[-2].text


same_url = 'http://www.mzitu.com/page/'
for n in range(1,int(max_page)+1):
    ul = same_url+str(n)
    request1 = urllib2.Request(ul,headers=heade)
    start_html = urllib2.urlopen(request1)
    soup = BeautifulSoup(start_html,"lxml")
    #实际上时第一个class = 'postlist'的div里的所有a标签
    all_a = soup.find('div',class_ ='postlist').find_all('a',target='_blank')
    #提取用户名
    for a in all_a:
        title = a.get_text() #提取文本
        if(title!=''):
            print ("准备爬取:"+title)
            if(os.path.exists(path+title.strip().replace('?',''))):
                print("目录已存在")
                flag=1
            else:
                os.makedirs(path+title.strip().replace('?',''))
                flag=0
            os.chdir(path + title.strip().replace('?',''))
            href = a['href']
            request2 = urllib2.Request(href,headers=heade)
            html = urllib2.urlopen(request2)
            mess = BeautifulSoup(html,"lxml")
            pic_max = mess.find_all('span')
            pic_max = pic_max[10].text #最大页数
            if(flag == 1 and len(os.listdir(path+title.strip().replace('?',''))) >= int(pic_max)):
                print('已经保存完毕，跳过')
                continue
            for num in range(1,int(pic_max)+1):
                pic = href+'/'+str(num)
                request = urllib2.Request(pic,headers=heade)
                html = urllib2.urlopen(request)
                mess = BeautifulSoup(html,"lxml")
                pic_url = mess.find('img',alt = title)
                if pic_url!="":
                    request = urllib2.Request(pic_url['src'],headers=heade)
                else:
                    continue
                html = urllib2.urlopen(request)
                file_name = pic_url['src'].split(r'/')[-1]
                f = open(file_name,'wb')
                f.write(html.read())
                f.close()
            print "完成"
        print "第",n,"页完成"