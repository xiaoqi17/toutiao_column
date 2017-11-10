# -*- coding: utf-8 -*-

import requests
import time
from bs4 import BeautifulSoup

def url_txt():
    with open('url.txt') as f:
        urls = f.readlines()
        for url in urls:
            yield url

def text_html(url,headers):
    time.sleep(0.1)
    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding
    if response.status_code == 200:
        soup = BeautifulSoup(response.text)
        result = soup.select('title')
        title = result[0].get_text() if result else ''
        print title



