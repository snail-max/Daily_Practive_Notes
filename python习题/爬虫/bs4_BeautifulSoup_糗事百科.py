# -*-coding:utf-8-*-


import requests
from bs4 import BeautifulSoup
import random
import time
import re
from lxml import etree
import os


def qiushibaike():
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64)AppleWebKit/537.36'
                      '(KHTML,likeGecko)Chrome/89.0.4389.90Safari/537.36'
    }

    if not os.path.exists('./qiushi_img'):
        os.makedirs('./qiushi_img')
    for page_num in range(1, 15):
        time.sleep(random.randint(1, 3))
        url = 'https://www.qiushibaike.com/imgrank/page/{}/'.format(page_num)
        print(url)
        res = requests.get(url=url, headers=headers,proxies={'http':'25.122.144.141:9999'})
        print(res.status_code)
        res = res.text
        # ex = '<img src="(.*?)" .*?>'
        # < img src = "//pic.qiushibaike.com/system/pictures/12423/124232227/medium/TGR6BXAQI6JGXC6H.jpg"
        # alt = "糗事#124232227" class ="illustration" width="100%" height="auto" >
        # print(res)
        # lis = re.findall(ex,res,re.S)
        # print(res)
        # soup = BeautifulSoup(res,'lxml')
        # a_list = soup.find('div',class_='thumb')
        # a_list = soup.select('.thumb > img')
        # a_list = soup.select('.image > div ')
        print(res)
        tree = etree.HTML(res)
        all_list = tree.xpath('//div[@class="thumb"]/a/img/@src')
        for li in all_list:
            file_name = li.split('/')[-1]
            file_path = os.path.join('./qiushi_img', file_name)
            file_url = url + li
            res_img = requests.get(url=file_url, headers=headers,proxies={'http':'25.122.144.141:9999'}).content
            with open(file_path, 'wb') as f:
                f.write(res_img)
            print('写入图片%s' % file_name)


if __name__ == '__main__':
    qiushibaike()
