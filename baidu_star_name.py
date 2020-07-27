# coding=utf-8

import os
import time
import json
import requests


class Query:
    def __init__(self, stat0, stat1, file_name):
        self.stat0 = stat0
        self.stat1 = stat1
        self.file_name = file_name


def getManyPages(pages, query):
    print(query.stat0 + ',' + query.stat1)
    params = []
    for i in range(0, 12 * pages + 12, 12):
        params.append({
            'resource_id': 28266,
            'from_mid': 1,
            'format': 'json',
            'ie': 'utf-8',
            'oe': 'utf-8',
            'query': '明星',
            'sort_key': '',
            'sort_type': 1,
            'stat0': query.stat0,
            'stat1': query.stat1,
            'stat2': '',
            'stat3': '',
            'pn': i,
            'rn': 12
        })
    url = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php'
    #    names = []
    #    img_results = []
    x = 0
    f = open(query.file_name, mode='w', encoding='UTF-8')
    for param in params:
        try:
            res = requests.get(url, params=param)
            js = json.loads(res.text)
            results = js.get('data')[0].get('result')
        except AttributeError as e:
            print(e)
            break
        for result in results:
            img_name = result['ename']
            #            img_url = result['pic_4n_78']
            #            img_result =  [img_name,img_url]
            #            img_results.append(img_result)
            f.write(img_name + '\n')
    #        names.append(img_name)

        if x % 10 == 0:
            print('第%d页......' % x)
        x += 1
        # time.sleep(0.1)
    f.close()


if __name__ == '__main__':
    L = []
    L.append(Query('男', '内地', 'male_mainland.txt'))
    L.append(Query('男', '香港', 'male_hongkong.txt'))
    L.append(Query('男', '台湾', 'male_taiwan.txt'))
    L.append(Query('男', '日本', 'male_japan.txt'))
    L.append(Query('男', '韩国', 'male_korea.txt'))
    L.append(Query('女', '内地', 'female_mainland.txt'))
    L.append(Query('女', '香港', 'female_hongkong.txt'))
    L.append(Query('女', '台湾', 'female_taiwan.txt'))
    L.append(Query('女', '日本', 'female_japan.txt'))
    L.append(Query('女', '韩国', 'female_korea.txt'))
    for l in L:
        getManyPages(400, l)
