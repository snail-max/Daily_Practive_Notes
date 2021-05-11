# -*-coding:utf-8-*-

# 1、请用代码实现：利用下划线将列表的每一个元素拼接成字符串，li＝[‘alex’, ‘eric’, ‘rain’]


li = ["alex", "eric", "rain"]

strsum = ''
for i in li:
    strsum =strsum+'_'+i
print(strsum)


strli = [i + '_'for i in li]
print(strli)
