# -*-coding:utf-8-*-
import requests
from  lxml import etree
import re

from multiprocessing.dummy import Pool
headers = {
    'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/89.0.4389.90Safari/537.36'
}
url = 'https://www.pearvideo.com/category_5'



res_text = requests.get(url=url,headers=headers,proxies={'http':'25.122.144.141:9999'}).text
tree = etree.HTML(res_text)
li_list = tree.xpath('//ul[@id="listvideoListUl"]/li')
print(li_list)
for li in li_list:
    vidio_url = li.xpath('./div/a/@href')[0]
    url_temp = 'https://www.pearvideo.com/'+vidio_url
    vadio_name= li.xpath('./div/a/div[2]/text()')[0]+'.mp4'
    reste = requests.get(url=url_temp,headers=headers,proxies={'http':'25.122.144.141:9999'}).text
    '"srcUrl": ".*?"'
    ex = 'srcUrl="(.*?)"'
    video_url = re.findall(ex,reste)
    print(video_url)


