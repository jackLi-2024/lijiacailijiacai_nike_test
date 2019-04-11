#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
File:   .py
Author: Lijiacai (v_lijiacai@baidu.com)
Date: 2018-xx-xx
Description:
"""

import json
import os
import sys
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from SpiderTool import Browser
import multiprocessing
import logging

cur_dir = os.path.split(os.path.realpath(__file__))[0]
sys.path.append("%s/" % cur_dir)


def buy(browser=None, url="", size=""):
    try:
        browser.get(url)
        time.sleep(5)
        browser.wait_for_element_loaded("size-grid-button", By.CLASS_NAME)
        sizeEU = browser.find_elements("size-grid-button", By.CLASS_NAME)

        for one in sizeEU:
            try:
                time.sleep(0.5)
                ActionChains(browser.browser).move_to_element(one).perform()
            except:
                pass
            print one.text
            if one.text == size:
                one.click()
                browser.wait_for_element_loaded("cta-btn", By.CLASS_NAME)
                # save_button = browser.find_elements_by_class_name("save-button")[0]
                save_button = browser.find_elements("cta-btn", By.CLASS_NAME)[0]
                # 得到鞋码数
                save_button.click()
                browser.wait_for_element_loaded("cta-btn", By.CLASS_NAME)
                print browser.find_elements("open-close", By.CLASS_NAME)
                # 获取配送地址
                addr = browser.find_elements("open-close", By.CLASS_NAME)[1]
                print "addr", addr
                print addr.text
                time.sleep(2)
                browser.wait_for_element_loaded("payment-provider-btn", By.CLASS_NAME)
                alipay = browser.find_elements("payment-provider-btn", By.CLASS_NAME)[1]
                print alipay
                # 确定支付方式为支付宝
                alipay.click()
                browser.wait_for_element_loaded("save-button", By.CLASS_NAME)
                save_button = browser.find_elements("save-button",By.CLASS_NAME)[1]
                print save_button
                print save_button.text
                save_button.click()
                time.sleep(1)


                browser.wait_for_element_loaded("save-button", By.CLASS_NAME)
                save_button = browser.find_elements("save-button",By.CLASS_NAME)[2]
                print save_button
                print save_button.text
            # 提交订单并排队
                save_button.click()
                time.sleep(10)
    except Exception as e:
        logging.exception(str(e))
