# -*-coding:utf-8-*-
"""
    如下，每个小字典的name对应股票名字，shares对应多少股，price对应股票的价格
        portfolio = [
    {‘name’: ‘IBM’, ‘shares’: 100, ‘price’: 91.1},
    {‘name’: ‘AAPL’, ‘shares’: 50, ‘price’: 543.22},
    {‘name’: ‘FB’, ‘shares’: 200, ‘price’: 21.09},
    {‘name’: ‘HPQ’, ‘shares’: 35, ‘price’: 31.75},
    {‘name’: ‘YHOO’, ‘shares’: 45, ‘price’: 16.35},
    {‘name’: ‘ACME’, ‘shares’: 75, ‘price’: 115.65}
]
    `通过哪个内置函数可以计算购买每支股票的总价
    用filter过滤出，单价大于100的股票有哪些

"""

info = "portfolio = [    {‘name’: ‘IBM’, ‘shares’: 100, ‘price’: 91.1}," \
       "{‘name’: ‘AAPL’, ‘shares’: 50, ‘price’: 543.22}," \
       "{‘name’: ‘FB’, ‘shares’: 200, ‘price’: 21.09}," \
       "{‘name’: ‘HPQ’, ‘shares’: 35, ‘price’: 31.75}," \
       "{‘name’: ‘YHOO’, ‘shares’: 45, ‘price’: 16.35}," \
       "{‘name’‘ACME’, ‘shares’: 75, ‘price’: 115.65}" \
       "]"

# 对原始数据格式化,将引号改变
# info = info.replace("’", '"')
# info = info.replace("‘", '"')
# print(info)

info = [{"name": "IBM", "shares": 100, "price": 91.1}, {"name": "AAPL", "shares": 50, "price": 543.22},
        {"name": "FB", "shares": 200, "price": 21.09}, {"name": "HPQ", "shares": 35, "price": 31.75},
        {"name": "YHOO", "shares": 45, "price": 16.35}]


lis = map(lambda x:x["shares"]*x["price"],info)
print(lis.__next__())




def greater(num):
    return num > 100
lis2 = [i["price"] for i in info]
lis1 = filter(greater,lis2)
print(lis1)