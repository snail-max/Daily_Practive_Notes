# -*-coding:utf-8-*-


# 用filter函数处理数字列表，将列表中所有的偶数筛选出来
# num = [1,3,5,6,7,8]

num = [1,3,5,6,7,8]

def is_odd(number):
    return number%2 == 0


newlist = filter(is_odd,num)
print(newlist.__next__())



