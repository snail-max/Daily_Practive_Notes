# -*-coding:utf-8-*-
# 16、有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

import os


def statisticalData(filepath):
    lispath = []
    for root, dirs, files, in os.walk(filepath):
        for name in files:
            if name.split(".")[-1] == "py":
                abspath = os.path.join(root, name)
                lispath.append(abspath)
    return lispath


def readpython(pypath_lis):
    sumlis = 0
    zhushi = 0
    nullli = 0
    for pypath in pypath_lis:
        with open(pypath, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                if len(line) == 0:
                    nullli += 1
                elif line[0] == "#":
                    zhushi += 1
                sumlis += 1
    print("总行数：{}，注释行数：{}，空行{}".format(sumlis, zhushi, nullli))


def run(filepath):
    pypath_lis = statisticalData(filepath)
    readpython(pypath_lis)



if __name__ == '__main__':
    filepath = r"D:\Git_Work_Space\Daily_Practive_Notes\python习题\爬取小说存入数据库"
    run(filepath)