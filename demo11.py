#encoding: utf-8
#多线程版本
import requests
import threading
import urllib
import time
from bs4 import BeautifulSoup
PAGE_URL_LIST = []
#表情包链接列表
FACE_URL_LIST = []
#名字
FACE_NAME_LIST = []
BESE_PAGE_URL = "https://www.doutula.com/photo/list/?page="
for x in range(1,1500):
    url = BESE_PAGE_URL + str(x)
    PAGE_URL_LIST.append(url)

#初始化锁
gLock = threading.Lock()

#生产者，负责从每个页面中提取表情的url
class Producer(threading.Thread):
    def run(self):
        while len(PAGE_URL_LIST) > 0:

            #在访问PAGE_URL_LIST中要使用锁机制
            gLock.acquire()
            page_url = PAGE_URL_LIST.pop()
            #使用完把锁释放，方便其他线程使用
            gLock.release()
            #url请求
            response = requests.get(page_url)
            #使用返回的数据构建ｂｅｓｕ对象

            #requests对象中　response.content返回的是二进制的数值，
            # response.text返回的是Unicode型的数据
            # 也就是说，如果你想获取文本，可以通过.text
            # 如果你想获取图片，文件可以通过　.content
            soup = BeautifulSoup(response.content,'lxml')
            img_list = soup.find('div',class_ = 'page-content').find_all('img',class_ = 'img-responsive lazy image_dta')

            #加锁
            gLock.acquire()
            for img in img_list:
                title = img['alt']
                src = img['data-original']
                print(title)
                print(src)
                # 把提取到的表情url，添加到FACE_URL_LIST中
                FACE_URL_LIST.append(src)
                FACE_NAME_LIST.append(title)
            #释放
            gLock.release()
            time.sleep(0.5)


#消费者，负责从FACE_URL_LIST中提取链接，并下载
class Consumer(threading.Thread):
    def run(self):
        print '%s is runing' % threading.current_thread()
        while True:
            #上锁
            gLock.acquire()
            if len(FACE_URL_LIST)==0 or len(FACE_NAME_LIST)==0:
                #不管什么情况，先释放锁
                gLock.release()
                continue
            else:
                #提取数据
                face_url = FACE_URL_LIST.pop()
                filename = FACE_NAME_LIST.pop()
                gLock.release()
                z = face_url[-4:]  #后缀取名
                path = 'images2'+ '/' +filename.strip()+z
                urllib.urlretrieve(face_url,path)


if __name__=='__main__':
    #两个生产者线程
    for x in range(2):
        Producer().start()

    #５个消费者
    for x in range(5):
        Consumer().start()