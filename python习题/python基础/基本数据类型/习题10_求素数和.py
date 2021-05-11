# -*-coding:utf-8-*-

# 求100以内的素数和。（编程题）

def primenumber(num):
    lis = []
    for i in range(2,num):
        flag = int(num ** 0.5)
        for j in range(2,flag):
            if i % j == 0:
                break
        else:
            lis.append(i)
    print(lis)
    print("总和是：%d"%(sum(lis)))

if __name__ == '__main__':
    primenumber(1000)




