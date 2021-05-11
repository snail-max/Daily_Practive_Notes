# -*-coding:utf-8-*-
"""

4、写代码，有如下列表，请按照功能要求实现每一个功能
    li = ["hello", 'seven', ["mon", ["h", "kelly"], 'all'], 123, 446]
    请根据索引输出“Kelly”
    请使用索引找到’all’元素并将其修改为“ALL”，如：li[0][1][9]…
"""

li = ["hello", 'seven', ["mon", ["h", "kelly"], 'all'], 123, 446]
print(li[2][1][1])
li[2][2] = "ALL"
print(li)