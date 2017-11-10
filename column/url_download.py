# -*- coding: utf-8 -*-
from urllib import urlencode
import json
import requests
import time



def get_index(max_behot_time,headers):
    data = {
        'category': '组图',
        'utm_source': 'toutiao',
        'max_behot_time':max_behot_time,
        'as': 'A1E5D9FFCBEEDBD',
        'cp': '59FBFE6DBB5D3E1'
    }
    params = urlencode(data)
    url = 'https://www.toutiao.com/api/pc/feed/?' + params
    print url
    time.sleep(2)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.text)
        if data and 'data' in data.keys():
            for item in data.get('data'):
                link = 'http://www.toutiao.com' + item.get('source_url')
                with open('url.txt','a+') as f:
                    text_url = f.readlines()
                    if link not in text_url:
                        f.write(link+ '\n')
                        f.close()

        max_behot_time1 = data['next']['max_behot_time']
        print max_behot_time1
        get_index(max_behot_time1,headers)


