# -*- coding: utf-8 -*-
import os
import re
import pymongo
import requests
import time
from bs4 import BeautifulSoup
from hashlib import md5
from flask import json

client = pymongo.MongoClient('localhost', 27017)
ceshi = client['toutiao']
item_info = ceshi['toutiao_imger']


def download_image(url):
    print('Downloading', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            save_image(response.content)
            return None
    except:
        return None


def save_image(content):
    file_path = '{0}/{1}.{2}'.format(os.getcwd(), md5(content).hexdigest(), 'jpg')
    print(file_path)
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(content)
            f.close()

def url_txt():
    with open('url.txt') as f:
        urls = f.readlines()
        for url in urls:
            yield url


def text_html(url,headers):
    time.sleep(1)
    if item_info.find_one({'url': url}):
        print '%s爬过' % url
    else:
        response = requests.get(url,headers=headers)
        text = response.text
        soup = BeautifulSoup(text, 'lxml')
        result = soup.select('title')
        title = result[0].get_text() if result else ''
        images_pattern = re.compile('var gallery = (.*?);', re.S)
        result = re.search(images_pattern, text)
        if result:
            data = json.loads(result.group(1))
            if data and 'sub_images' in data.keys():
                sub_images = data.get('sub_images')
                images = [item.get('url') for item in sub_images]
                for image in images: download_image(image)
                return {
                    'title': title,
                    'url': url,
                    'images': images
                    }

def save_to_mongo(result):
    if item_info.insert(result):
        print('Successfully Saved to Mongo', result)
        return True
    return False
