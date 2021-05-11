# -*-coding:utf-8-*-
import requests
import json


def kfc():
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx'
    data = {
        'cname': '',
        'pid': '',
        'keyword': '北京',
        'pageIndex': '1',
        'pageSize': '10'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0;WOW64)AppleWebKit/537.36(KHTML,'
                      'likeGecko)Chrome/89.0.4389.90Safari/537.36 '
    }

    response = requests.post(url=url, data=data,headers=headers)
    print(response.text)


if __name__ == '__main__':
    kfc()
