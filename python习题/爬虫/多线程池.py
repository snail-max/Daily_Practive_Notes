# -*-coding:utf-8-*-
# import time
#
#
# def get_url(url):
#     print("正在下载：",url)
#     time.sleep(2)
#     print('下载成功：',url)
#
# urls = [
#     'www.baidu.com',
#     'www.sougou.com',
#     'https://www.baidu.com/s?wd=IP'
# ]
# start_time = time.time()
#
# for url in urls:
#     get_url(url)
#
# end_time  = time.time()
#
# print("总共耗时{}s".format(end_time-start_time))
import time
from multiprocessing.dummy import Pool

start_time = time.time()
def get_url(url):
    time.sleep(2)

urls = [
    'www.baidu.com',
    'www.sougou.com',
    'https://www.baidu.com/s?wd=IP'
]
# 实例化线程池对象
pool = Pool(4)
# 将列表中的每一个元素单独交给get_url处理
pool.map(get_url,urls)
end_time = time.time()

print("总共耗时{}s".format(end_time-start_time))
