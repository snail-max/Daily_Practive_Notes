# -*-coding:utf-8-*-

import random






def Rolldice(bet,num):
    sum = 0
    for i in range(3):
        sum += random.randint(1,6)
    if sum <9 and bet=="小":
        print("赚取{}元".format(num))
    elif  sum >9 and bet=="大":
        print("赚取{}元".format(num))
    else:
        print("亏损{}元".format(num))



if __name__ == '__main__':
    Rolldice("大",10)



