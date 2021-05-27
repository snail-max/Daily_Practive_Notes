# -*-coding:utf-8-*-


"""
    根据用户输入的用户名&密码，找到对应的json文件，把数据加载出来进行验证
    用户名为json文件名，密码为 password。
    判断是否过期，与expire_date进行对比。
    登陆成功后，打印“登陆成功”，三次登陆失败，status值改为1，并且锁定账号。
    用户密码进行hashlib加密处理。即：json文件里的密码保存为md5的值，然后用md5的值进行验证账号信息是否正确
"""
import json
import os
import time
import datetime
import hashlib
import sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
sys.path.append(BASE_DIR)

from ..core import withdraw


# {"expire_date": "2021-01-01", "id": 1234, "status": 0, "pay_day": 22, "password": "abc"}


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


def login(function):
    def inner(*args,**kwargs):
        name = input("请输入用户名: ").strip("")
        filepath = os.path.join('../account', str(name) + ".json")
        today = time.strftime("%Y-%m-%d", time.localtime())
        print(today)
        if os.path.exists(filepath):
            f = open(filepath)
            informationJson = json.load(f)
            m = hashlib.md5()

            if informationJson["status"] == 0:
                for i in range(3):
                    passwd = input("请输入密码").strip("")
                    m.update(passwd.encode("utf-8"))
                    passwd = m.hexdigest()
                    # 时间字符串比较大小
                    if informationJson["password"] == passwd:
                        if datetime.datetime.strptime(today, '%Y-%m-%d') > datetime.datetime.strptime(
                                informationJson["expire_date"], '%Y-%m-%d'):
                            print("用户名密码已经过期，请重置密码")
                            m.update(input("请输入重置的密码").strip(""))
                            resetPasswd = m.hexdigest()
                            with open(filepath, 'w+') as fw:
                                informationJson["password"] = resetPasswd
                                # 修改密码后有效时效增加30天
                                dateNow = datetime.datetime.now() + datetime.timedelta(30)  # 当前时间 30天
                                informationJson["expire_date"] = str(dateNow).split(" ")[0]
                                json.dump(informationJson, fw)
                                print("修改密码成功")
                                break
                        else:
                            print("登录成功")
                            function(*args,**kwargs)
                            break
                    else:
                        print("密码错误")
                else:
                    with open(filepath, 'w+') as f1:
                        informationJson["status"] = 1
                        json.dump(informationJson, f1)
                    print("输入密码超过3次账户锁住")
            else:
                print("用户登录错误被锁住,请联系管理员")
        else:
            print("用户名不存在")
            exit()
    return inner


# 账户信息
def AccountInformation():
    f = open("../account/alex.json")
    accountInformation = json.load(f)
    print("账户余额：{}".format(accountInformation["pay_day"]))


# 转账
def transfer():
    unitPrice = 950000
    poundage = unitPrice * 0.05
    paymaney = unitPrice + poundage
    fr = open("../account/alex.json")
    userdic = json.load(fr)
    with open("../account/alex.json", "w+") as fw:
        if userdic["pay_day"] > paymaney:
            userdic["pay_day"] -= paymaney
            json.dump(userdic, fw)
            fr1 = open("../account/tesla_company.json")
            tsaaccount = json.load(fr1)
            with open("../account/tesla_company.json", "w+") as fw1:
                tsaaccount["account"] += unitPrice
                json.dump(tsaaccount, fw1)
            print("购买成功")

        else:
            print("账户余额不足,无法支付")


def PaymentAction():
    print("==================================")
    print("|| 1.账户信息                     ||")
    print("|| 2.转账                        ||")
    print("|| 3.提现                        ||")
    print("==================================")
    try:
        selectId = int(input("请输入选项的序号：").strip(""))
    except Exception as e:
        print(e)
        print("亲输入序号")
    if selectId == 1:
        AccountInformation()
    elif selectId == 2:
        transfer()
    elif selectId == 3:
        withdraw.withDraw()



if __name__ == '__main__':
    PaymentAction()
