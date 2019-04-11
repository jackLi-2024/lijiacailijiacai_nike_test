#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# """
# File:   orderUtil.py
# Author: wld
# Date: 2019-xx-xx
# Description:
# """

from config import *
from emailUtil import *
from SpiderTool import Browser
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
import time


class Order(object):

    def __init__(self, browser):
        self.__browser = browser
        self.__browser.get(order_page_url)
        self.__email = Email()

    def getOrderRecords(self):
        self.__browser.wait_for_element_loaded("table-content", elem_type=By.CLASS_NAME)
        order_li_elements = self.__browser.find_elements("order-details-cta", By.CLASS_NAME)
        print(len(order_li_elements))
        if len(order_li_elements) > 0 :

            text = ""
            for order_element in order_li_elements:
                print order_element.get_attribute("text()")
                if order_element.get_attribute("data-status-code") == "1001":
                    continue
                sub_elements = order_element.find_elements_by_xpath("./*")
                a = order_element.find_element_by_xpath(".//a")
                for index, element in enumerate(sub_elements):
                    if index == len(sub_elements) -1:
                        href = a.get_attribute("href")
                        text = text + href + "\n"
                    else:
                        text = text + element.text + " "
            print(text)
            if text:
                self.__email.appendText(text)
                self.__email.sendEmail()
                return 1




