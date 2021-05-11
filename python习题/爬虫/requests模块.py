# -*-coding:utf-8-*-

"""
    1.指定url
    2.get方法获取一个响应对象
    3.获取相应数据字符串的形式存储.text
    4.持久化存储

"""
import requests





def re_url(url):
    reponse = requests.get(url)
    reponse_text = reponse.text
    with open('sougou.text','w',encoding='utf-8') as f:
        f.write(reponse_text)



if __name__ == '__main__':
    url = 'http://www.baidu.com'
    re_url(url)