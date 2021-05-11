# -*-coding:utf-8-*-
"""
    6、转换
        将字符串s = “alex”转换成列表
        将字符串s = “alex”转换成元祖
        将列表li = [“alex”, “seven”]转换成元组
        将元组tu = (‘Alex’, “seven”)转换成列表
        将列表li = [“alex”, “seven”]转换成字典且字典的key按照10开始向后递增
"""

s = "alex"
slis = list(s)
print(slis)
tups = tuple(s)
print(tups)
li = ["alex","seven"]
print(tuple(li))
tu = ("Alex","seven")
listu = list(tu)
print(listu)
li = ["alex","seven"]
dic = {}
for i in range(10,10+len(li),1):
    dic[i] = li[i-10]
print(dic)

