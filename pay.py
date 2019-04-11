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
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from SpiderTool import Browser
import multiprocessing
import logging
import time
cur_dir = os.path.split(os.path.realpath(__file__))[0]
sys.path.append("%s/" % cur_dir)


def pay(browser=None, url=""):
    browser.get(url)
    time.sleep(5)
    browser.wait_for_element_loaded("为您的订单付款", By.PARTIAL_LINK_TEXT)
    p = browser.find_element("为您的订单付款", By.PARTIAL_LINK_TEXT)
    p.click()
    time.sleep(10)





