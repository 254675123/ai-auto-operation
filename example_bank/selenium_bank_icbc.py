# -*- coding: utf-8 -*-

"""
这里自动操作工商银行账号
"""
from selenium import webdriver
from time import sleep

#driver = webdriver.Chrome()
driver = webdriver.Ie()
#driver.get("http://www.icbc.com.cn/icbc/")
#sleep(10)
driver.get("https://mybank.icbc.com.cn/icbc/newperbank/perbank3/frame/frame_index.jsp")
driver.maximize_window()
sleep(10)
ele = driver.find_element_by_id('safeEdit1')
#ele = driver.find_element_by_name('prompttext')

ele.send_keys('123456')  #输入框第一个方法，输入文字
sleep(2) #这里加等待只是为了让我们看清楚动作