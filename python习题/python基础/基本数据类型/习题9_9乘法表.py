# -*-coding:utf-8-*-

# 10、利用for循环和range输出9 * 9乘法表 。（编程题）

for i in range(1,10):
    for j in range(1,i):
        print('%d*%d=%d'%(j,i,i*j),end=' ')
    print('')