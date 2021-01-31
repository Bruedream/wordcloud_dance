import requests
import pandas as pd
import re
import time
import random
from concurrent.futures import ThreadPoolExecutor
import datetime
from fake_useragent import UserAgent

# 随机产生请求头
ua = UserAgent(verify_ssl=False, path='fake_useragent.json')
start_time = datetime.datetime.now()


def grab_barrage(date):
    # 伪装请求头
    headers = {
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "accept-encoding": "gzip",
        "origin": "https://www.bilibili.com",
        "referer": "https://www.bilibili.com/video/BV1rD4y1Q7jc?from=search&seid=10634574434789745619",
        "user-agent": ua.random,
        "cookie": "finger=158939783; _uuid=35D2EAA5-CF9E-0F4E-36FA-B682DE0952D758849infoc; buvid3=383AC5EC-1294-46AF-8D29-EAE21A54A5E8143082infoc; rpdid=|(Y|YkYukR|0J'ulmlmRR)uY; sid=9nzocel4; DedeUserID=351906959; DedeUserID__ckMd5=7c02cbbf60a2e150; SESSDATA=c2a82a7c%2C1612434769%2C3d540*81; bili_jct=73d05a1054a125f99cc0a2f81c637493; blackside_state=1; CURRENT_FNVAL=80; LIVE_BUVID=AUTO4415999633949722; CURRENT_QUALITY=0; PVID=1; bsource=search_google; bfe_id=6f285c892d9d3c1f8f020adad8bed553"
    }

    # 构造url访问 需要用到的参数 爬取指定日期的弹幕
    params = {
        'type': 1,
        'oid': '206344228',
        'date': date
    }
    # 发送请求 获取响应
    response = requests.get(url, params=params, headers=headers)
    # print(response.encoding) #重新设置编码
    response.encoding = 'utf-8'
    # 正则匹配提取数据 转成集合去除重复弹幕
    # print(response.text)
    comment = set(re.findall('<d p=".*?">(.*?)</d>', response.text))
    # 将每条弹幕数据写入txt
    with open('bullet.txt', 'a+') as f:
        for con in comment:
            f.write(con+'\n')
            print(con)
    time.sleep(random.randint(1, 3))  # 休眠


def main():
    # 开多线程爬取 提高爬取效率
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(grab_barrage, date_list)
    # 计算所用时间
    delta = (datetime.datetime.now()-start_time).total_seconds()
    print(f'用时：{delta}s   -----------> 弹幕数据成功保存到本地txt')


if __name__ == '__main__':
    # 目标url
    url = "https://api.bilibili.com/x/v2/dm/history"
    start = '20201201'
    end = '20210128'
    # 生成时间序列
    date_list = [x for x in pd.date_range(start, end).strftime('%Y-%m-%d')]
    print(date_list)
    count = 0
    # 调用主函数
    main()