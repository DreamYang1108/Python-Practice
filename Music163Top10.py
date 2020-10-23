# _*_ coding: utf-8 _*_
# @DateTime : 2020/10/20 22:56
# @Author   : DreamYang
# @File     : Music163Top10.py
# @Software : PyCharm 


import csv
import time
import logging
from lxml import etree
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


logger = logging.getLogger(__name__)
handler = logging.FileHandler(r"./data/Music163Top10.log", mode="w", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(level=logging.INFO)

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 3)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}


def get_singers(id, tag):
    """
    获取不同分类下的TOP10歌手并返回
    :param id: 分类id
    :param tag: 分类标签
    :return: 歌手id与歌手名
    """
    logger.info("正在爬取Top10的{}歌曲信息".format(tag))
    base_url = "https://music.163.com/#/discover/artist/cat?id=" + id
    browser.get(base_url)
    browser.switch_to.frame("g_iframe")
    page_text = browser.page_source
    tree = etree.HTML(page_text)
    li_list = tree.xpath("//ul[@class='m-cvrlst m-cvrlst-5 f-cb']/li")
    singer_dict = {}
    for li in li_list[0:10]:
        name = li.xpath("./p/a/text()")[0]
        singer_id = li.xpath("./p/a/@href")[0].split("=")[-1]
        singer_dict[singer_id] = name
    return singer_dict


def get_songs(singer_id, name):
    """
    获取每位歌手的TOP50歌曲信息
    :param singer_id: 歌手id
    :param name: 歌手姓名
    :return: TOP50歌曲信息
    """
    logger.info("正在爬取{}TOP50歌曲信息".format(name))
    singer_url = "https://music.163.com/#/artist?id=" + singer_id
    browser.get(singer_url)
    browser.switch_to.frame("g_iframe")
    page_text = browser.page_source
    tree = etree.HTML(page_text)
    tr_list = tree.xpath("//tbody/tr")
    songs = []
    for tr in tr_list:
        song = tr.xpath(".//td[2]//b/@title")[0]
        songs.append(song)
    return songs


def save_data(name, songs):
    """
    保存结果到本地
    :param name: 歌手名
    :param songs: 歌曲名
    """
    logger.info("正在保存{}的歌曲信息".format(name))
    for song in songs:
        with open(r"./data/Music163Top10.csv", mode="a", encoding="utf-8-sig", newline="") as f:
            csv_write = csv.writer(f)
            csv_write.writerow([name, song])


if __name__ == "__main__":
    time_start = time.time()
    print("==========正在进行爬虫==========")
    region_dict = {"1001": "华语男歌手", "1002": "华语女歌手", "1003": "华语组合/乐队",
                   "2001": "欧美男歌手", "2002": "欧美女歌手", "2003": "欧美组合/乐队",
                   "4001": "其他男歌手", "4002": "其他女歌手", "4003": "其他组合/乐队",
                   "6001": "日本男歌手", "6002": "日本女歌手", "6003": "日本组合/乐队",
                   "7001": "韩国男歌手", "7002": "韩国女歌手", "7003": "韩国组合/乐队"}

    for id, tag in region_dict.items():
        singer_dict = get_singers(id, tag)
        for singer_id, name in singer_dict.items():
            songs = get_songs(singer_id, name)
            save_data(name, songs)

        logger.info("已保存Top10的{}歌曲信息".format(tag))

    print("==========爬虫结束==========")
    time_end = time.time()
    print("总共耗时{}秒".format(str(round(time_end-time_start, 0))))

