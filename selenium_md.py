# -*- coding: utf-8 -*-
# selenium 使用方法

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
driver.maximize_window()
ele = driver.find_element_by_id('kw')
ele.send_keys('storm啊')  #输入框第一个方法，输入文字
sleep(2) #这里加等待只是为了让我们看清楚动作
ele.clear() #第二个方法，清除文字
sleep(2)
ele.send_keys('storm啊')
print(ele.get_property('value')) #获得输入框的值
print(ele.get_attribute('name')) #获得name属性值
print(ele.get_attribute('maxlength')) #获得maxlength属性值
print(ele.is_selected()) #输入框是否被选中
print(ele.is_displayed()) #输入框是否可见
print(ele.is_enabled()) #输入框是否可用
print(ele.tag_name) #打印tag name
print(ele.size)  #打印输入框size
sleep(2)
ele.submit() #第三个方法，提交搜索，注意我可没有点搜索按钮
sleep(2)
driver.quit()
