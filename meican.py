#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/1/22 00:28
# @Author  : Sunbowen
# @Email   : sunbowen@zhuge.com
# @File    : meican.py
# @Software: PyCharm

import sys
import requests,time

class Meican:
    def __init__(self, id):
        self.id = id

    def get_data(self):
        now = time.time()
        ten = now - (now % 86400) + 7200
        targetTime = time.strftime("%Y-%m-%d %H:%M", time.localtime(ten))
        data = {
                "tabUniqueId":"9a0b88c8-d520-4ad0-9d46-aa497667e8eb",
                "order":"[{'count':1,'dishId': "+self.id+"}]",
                "targetTime":targetTime,
                "userAddressUniqueId":"31cfe018f71b",
                "corpAddressUniqueId":"31cfe018f71b",
                "remarks":"[{'dishId':'"+self.id+"','remark':''}]"
                }
        return data

    def get_headers(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'Cache-Control': 'no-cache',
            'Content-Length': '6',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'www.mm131.com',
            'Pragma': 'no-cache',
            'Origin': 'http://www.mm131.com/xinggan/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'cookie': "machineId=c405012e-2f2e-4536-a62f-dd02737fad5c; __utmz=1.1545580882.1.1.utmcsr=meican.com|utmccn=(referral)|utmcmd=referral|utmcct=/; guestId=d67b38ca-6b62-4515-9709-bb9302fabfd0; __utma=1.1859136358.1545580882.1545901463.1546012076.3; remember=e04b8052b14855918ce9919c45f975cc9dc4f1d5-1080644; Hm_lvt_d63dbf1497d491c4e3cf91f6efab2555=1545580881,1547086601,1547613121,1548088957; Hm_lpvt_d63dbf1497d491c4e3cf91f6efab2555=1548088957"
        }
        return headers

def main():
    id = sys.argv[1]
    url = "https://meican.com/preorder/api/v2.1/orders/add"
    now = time.time()
    time_now = now - (now % 86400) + 3400
    meican = Meican(id)
    data = meican.get_data()
    headers = meican.get_headers()
    print(data)
    while 1:
        now = time.time()
        if int(now) > int(time_now):
            a = requests.post(url=url, data=data, headers=headers)
            print(a.text)
        elif int(now) < int(time_now + 400):
            break
        time.sleep(3)

if __name__ == '__main__':
    main()



