import time
import requests
import random
import re
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from multiprocessing import Queue, Process
from bs4 import BeautifulSoup
import lxml

# 设置文件的请求头

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}

url_base = 'https://www.cilitiantang2022.xyz/'


# 读取txt文件获取关键词
def read_txt(text_path):
    key_list = []
    try:
        with open(text_path, encoding='utf-8') as f:
            str_line = f.readlines()
            for line in str_line:
                for key in line.split(' '):
                    key_list.append(search_key(key.strip('\n')))
    except IndentationError as e:
        print("文件路径不存在")
    return key_list


# 设置生产者消费者模型
# 给生产者添加关键字
def producer(q, key_word):
    q.put(key_word)


# 给消费者输入值
def consumer(q, key_word):
    while 1:
        info = q.get()
        if info:
            search_key(info)
        else:
            break


# 输入关键点击搜索:
def search_key(key_word):
    # driver = webdriver.Chrome()
    # # 设置成隐式等待
    # driver.implicitly_wait(10)
    # driver.get("https://www.cilitiantang2022.xyz/")
    # try:
    #     driver.find_element_by_name('kw').send_keys(key_word)
    #     driver.find_element_by_xpath('/html/body/div/div/form/div[2]/span/button').click()
    #     time.sleep(random.randint(5,15))
    # except NoSuchElementException as e:
    #     print(e)
    # current_url = driver.current_url
    # 修改成直接发送request请求获取
    # urls = ['https://www.cilitiantang2022.xyz/search/' + key_word + '_ctime_{}.html'.format(str(i) for i in range(1, 10))]
    content_lis = []
    for i in range(1, 10):
        url = 'https://www.cilitiantang2022.xyz/search/' + key_word + '_ctime_{}.html'.format(str(i))
        print(url)
        # 设置随机时间
        time.sleep(random.randint(2, 7))
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(response.status_code)
            cont = response.text
            html = BeautifulSoup(cont, 'lxml')
            con_li = html.find_all('h5', class_="item-title")
            content_lis.append(con_li)
            # if len(con_li) != 0:
            #     for li in con_li:
            #         print(li)
            #         text = re.match(
            #             r'<h5 class="item-title"><a href="(.*?)" target="_blank">(.*?)<span class="highlight">'
            #             r'(.*?)</span>(.*?)</a><span class="click"></span><span class="highlight"></span></h5>', li,re.M | re.I)
            #     content_lis.append(list(text.groups()))
        else:
            print('{}没有访问到'.format(url))
    # 对搜索过的界面,提取网址
    time.sleep(1)
    yield content_lis
    

# def write_info(cont_list):
#     for lis in cont_list:
#         text = re.match(r'< h5 class ="item-title" > < a href="(.*?)" target="_blank" > ? < span class ="highlight" >'
#                  ' (.*?) < / span > (.*?) < / a > < span class ="click" > < / span > < span class ="highlight" > < / span > < / h5 >',lis)
#         print(text.group())
# with open('number.txt',mode='w',encoding='utf-8') as f:

if __name__ == '__main__':
    q = Queue(10)
    path = 'key_words'
    # 设置一个文件对解析的数据进行保存
    content_lis = read_txt(path)
    if len(content_lis) != 0:
        for key in content_lis:
            p_pro = Process(target=producer, args=(q, key))
            p_con = Process(target=consumer, args=(q, key))
            p_pro.start()
            p_con.start()
