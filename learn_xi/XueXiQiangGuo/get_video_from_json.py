# _*_ coding: utf-8 _*_

import json
import pymongo

__author__ = 'Silent_YangRun'
__date__ = '2019/3/25 11:06'

client = pymongo.MongoClient(host='localhost', port=27017)
db = client['learn_xi']
articles_col = db['article_data']
videos_col = db['video_data']

video_data = {
    "link": '',
    "video_duration": 0,
    'datetime': '',
    'isWatch': False,
    'title': ''
}

category = ['["习近平活动视频集"]', '["专题报道"]', '["学习新视界"]', '["十九大报告视频"]']

test_list = list()
file = open("C:/Users/Coder/Desktop/data/video.json", 'r', encoding='utf-8')
text = json.load(file)
for index in text['fp2t40yxso9xk0010']['list1']:
    print(index)
    if index["type"] == '':
        print(index['static_page_url'])


