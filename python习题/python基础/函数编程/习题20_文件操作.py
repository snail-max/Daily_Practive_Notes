# -*-coding:utf-8-*-
# 有名为username.txt的文件，其内容格式如下，写一个程序，
# 判断该文件中是否存在”alex”, 如果没有，则将字符串”alex”添加到该文件末尾，否则提示用户该用户已存在；

with open('username.txt','r+',encoding="utf-8") as f:
    lis = f.readlines()
    for i in lis:
        if 'alex' in i:
            break
    else:
        f.write('alex')


