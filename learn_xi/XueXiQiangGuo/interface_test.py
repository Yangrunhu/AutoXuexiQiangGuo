# _*_ coding: utf-8 _*_

from selenium import webdriver
import time
import pymongo
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import json

__author__ = 'Silent_Coder'
__date__ = '2019/3/12 22:41'

HOME_PAGE = 'https://www.xuexi.cn/'
VIDEO_LINK = 'https://www.xuexi.cn/a191dbc3067d516c3e2e17e2e08953d6/b87d700beee2c44826a9202c75d18c85.html?pageNumber=39'
LONG_VIDEO_LINK = 'https://www.xuexi.cn/f65dae4a57fe21fcc36f3506d660891c/b2e5aa79be613aed1f01d261c4a2ae17.html'
LONG_VIDEO_LINK2 = 'https://www.xuexi.cn/0040db2a403b0b9303a68b9ae5a4cca0/b2e5aa79be613aed1f01d261c4a2ae17.html'
TEST_VIDEO_LINK = 'https://www.xuexi.cn/8e35a343fca20ee32c79d67e35dfca90/7f9f27c65e84e71e1b7189b7132b4710.html'
SCORES_LINK = 'https://pc.xuexi.cn/points/my-points.html'
LOGIN_LINK = 'https://pc.xuexi.cn/points/login.html'
ARTICLES_LINK = 'https://www.xuexi.cn/d05cad69216e688d304bb91ef3aac4c6/9a3668c13f6e303932b5e0e100fc248b.html'

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
browser = webdriver.Chrome(options=options)

client = pymongo.MongoClient(host='localhost', port=27017)
db = client['learn_xi']
articles_col = db['article_data']
videos_col = db['video_data']


def login_simulation(username, password):
    """模拟登录"""
    # 方式一：使用cookies方式
    # 先自己登录，然后复制token值覆盖
    # cookies = {'name': 'token', 'value': ''}
    # browser.add_cookie(cookies)

    # 方式二：自己扫码登录
    # browser.get(LOGIN_LINK)
    # browser.maximize_window()
    # browser.execute_script("var q=document.documentElement.scrollTop=1000")
    # time.sleep(10)
    # browser.get(HOME_PAGE)
    # print("模拟登录完毕\n")

    # 方式三：账号密码登录
    browser.maximize_window()
    phone = ("+86", username)
    browser.get("https://pc.xuexi.cn/points/login.html")
    browser.get("https://login.dingtalk.com/login/index.htm?goto=https%3A%2F%2Foapi.dingtalk.com%2Fconnect%2Foauth2%2Fsns_authorize%3Fappid%3Ddingoankubyrfkttorhpou%26response_type%3Dcode%26scope%3Dsnsapi_login%26redirect_uri%3Dhttps%3A%2F%2Fpc-api.xuexi.cn%2Fopen%2Fapi%2Fsns%2Fcallback")
    browser.find_element_by_xpath("//select[@class='country_code_select']/option[@value='{}']".format(phone[0])).click()
    browser.find_element_by_xpath("//div[@id='mobilePlaceholder']").click()
    browser.find_element_by_xpath("//input[@id='mobile']").send_keys(phone[1])
    browser.execute_script("document.getElementById('pwd').setAttribute('style', 'display: inline-block')")
    browser.find_element_by_xpath("//input[@id='pwd']").click()
    browser.find_element_by_xpath("//input[@id='pwd']").send_keys(password)
    time.sleep(3)
    browser.find_element_by_xpath("//a[@id='loginBtn']").click()

    WebDriverWait(browser, 270).until(EC.title_is(u"我的学习"))
    # cookies = browser.get_cookies()
    # with open("./user/{}/cookies.txt".format(user_name), "w") as fp:
    #     json.dump(cookies, fp)
    #
    # check(phone, password)


def watch_videos(video_number=6, watch_time=1100):
    """观看视频"""
    if watch_time == 0:
        return
    spend_time = 0
    if video_number > 0:
        query = {"isWatch": False}
        new_values = {"$set": {"isWatch": True}}
        for video in videos_col.find(query).limit(video_number):
            browser.get(video['link'])
            time.sleep(1)
            browser.execute_script("var q=document.documentElement.scrollTop=500")
            # 点击播放
            try:
                browser.find_element_by_xpath("//div[@class='outter']").click()
            except ElementNotVisibleException:
                pass
            # 获取视频时长
            video_duration = video['video_duration']
            # 保持学习，直到视频结束
            time.sleep(video_duration + 5)
            spend_time += video_duration + 5
            time.sleep(1)
            browser.execute_script("var q=document.documentElement.scrollTop=300")
            videos_col.update_one({'link': video['link']}, new_values)
    print("已观看" + str(int(spend_time/60)) + "分钟")
    # 播放长视频
    browser.get(TEST_VIDEO_LINK)
    time.sleep(2)
    browser.execute_script("var q=document.documentElement.scrollTop=300")
    if watch_time - spend_time > 0:
        time.sleep(watch_time - spend_time)
        browser.execute_script("var q=document.documentElement.scrollTop=200")
    print("播放视频完毕\n")


def read_articles(article_number=6):
    """阅读文章"""
    browser.get(ARTICLES_LINK)
    query = {"is_read": False}
    new_values = {"$set": {"is_read": True}}
    if article_number == 0:
        return
    for article in articles_col.find(query).limit(article_number):
        browser.get(article['link'])
        for i in range(0, 2000, 100):

            js_code = "var q=document.documentElement.scrollTop=" + str(i)
            browser.execute_script(js_code)
            time.sleep(3.5)
        for i in range(2000, 0, -100):
            js_code = "var q=document.documentElement.scrollTop=" + str(i)
            browser.execute_script(js_code)
            time.sleep(3.5)
        articles_col.update_one({'link': article['link']}, new_values)
    print("阅读文章完毕\n")


def get_scores():
    """获取当前积分"""
    browser.get(SCORES_LINK)
    time.sleep(2)
    gross_score = browser.find_element_by_xpath("//*[@id='app']/div/div[2]/div/div[2]/div[2]/span[1]")\
        .get_attribute('innerText')
    today_score = browser.find_element_by_xpath("//span[@class='my-points-points']").get_attribute('innerText')
    print("当前总积分：" + str(gross_score))
    print("今日积分：" + str(today_score))
    print("获取积分完毕，即将退出\n")


if __name__ == '__main__':
    print("请输入学习强国APP用户名")
    usr = input()
    print("请输入学习强国APP密码")
    pwd = input()
    # 阅读文章个数
    articles_number = 6
    # 观看视频数量
    videos_number = 6
    # 观看视频时长
    videos_time = 1100
    # print("请输入想要阅读的文章数量：（不输入默认为6篇文章）")
    # articles_number = input()
    # if articles_number == "":
    #     articles_number = 6
    # else:
    #     articles_number = int(articles_number)
    # print("请输入想要观看的视频数量：（不输入默认为6个视频）")
    # videos_number = input()
    # if videos_number == "":
    #     videos_number = 6
    # else:
    #     videos_number = int(videos_number)
    # print("请输入想要观看的视频时间（以分钟为单位）：（不输入默认是18分钟）")
    # videos_time = input()
    # if videos_time == "":
    #     videos_time = 1100
    # else:
    #     videos_time = int(videos_time) * 60 + 10
    login_simulation(usr, pwd)  # 模拟登录
    read_articles(articles_number)     # 阅读文章
    watch_videos(videos_number, videos_time)      # 观看视频
    get_scores()        # 获得今日积分
    browser.quit()
