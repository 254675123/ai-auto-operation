# -*- coding: utf-8 -*-

#可以定位截图在屏幕上的坐标位置。比如，你需要在计算器里输入：1+2=
# 这里需要1和2的识别图

import pyautogui
import time
def pressCaculatorKeys(name):
    x, y = pyautogui.locateCenterOnScreen('./img/{}.png'.format(name))
    pyautogui.click(x, y, interval=0.25)

def caculate(name1, name2, op):
    pressCaculatorKeys(name1)
    pressCaculatorKeys(op)
    pressCaculatorKeys(name2)
    pressCaculatorKeys('equal')

time.sleep(2)
print('start work.')
caculate('1', '2', 'add')