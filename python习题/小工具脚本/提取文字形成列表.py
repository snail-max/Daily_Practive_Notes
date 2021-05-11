# -*-coding:utf-8-*-
# 需求：对UserAgent文档中的数据useragent数据进行提取




useragent_list = []
with  open('useragent.txt','r',encoding='utf-8') as fp:
    for line in fp.readlines():
        if line.startswith('Mozilla') and line != None:
            line = line.split('\n')[0]
            print(line)
            line_str = line
            useragent_list.append(line_str)
    print(useragent_list)
with open('temp.txt',mode='w',encoding='utf-8') as tp:
    tp.write(str(useragent_list))



