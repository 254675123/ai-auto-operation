# -*- coding: utf-8 -*-

"""
这里自动操作工商银行账号
"""

import pyautogui
import time

def pressImageIcon(name, clicks=1):
    """
    点击图片按钮
    :param name: 
    :return: 
    """
    x, y = pyautogui.locateCenterOnScreen('./img/{}.png'.format(name))
    pyautogui.click(x, y, clicks=clicks, interval=0.25)

def inputContent(content):
    """
    在当前位置输入值
    :param content: 
    :return: 
    """
    pyautogui.typewrite(content, interval=0.25)



# print('ready ... ')
# time.sleep(5)
#
# # 打开应用，这里是桌面的图标
# pressImageIcon('icbc_icon', 2)
# time.sleep(10)
# # 点击登录按钮
# pressImageIcon('icbc_login_link')
# time.sleep(10)
#
# # 填写登录账号和密码
# #pressImageIcon('icbc_username_text')
#
# inputContent('9558800200145074817')
# time.sleep(2)
time.sleep(5)
#pressImageIcon('icbc_password_text')
pyautogui.press(['1', 'shift', 'e', 'r'])


time.sleep(5)

# 识别验证码
#pressImageIcon('icbc_validate_code')
# 这里要识别验证码的数字
pyautogui.press('tab')
pyautogui.press(['1', '1', '2'])


time.sleep(2)
# 最后点击登录按钮
#pressImageIcon('icbc_login_button')

time.sleep(2)
print('over')


