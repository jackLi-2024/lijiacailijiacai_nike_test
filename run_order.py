#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
File:   .py
Author: Lijiacai (v_lijiacai@baidu.com)
Date: 2018-xx-xx
Description:
"""

import os
import sys
from login import *
from orderUtil import *
from SpiderTool import Browser
import logging

cur_dir = os.path.split(os.path.realpath(__file__))[0]
sys.path.append("%s/" % cur_dir)


def test(username="13691926738", password="Ljc19941108",
         url="https://www.nike.com/cn/launch/t/air-max-95-premium-throwback-future/"):
    browser = Browser.Browser(browser_type="Chrome", headless=False, timeout=1000)
    result = login(browser, username=username, password=password,
                   url=url)

    if result.get("status", "-1") == "1":
        try:
            order = Order(result.get("browser"))
            if order.getOrderRecords():
                with open("order.json", "a") as f:
                    f.write(json.dumps({"username": username, "password": password, "goods": "yes"},
                                       ensure_ascii=False) + "\n")
        except Exception as e:
            logging.exception(str(e))
    browser.close()


def run():
    p = multiprocessing.Pool(1)
    with open("nike.txt","r") as f:
        for one in f:
            l = one.split("\t")
            username = l[0].strip()
            password = l[1].strip()
            p.apply_async(test,args=(username,password))
    p.close()
    p.join()


if __name__ == '__main__':

    test()

