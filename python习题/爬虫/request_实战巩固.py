# -*-coding:utf-8-*-
"""
    需求：搜狗指定词条对应的页面搜素结果
    需求：破解百度翻译
    需求：爬取豆瓣电影分类排行榜 https://movie.douban.com/中的详细数据

"""

import requests

# UA伪装
#UA：User-angent（请求载体的身份标识）

def sougou_seaerch_key(url):
    # 对指定的url，是携带参数的
    kw = input('enter a word:')
    param = {
        'query': kw
    }
    print(url)
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/89.0.4389.90Safari/537.36'
    }
    response = requests.get(url=url,params=param,headers=headers)
    res_text = response.text
    filename = kw+'.html'
    with open(filename,'w',encoding='utf-8') as f:
        f.write(res_text)





if __name__ == '__main__':
    url = 'https://www.sogou.com/web'
    sougou_seaerch_key(url)
