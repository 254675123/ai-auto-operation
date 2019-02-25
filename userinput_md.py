# -*- coding: utf-8 -*-
# pyuserinput使用方法

import pymouse,pykeyboard,os,sys
from pymouse import *
from pykeyboard import PyKeyboard
# 分别定义一个实例
m = PyMouse()
k = PyKeyboard()

# 鼠标操作：
#m.click(x,y,button,n) #–鼠标点击
# x,y –是坐标位置
#buttong –1表示左键，2表示点击右键
#n –点击次数，默认是1次，2表示双击

#m.move(x,y) #–鼠标移动到坐标(x,y)

x_dim, y_dim = m.screen_size() #–获得屏幕尺寸

#键盘操作：

k.type_string('Hello, World!') #–模拟键盘输入字符串
k.press_key('H') #–模拟键盘按H键
k.release_key('H') #–模拟键盘松开H键
k.tap_key('H') #–模拟点击H键
k.tap_key('H',n=2,interval=5) #–模拟点击H键，2次，每次间隔5秒
k.tap_key(k.function_keys[5]) #–点击功能键F5
k.tap_key(k.numpad_keys[5],3) #–点击小键盘5,3次
k.tab_key(k.enter_key) #点击回车键
#联合按键模拟
#例如同时按alt+tab键盘
k.press_key(k.alt_key) #–按住alt键
k.tap_key(k.tab_key) #–点击tab键
k.release_key(k.alt_key) #–松开alt键

# 使用PyUserInput模拟文件上传
# kk = PyKeyboard()
# driver.find_element_by_css_selector( '你的上传文件元素位置').click()
# sleep(1)
# kk.tap_key(kk.shift_key) #切换为英文，看实际情况是否需要
# sleep(1)
# kk.type_string('X:\XXX\Pictures')#打开文件所在目录，方便多个文件上传
# sleep(1)
# kk.tap_key(kk.enter_key)
# sleep(1)
# kk.type_string('"1.png" "2.png" "3.png" ')#多文件上传
# sleep(1)
# kk.tap_key(kk.enter_key)