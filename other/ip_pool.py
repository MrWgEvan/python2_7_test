# coding:utf8
import requests
from lxml.etree import HTML
from Queue import Queue
import time,re
from threading import Thread,currentThread
#from apscheduler.schedulers.blocking import BlockingScheduler

qe = Queue()

def kuaidaili(num):
    print('--------正在爬取快代理---------')
    url = 'https://www.kuaidaili.com/free/inha/{}/'
    for i in range(1,num+1):
        try:
            now_url = url.format(i)
            try:
                res = requests.get(now_url)
            except:
                break
            res = HTML(res.text)
            ip_list = res.xpath('//*[@id="list"]/table/tbody/tr/td[1]/text()')
            port_list = res.xpath('//*[@id="list"]/table/tbody/tr/td[2]/text()')
            result_list = zip(ip_list,port_list)
            time.sleep(1)
            i+=1
            # 拼接IP端口，加入队列
            # print(result_list)
            for r in result_list:
                item = ':'.join(r)
                qe.put(item)
                # print item
        except:
            continue
    print('--------爬取快代理完毕---------')
# kuaidaili()

def daili66(num):
    print('--------正在爬取代理66---------')
    url = 'http://www.66ip.cn/mo.php?sxb=&tqsl={}&port=&export=&ktip=&sxa=&submit=%CC%E1++%C8%A1&textarea='
    now_url = url.format(num)
    try:
        res = requests.get(now_url).text
        pattern = re.findall(r'\d+?\.\d+?\.\d+?\.\d+?:\d+',res)
        for item in pattern:
            qe.put(item)
    except:
        pass
    print('--------爬取代理66完毕---------')
# daili66(1000)

'''
def wuyoudaili():
    print('--------正在爬取无忧代理---------')
    url_list = [
        'http://www.data5u.com/free/gngn/index.shtml',
        'http://www.data5u.com/free/gnpt/index.shtml',
        'http://www.data5u.com/free/gwgn/index.shtml',
        'http://www.data5u.com/free/gwpt/index.shtml'
    ]

    headers = {
        'Cookie':'JSESSIONID=B43F2C56809E0B6B925B6833FEA419A8; UM_distinctid=161fa0e19af144-040042952b8af-3e3d5100-1fa400-161fa0e19b2692; CNZZDATA1260383977=1333230780-1520318210-null%7C1520318210; Hm_lvt_3406180e5d656c4789c6c08b08bf68c2=1520318684; Hm_lpvt_3406180e5d656c4789c6c08b08bf68c2=1520320412',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'
    }

    for url in url_list:
            try:
                response = requests.get(url,headers=headers).text
                response = HTML(response)
            except:
                continue
            ip_list = response.xpath('//div[@class="wlist"]/ul/li[2]/ul/span[1]/li/text()')[1:]
            port_list = response.xpath('//div[@class="wlist"]/ul/li[2]/ul/span[2]/li/text()')[1:]
            result_list = zip(ip_list,port_list)
            for item in result_list:
                proxy = ':'.join(item)
                qe.put(proxy)
    print('--------爬取无忧代理完毕---------')
# wuyoudaili()

'''
def xicidaili(num):
    print('--------正在爬取西刺代理---------')
    url_list = [
        'http://www.xicidaili.com/nn/{}',
        'http://www.xicidaili.com/nt/{}'
    ]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'
    }

    for url in url_list:
        for i in range(1,num+1):
            now_url = url.format(i)
            try:
                response = requests.get(now_url,headers=headers).text
                response = HTML(response)
                ip_list = response.xpath('//table[@id="ip_list"]//tr/td[2]/text()')
                port_list = response.xpath('//table[@id="ip_list"]//tr/td[3]/text()')
                result_list = zip(ip_list,port_list)
                for item in result_list:
                    proxy = ':'.join(item)
                    qe.put(proxy)
            except:
                continue
    print('--------爬取西刺代理完毕---------')
# xicidaili(2)


def check_ip():
    print '-----------{}开始检测--------'.format(currentThread().name)
    while True:
        try:
            ip = qe.get(timeout=20)
        except:
            break
        try:
            proxies = {"http": "http://{}".format(ip)}
            #r = requests.get('http://httpbin.org/ip', proxies=proxies, timeout=20, verify=False)
            r = requests.get('https://www.biquge5200.com', proxies=proxies, timeout=20)
            # print type(r.status_code)
            if r.status_code == 200:
                print(ip)
        except:
            pass
    print '-----------{}检测完毕--------'.format(currentThread().name)


def main():
    t1 = Thread(target=kuaidaili,args=(20,))
    t2 = Thread(target=daili66,args=(1000,))
   # t3 = Thread(target=wuyoudaili)
    t4 = Thread(target=xicidaili,args=(10,))
    t_list = []
    for i in range(10):
        t = Thread(target=check_ip)
        t.setDaemon(False)
        t_list.append(t)

    t1.setDaemon(False)
    t2.setDaemon(False)
    #t3.setDaemon(False)
    t4.setDaemon(False)


    t1.start()
    t2.start()
    #t3.start()
    t4.start()

    map(lambda x:x.start(),t_list)

    t4.join()
   # t3.join()
    t2.join()
    t1.join()
    map(lambda x:x.join(),t_list)

def run():
    print "~~~~~~~~~~~~~~~爬虫程序开始运行~~~~~~~~~~~~~~~"
    main()
   # sched = BlockingScheduler()
    # sched.add_job(main,'interval',minutes=30)
   # sched.start()
    print "~~~~~~~~~~~~~~~本次爬取结束~~~~~~~~~~~~~~~"

if __name__ == '__main__':
    run()
