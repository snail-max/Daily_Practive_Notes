# -*-coding:utf-8-*-
# 有列表 li = [‘alex’, ‘egon’, ‘smith’, ‘pizza’, ‘alen’], 请将以字母“a”开头的元素的首字母改为大写字母；






li = ["alex", "egon", "smith", "pizza", "alen"]



lis = map(lambda x:x.title() if x[0]=='a'else x ,li)
print(lis.__next__())