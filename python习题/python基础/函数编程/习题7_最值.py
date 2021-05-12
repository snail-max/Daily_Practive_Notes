# -*-coding:utf-8-*-

# 写函数，传入n个数，返回字典{‘max’:最大值,’min’:最小值}
    # 例如:minmax(2,5,7,8,4)
    # 返回:{‘max’:8,’min’:2}




def  minmax(*args):
    dic = {}
    dic['max'] = max(args)
    dic["min"] = min(args)

    print(dic)

minmax(2,5,7,8,4)