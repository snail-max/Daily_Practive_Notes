# -*-coding:utf-8-*-


# 有列表 li = [‘alex’, ‘egon’, ‘smith’, ‘pizza’, ‘alen’], 请以列表中每个元素的第二个字母倒序排序；


li = ["alex", "egon", "smith", "pizza", "alen"]

# print(list(sorted(li, key=lambda x: x[1], reverse=True)))
print(list(sorted(li,key=lambda x:x[1],reverse=True)))
