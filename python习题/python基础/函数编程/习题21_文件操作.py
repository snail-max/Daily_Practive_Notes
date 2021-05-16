# -*-coding:utf-8-*-


#有名为user_info.txt的文件，其内容格式如下，写一个程序，删除id为100003的行；


import os

filepath = r'user_info.txt'
newfile = '%s.new'%(filepath)


f_new = open(newfile,'w',encoding="utf-8")

with open(filepath,'r',encoding='utf-8') as f:
    for line in f.readlines():
        if '100003' in line:
            pass
        else:
            f_new.write(line)
f_new.close()
os.replace(newfile,filepath)