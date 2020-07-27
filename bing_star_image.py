# coding=utf-8

import os
import time
from icrawler import ImageDownloader
from icrawler.builtin import BingImageCrawler
from pypinyin import lazy_pinyin

group = ''
global_name = ''


class PrefixNameDownloader(ImageDownloader):
    def get_filename(self, task, default_ext):
        return global_name + '-' + group + '.' + default_ext


path = r'D:/code_py/face_base_spider/BingImage'
files = [
    'male_mainland', 'male_hongkong', 'male_taiwan', 'male_japan',
    'male_korea', 'female_mainland', 'female_hongkong', 'female_taiwan',
    'female_japan', 'female_korea'
]
group = files[4]
f = open(files[4] + '.txt', mode='r', encoding='UTF-8')
lines = f.readlines()
for i, line in enumerate(lines):
    name = line.strip('\n')
    global_name = ''.join(lazy_pinyin(name))
    # file_path = os.path.join(path, name)
    # if not os.path.exists(file_path):
    #     os.makedirs(file_path)
    # bing_storage = {'root_dir': file_path}
    bing_storage = {'root_dir': path}
    bing_crawler = BingImageCrawler(downloader_cls=PrefixNameDownloader,
                                    parser_threads=2,
                                    downloader_threads=4,
                                    storage=bing_storage)
    bing_crawler.crawl(keyword=name, max_num=1)
    print('第{}位明星：{}'.format(i, name))