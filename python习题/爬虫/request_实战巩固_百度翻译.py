# -*-coding:utf-8-*-


import requests
import json


def BaiduInterput(url):
    key = input('请输入一个一段文字：')
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/89.0.4389.90Safari/537.36'
    }
    data = {
        'kw':key
    }
    response  = requests.post(url=url,data=data,headers=headers)
    res_json = response.json()
    file_name = key+'.json'
    # 进行持久化存储
    fp = open(file_name,'w',encoding='utf-8')
    json.dump(res_json,fp=fp,ensure_ascii=False)

if __name__ == '__main__':
    url = 'https://fanyi.baidu.com/sug'
    BaiduInterput(url)

