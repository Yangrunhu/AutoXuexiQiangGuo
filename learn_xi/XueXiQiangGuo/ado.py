# _*_ coding: utf-8 _*_

import pymongo


__author__ = 'Silent_YangRun'
__date__ = '2019/3/20 7:47'


client = pymongo.MongoClient(host='localhost', port=27017)
db = client['learn_xi01']
articles_col = db['article_data']
videos_col = db['video_data']


def create(col, data):
    """增"""
    return col.insert_one(data)


def read(col, query):
    """查"""
    return col.find(query)


def update(col, query, new_values):
    """改"""
    return col.update(query, {"$set": new_values})


def update_many(col, query, new_values):
    """改"""
    return col.update_many(query, {"$set": new_values})


def delete(col, query):
    return col.delete_one(query)


def check():
    article_query = {'is_read': True}
    article_query2 = {'is_read': False}
    print("已阅读文章总数为：" + str(read(articles_col, query=article_query).count()))
    print("\n未阅读文章总数为：" + str(read(articles_col, query=article_query2).count()))

    video_query = {'isWatch': True}
    video_query2 = {'isWatch': False}
    print("\n已观看视频总数为：" + str(read(videos_col, query=video_query).count()))
    print("\n未观看视频总数为：" + str(read(videos_col, query=video_query2).count()))


def test():
    article_query = {"is_read": True}
    article_new_value = {'is_read': False}
    update_many(articles_col, article_query, article_new_value)
    video_query = {"isWatch": True}
    video_new_value = {'isWatch': False}
    update_many(videos_col, video_query, video_new_value)


test()
check()
