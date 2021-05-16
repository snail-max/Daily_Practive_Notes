# -*-coding:utf-8-*-
# 写一个计算每个程序执行时间的装饰器；



import time


def spendtime(func):
    def inner(*args,**kwargs):
        start_time = time.time()
        ret = func(*args,**kwargs)
        spend_time = time.time() - start_time
        print("一共花费时间为{}".format(spend_time))
        return ret
    return inner

@spendtime
def func():
    time.sleep(5)


if __name__ == '__main__':
    func()