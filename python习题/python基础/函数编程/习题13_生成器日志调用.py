# -*-coding:utf-8-*-
"""
通过生成器写一个日志调用方法， 支持以下功能

    根据指令向屏幕输出日志
    根据指令向文件输出日志
    根据指令同时向文件&屏幕输出日志
    以上日志格式如下
        2017-10-19 22:07:38 [1] test log db backup 3
        2017-10-19 22:07:40 [2]    user alex login success
        #注意：其中[1],[2]是指自日志方法第几次调用，每调用一次输出一条日志
"""
import time
import datetime


def logging(num):
    if num == 1:
        yield  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),i
    elif num == 2:
        with open('log.txt','a',encoding='utf-8') as f:
            f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'\n')
        yield time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),i



for i in range(1,10):

    logging(2).__next__()






