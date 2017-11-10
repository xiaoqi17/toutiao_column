# -*- coding: utf-8 -*-


from Queue import Queue
import random
import threading
import time
import url_download
import html_download

headers = {
            'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cache - Control': 'max - age = 0',
            'Connection': 'keep-alive',
            'Content - Type': 'application / x - www - form - urlencoded',
            'Cookie': 'tt_webid = 6484032377030034957',
            'Host': 'www.toutiao.com',
            'Referer': 'https://www.toutiao.com/ch/news_image/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
            'X - Requested - With': 'XMLHttpRequest'
        }

class Url_Download(threading.Thread):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.data = queue

    def run(self):
        time.sleep(2)
        max_behot_time = 0
        url_download.get_index(max_behot_time, headers)



class Html_Downlad(threading.Thread):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.data = queue

    def run(self):
        time.sleep(0.1)
        for url in html_download.url_txt():
            html_download.text_html(url, headers)


if __name__ == '__main__':
    queue = Queue()
    p = Url_Download('Url' + str(1), queue)
    c = Html_Downlad('Html' + str(5), queue)
    p.start()
    c.start()