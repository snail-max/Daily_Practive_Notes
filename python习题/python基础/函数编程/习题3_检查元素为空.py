# -*-coding:utf-8-*-




def cheackelement(*args):
    len_num = len(args)
    if len_num:
        return args
    else:
        return None



lis = [1,2,3]
tuple = ()
print(cheackelement(tuple))
