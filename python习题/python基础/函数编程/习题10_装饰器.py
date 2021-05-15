# -*-coding:utf-8-*-
# 编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），要求登录成功一次，后续的函数都无需再输入用户名和密码


def decorator(func):
    def inner(*args, **kwargs):
        IsCertification = False
        name = input("亲输入用户名：")
        passwd = input("请输入密码:")
        dic = {}
        with open("passwd.txt", 'r', encoding='utf-8') as f:

            for line in f.readlines():
                information = line.split('/\n')[0].split('=')
                dic[information[0]] = information[1]
        try:
            if dic[name] == passwd:
                IsCertification = True
        except Exception as e:
            print(e)
        while IsCertification:
            func(*args, **kwargs)
    return inner()


@decorator
def CommonFuntion():
    print("函数执行了")


if __name__ == '__main__':
    CommonFuntion()
