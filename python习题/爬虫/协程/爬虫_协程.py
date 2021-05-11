# -*-coding:utf-8-*-
import asyncio
import time


async def get_request(url):
    print('下载开始')
    time.sleep(2)
    print('下载结束')


urls = {
    'www.baidu.com',
    'www.sougou.com',
    'www.jingdong.com'
}




tasks = []
for url in urls:
    c = get_request(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
