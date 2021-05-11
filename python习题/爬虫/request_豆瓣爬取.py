# -*-coding:utf-8-*



import requests
import json





def DouBan():
    url = "https://movie.douban.com/j/chart/top_list"
    param = {
        'type':'24',
        'interval_id':'100:90',
        'action':'',
        'start':'1',
        'limit':'20',
    }
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/89.0.4389.90Safari/537.36'
    }

    res = requests.get(url=url,params=param,headers=headers)
    res_json = res.json()
    fp = open('aa.json', 'w', encoding='utf-8')
    json.dump(res_json, fp=fp, ensure_ascii=False)

if __name__ == '__main__':
    DouBan()