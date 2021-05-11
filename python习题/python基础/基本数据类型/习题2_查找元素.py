# -*-coding:utf-8-*-
"""
    2、查找列表中元素，移除每个元素的空格，并查找以a或A开头并且以c结尾的所有元素
        li = ["alec", " aric", "Alex", "Tony", "rain"]
        tu = ("alec", " aric", "Alex", "Tony", "rain")
        dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}
"""

li = ["alec", " aric", "Alex", "Tony", "rain"]
tu = ("alec", " aric", "Alex", "Tony", "rain")
dic1 = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}


def SearchElement(li):
    if type(li) is dict:
        for key, value in dic1.items():
            checkelemet(key)
            checkelemet(value)
    elif type(li) is list or type(li) is tuple:
        for i in li:
            checkelemet(i)


def checkelemet(element):
    i = element.strip()
    if i[-1] is 'c' and i.lower()[0] is 'a':
        print("这个元素是%s" % i)


SearchElement(li)
SearchElement(tu)
SearchElement(dic1)
