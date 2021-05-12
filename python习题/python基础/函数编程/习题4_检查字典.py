# -*-coding:utf-8-*-


#写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容（对value的值进行截断），
# 并将新内容返回给调用者，注意传入的数据可以是字符、list、dict


def checkdic(*args,**kwargs):
    # print(args)
    for key,value in args[0].items():
        if len(value) > 2:
            args[0][key] = value[0:2]
    print(args[0])


dic = {"key": ['aaa','bbb','ccc']}
checkdic(dic)

