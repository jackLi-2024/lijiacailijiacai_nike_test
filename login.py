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
from selenium.webdriver.common.by import By
from SpiderTool import Browser
import multiprocessing
import logging

cur_dir = os.path.split(os.path.realpath(__file__))[0]
sys.path.append("%s/" % cur_dir)


def login(browser, username="", password="", url=""):
    """
    :param username: 用户名
    :param password: 密码
    :return:
    """
    # browser = Browser.Browser(browser_type="Chrome", headless=False, timeout=1000)
    # browser = Browser.Browser(browser_type="PhantomJS", headless=False, timeout=100,executable_path="")
    try:
        browser.get(url=url)
        try:
            browser.browser.fullscreen_window()
            browser.wait_for_element_loaded(type_name="g72-menu", elem_type=By.CLASS_NAME)
            menu = browser.find_element("g72-menu", By.CLASS_NAME)
            browser.click_elem(menu)
        except Exception as e:
            logging.exception(str(e))

        browser.wait_for_element_loaded(type_name="join-log-in", elem_type=By.CLASS_NAME)
        join_in_elem = browser.find_element("join-log-in", By.CLASS_NAME)
        browser.click_elem(join_in_elem)
        browser.wait_for_element_loaded(type_name="verifyMobileNumber", elem_type=By.NAME)
        user = browser.find_element("verifyMobileNumber", By.NAME)
        pwd = browser.find_element("password", By.NAME)
        browser.send_keys(user, username)
        browser.send_keys(pwd, password)

        submit = browser.find_element("mobileLoginSubmit", By.CLASS_NAME)
        browser.click_elem(submit)
        browser.wait_for_element_loaded(type_name="test-profile-picture", elem_type= By.CLASS_NAME)
        return {"status": "1", "browser": browser}
    except Exception as e:
        logging.exception(str(e))
        return {"status": "-1","browser": browser}


if __name__ == '__main__':
    browser = Browser.Browser(browser_type="Chrome", headless=False, timeout=1000)
    print login(browser, username="13691926738", password="Ljc19941108",
                url="https://www.nike.com/cn/launch/t/air-max-95-premium-throwback-future/")
    browser.close()
