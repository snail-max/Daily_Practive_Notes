# -*-coding:utf-8-*-
#有名为user_info.txt的文件，其内容格式如下，
# 写一个程序，将id为100002的用户名修改为alex li；



import os


filename = "user_info.txt"

file_new = "%s.new"%(filename)

f_new = open(file_new,"w",encoding="utf-8")

with open(filename,"r",encoding="utf-8") as f:
    for line in f:
        if '100002' in line:
            line = ",".join(["alex li","100002"])
            f_new.write(line+"\n")
        else:
            f_new.write(line)
f_new.close()
os.replace(file_new,filename)







