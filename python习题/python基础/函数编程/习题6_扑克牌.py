# -*-coding:utf-8-*-


# 写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组
#
# 例如：[(‘红心’，2),(‘草花’，2), …(‘黑桃A’)]



def poker():
    numlis = [ str(i) for i in range(2,11)]
    polis = ['A','J','Q','K']
    numlis.extend(polis)
    poket = ["草花","梅花","方块","红桃"]
    lis = []

    for num in numlis:
        for pok in poket:
            lis.append((num,pok))
    return lis

print(poker())