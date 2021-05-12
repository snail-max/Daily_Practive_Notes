# -*-coding:utf-8-*-
# 写函数，计算传入数字参数的和。（动态传参）


def number(*args, **kwargs):
    sum = 0
    for num in args:
        sum += num
    print(sum)


num1 = 1
num2 = 2

number(1, 2,3)
