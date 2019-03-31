# _*_ coding: utf-8 _*_

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import pymongo

__author__ = 'Silent_YangRun'
__date__ = '2019/3/20 7:59'


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
browser = webdriver.Chrome(options=options)

# 重要活动视频专辑
VIDEO_URL = 'https://www.xuexi.cn/a191dbc3067d516c3e2e17e2e08953d6/b87d700beee2c44826a9202c75d18c85.html'
ARTICLES_NAME_LIST = ['重要新闻', '综合新闻', '学习实践', '新闻发布厅', '中宣部发布', '学习时评', '新时代纪实',
                      '函电贺词', '指示批示', '出国访问', '重要文章', '重要讲话', '重要会议', '重要活动', '重要新闻']
ARTICLES_LINK_LIST = [
    # 重要新闻
    'https://www.xuexi.cn/98d5ae483720f701144e4dabf99a4a34/5957f69bffab66811b99940516ec8784.html',
    # 综合新闻
    'https://www.xuexi.cn/7097477a9643eacffe4cc101e4906fdb/9a3668c13f6e303932b5e0e100fc248b.html',
    # 学习实践
    'https://www.xuexi.cn/03c8b56d5bce4b3619a9d6c2dfb180ef/9a3668c13f6e303932b5e0e100fc248b.html',
    # 新闻发布厅
    'https://www.xuexi.cn/bab787a637b47d3e51166f6a0daeafdb/9a3668c13f6e303932b5e0e100fc248b.html',
    # 中宣部发布
    'https://www.xuexi.cn/105c2fa2843fa9e6d17440e172115c92/9a3668c13f6e303932b5e0e100fc248b.html',
    # 学习时评
    'https://www.xuexi.cn/d05cad69216e688d304bb91ef3aac4c6/9a3668c13f6e303932b5e0e100fc248b.html',
    # 新时代纪实
    'https://www.xuexi.cn/9ca612f28c9f86ad87d5daa34c588e00/9a3668c13f6e303932b5e0e100fc248b.html',
    # 函电贺词
    'https://www.xuexi.cn/13e9b085b05a257ed25359b0a7b869ff/9a3668c13f6e303932b5e0e100fc248b.html',
    # 指示批示
    'https://www.xuexi.cn/682fd2c2ee5b0fa149e0ff11f8f13cea/9a3668c13f6e303932b5e0e100fc248b.html',
    # 出国访问
    'https://www.xuexi.cn/2e5fc9557e56b14ececee0174deac67f/9a3668c13f6e303932b5e0e100fc248b.html',
    # 重要文章
    'https://www.xuexi.cn/6db80fbc0859e5c06b81fd5d6d618749/9a3668c13f6e303932b5e0e100fc248b.html',
    # 重要讲话
    'https://www.xuexi.cn/588a4707f9db9606d832e51bfb3cea3b/9a3668c13f6e303932b5e0e100fc248b.html',
    # 重要会议
    'https://www.xuexi.cn/89acb6d339cd09d5aaf0c2697b6a3278/9a3668c13f6e303932b5e0e100fc248b.html',
    # 重要活动
    'https://www.xuexi.cn/c06bf4acc7eef6ef0a560328938b5771/9a3668c13f6e303932b5e0e100fc248b.html',
    # 重要新闻
    'https://www.xuexi.cn/98d5ae483720f701144e4dabf99a4a34/5957f69bffab66811b99940516ec8784.html'

]

client = pymongo.MongoClient(host='localhost', port=27017)
db = client['learn_xi']
articles_col = db['article_data']
videos_col = db['video_data']


def get_all_videos_data(video_link):
    browser.get(video_link)
    # 获取最终页码
    page_numbers = int(browser.find_element_by_xpath("//*[@id='Cbihw8wtupvk00']/div/ul/li[6]")
                       .get_attribute('innerText'))
    videos_data = list()
    for page_number in range(1, page_numbers + 1):
        browser.get(video_link + "?pageNumber=" + str(page_number))
        videos = browser.find_elements_by_xpath("//div[@id='Ck3ln2wlyg3k00']")
        videos_datetime = browser.find_elements_by_xpath("//div[@id='C7sa7nbl3hvs00']")
        for video_index, video in enumerate(videos):
            video_data = dict()
            video_data['title'] = videos[video_index].get_attribute('innerText')
            video_data['datetime'] = videos_datetime[video_index].get_attribute('innerText').split(' ')[0]
            video.click()
            browser.switch_to.window(browser.window_handles[-1])
            browser.get(browser.current_url)
            # 获取链接
            video_data['link'] = browser.current_url
            time.sleep(1)
            # 获取视频时长
            video_duration_str = browser.find_element_by_xpath("//span[@class='duration']").get_attribute('innerText')
            video_data['video_duration'] = int(video_duration_str.split(':')[0]) * 60 + int(
                video_duration_str.split(':')[1])
            browser.close()
            browser.switch_to.window(browser.window_handles[0])
            video_data['isWatch'] = False
            exists = videos_col.find({'link': video_data['link']})
            if exists.count() < 1:
                videos_col.insert_one(video_data)
            else:
                return 0
            videos_data.append(video_data)
        print("爬取了视频列表的第" + str(page_number) + "页")
    return videos_data.__len__()


def get_all_articles_data(articles_link, articles_name):
    browser.get(articles_link)
    try:
        page_numbers = browser.find_element_by_xpath("//*[@id='Cbihw8wtupvk00']/div/ul/li[6]")
    except NoSuchElementException as e:
        page_numbers = browser.find_element_by_xpath("//*[@id='Cbihw8wtupvk00']/div/ul/li[5]")
    page_numbers = page_numbers.get_attribute('innerText')
    articles_data = list()
    for page in range(1, int(page_numbers) + 1):
        browser.get(articles_link + "?pageNumber=" + str(page))
        titles = browser.find_elements_by_xpath("//div[@id='Ca4gvo4bwg7400']")
        datetime = browser.find_elements_by_xpath("//div[@id='Ceqj4drwadtc00']")
        for index, article in enumerate(titles):
            article_data = dict()
            article_data['title'] = titles[index].get_attribute("innerText")
            article_data['datetime'] = datetime[index].get_attribute('innerText')
            article.click()
            all_handles = browser.window_handles
            browser.switch_to.window(all_handles[-1])
            article_data['link'] = browser.current_url
            article_data['is_read'] = False
            browser.close()
            browser.switch_to.window(all_handles[0])
            exists = articles_col.find({'link': article_data['link']})
            if exists.count() < 1:
                articles_col.insert_one(article_data)
            else:
                return 0
            articles_data.append(article_data)

        print("爬取了《" + articles_name + "》列表的第" + str(page) + "页")
    return articles_data.__len__()


if __name__ == "__main__":
    new_video_num = 0
    new_article_num = 0
    # 获取所有文章数
    for article_index, article_link in enumerate(ARTICLES_LINK_LIST):
        new_article_num += get_all_articles_data(article_link, ARTICLES_NAME_LIST[article_index])
    # 获取部分视频数
    new_video_num += get_all_videos_data(VIDEO_URL)

    print("获取新文章数：" + str(new_article_num) + "，现有未读文章数：" +
          str(articles_col.find({'is_read': False}).count()))
    print("\n获取新视频数：" + str(new_video_num) + "，现有未观看视频数：" +
          str(videos_col.find({'isWatch': False}).count()))
    browser.quit()
