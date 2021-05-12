# -*-coding:utf-8-*-
"""
写函数，专门计算图形的面积
    其中嵌套函数，计算圆的面积，正方形的面积和长方形的面积
    调用函数area(‘圆形’,圆半径) 返回圆的面积
    调用函数area(‘正方形’,边长) 返回正方形的面积
    调用函数area(‘长方形’,长，宽) 返回长方形的面积
"""


def area(*args):

    def circular(r):
        return 3.14 * r ** 2

    def square(r):
        return r ** 2

    def rectangle(l, h):
        return l * h


    if args[0] == "圆形":
        return circular(args[1])
    elif args[0] == "正方形":
        return square(args[1])
    elif args[0] == "长方形":
        return rectangle(args[1],args[2])



if __name__ == '__main__':
    print(area("圆形",5))
