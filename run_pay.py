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
from pay import *
import multiprocessing

cur_dir = os.path.split(os.path.realpath(__file__))[0]
sys.path.append("%s/" % cur_dir)


def test(username="13691926738", password="Ljc19941108",
         url="https://www.nike.com/cn/launch/t/kyrie-5-nike-day/", size="EU 46"):
    browser = Browser.Browser(browser_type="Chrome", headless=False, timeout=1000)
    result = login(browser, username=username, password=password,
                   url=url)
    if result.get("status", "-1") == "1":
        pay(browser,url)
    browser.close()

if __name__ == '__main__':
    test()