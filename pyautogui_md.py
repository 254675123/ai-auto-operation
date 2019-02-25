# -*- coding: utf-8 -*-
# pyautogui 使用方法
#  PyAutoGUI可以模拟鼠标的移动、点击、拖拽，键盘按键输入、按住操作，
# 以及鼠标+键盘的热键同时按住等操作，可以说手能动的都可以。
# Python让生活更简单，人生苦短，Python当歌

"""
PyAutoGUI支持Python 2.x和Python 3.x

Windows：PyAutoGUI没有任何依赖，因为它用Python的ctypes模块所以不需要pywin32
pip3 install pyautogui

OS X：PyAutoGUI需要PyObjC运行AppKit和Quartz模块。这个模块在PyPI上的按住顺序是pyobjc-core和pyobjc
sudo pip3 install pyobjc-core
sudo pip3 install pyobjc
sudo pip3 install pyautogui

Linux：PyAutoGUI需要python-xlib（Python 2）、python3-Xlib（Python 3）
sudo pip3 install python3-xlib
sudo apt-get scrot
sudo apt-get install python-tk
sudo apt-get install python3-dev
sudo pip3 install pyautogui
"""

import pyperclip
import pyautogui

#  PyAutoGUI中文输入需要用粘贴实现
#  Python 2版本的pyperclip提供中文复制
def paste(foo):
    pyperclip.copy(foo)
    pyautogui.hotkey('ctrl', 'v')

def input_cn(text):
    foo = u'学而时习之'
    #foo = text
    #  移动到文本框
    pyautogui.click(130, 30)
    paste(foo)

def screen():
    """
    原点(0,0)在左上角，分别向右、向下增大
    如果屏幕像素是 1920×10801920×1080 ，那么右下角的坐标是(1919, 1079)
    :return: 
    """
    # 当前屏幕的分辨率（宽度和高度）
    screenWidth, screenHeight = pyautogui.size()

    # 鼠标当前位置
    currentMouseX, currentMouseY = pyautogui.position()
    #  (x,y)是否在屏幕上
    x, y = 122, 244
    pyautogui.onScreen(x, y)

def mouseMove():
    """
    坐标系的原点是左上角。X轴（水平）坐标向右增大，Y轴（竖直）坐标向下增大。
    num_seconds = 1.2
    用num_seconds秒的时间把光标移动到(x, y)位置
    pyautogui.moveTo(x, y, duration=num_seconds)
    用num_seconds秒的时间把光标的X轴（水平）坐标移动xOffset，
    Y轴（竖直）坐标向下移动yOffset。
    xOffset, yOffset = 50, 100
    pyautogui.moveRel(xOffset, yOffset, duration=num_seconds)
    :return: 
    """
    screenWidth, screenHeight = pyautogui.size()
    # 让鼠标移到屏幕中央。
    pyautogui.moveTo(screenWidth / 2, screenHeight / 2)

    #  鼠标向下移动10像素, None时，表示不变
    # moveTo()函数会把鼠标光标移动到指定的XY轴坐标处。
    # 如果传入None值，则表示使用当前光标的对象轴坐标值。
    pyautogui.moveTo(100, 200)  # 光标移动到(100, 200)位置
    pyautogui.moveTo(None, 500)  # 光标移动到(100, 500)位置
    pyautogui.moveTo(600, None)  # 光标移动到(600, 500)位置

    # 一般鼠标光标都是瞬间移动到指定的位置，如果你想让鼠标移动的慢点，可以设置持续时间
    # 默认的持续时间pyautogui.MINIMUM_DURATION是0.1秒，如果你设置的时间比默认值还短，那么就会瞬间执行。
    #  用缓动/渐变函数让鼠标2秒后移动到(500,500)位置
    #  use tweening/easing function to move mouse over 2 seconds.
    pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)

    # 如果你想让光标以当前位置为原点，进行相对移动，就用pyautogui.moveRel()函数。
    pyautogui.moveTo(100, 200)  # 把光标移动到(100, 200)位置
    pyautogui.moveRel(0, 50)  # 向下移动50
    pyautogui.moveRel(30, 0, 2)  # 向右移动30
    pyautogui.moveRel(30, None)  # 向右移动30
    pyautogui.moveRel(None, 100)


def mouseMovingPy3():
    # ! python 3
    import pyautogui
    print('Press Ctrl-C to quit')
    try:
        while True:
            x, y = pyautogui.position()
            #positionStr = 'X: {} Y: {}'.format(*[str(x).rjust(4) for x in [x, y]])
            positionStr = 'X: {} Y: {}'.format(x, y)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')

def mouseMovingPy2():
    # ! python
    # import pyautogui, sys
    # print('Press Ctrl-C to quit.')
    # try:
    #     while True:
    #         x, y = pyautogui.position()
    #         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    #         print  positionStr,
    #         print '\b' * (len(positionStr) + 2),
    #         sys.stdout.flush()
    # except KeyboardInterrupt:
    #     print '\n'
    pass

def mouseClick():
    """
    click()函数就是让鼠标点击，默认是单击左键，参数可以设置：
    pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
    其中，button属性可以设置成left，middle和right。
    所有的点击都可以用这个函数，不过下面的函数可读性更好：
    :return: 
    """
    moveToX = 100
    moveToY = 100
    pyautogui.rightClick(x=moveToX, y=moveToY)
    pyautogui.middleClick(x=moveToX, y=moveToY)
    pyautogui.doubleClick(x=moveToX, y=moveToY)
    pyautogui.tripleClick(x=moveToX, y=moveToY)

    # 如果单机之前要先移动，可以把目标的XY坐标值传入函数：
    #  先移动到(100, 200)再单击
    pyautogui.click(x=100, y=200, duration=2)
    # 可以通过button参数设置left，middle和right三个键。例如：
    pyautogui.click(button='right')
    # 要做多次单击可以设置clicks参数，还有interval参数可以设置每次单击之间的时间间隔。例如：
    #  双击左键
    pyautogui.click(clicks=2)
    #  两次单击之间停留0.25秒
    pyautogui.click(clicks=2, interval=0.25)
    #  三击右键
    pyautogui.click(button='right', clicks=2, interval=0.25)

    # 为了操作方便，PyAutoGUI提供了doubleClick()，tripleClick()和rightClick()来实现双击、三击和右击操作。

    # mouseDown()和mouseUp()函数可以实现鼠标按下和鼠标松开的操作。两者参数相同，有x，y和button。例如：
    #  鼠标左键按下再松开
    pyautogui.mouseDown();
    pyautogui.mouseUp()
    #  按下鼠标右键
    pyautogui.mouseDown(button='right')
    #  移动到(100, 200)位置，然后松开鼠标右键
    pyautogui.mouseUp(button='right', x=100, y=200)



def mourseScroll():
    """
    scroll函数控制鼠标滚轮的滚动，amount_to_scroll参数表示滚动的格数。
    正数则页面向上滚动，负数则向下滚动：
    pyautogui.scroll(clicks=amount_to_scroll, x=moveToX, y=moveToY)
    每个按键按下和松开两个事件可以分开处理：
    
    :return: 
    """
    moveToX = 100
    moveToY = 100
    pyautogui.mouseDown(x=moveToX, y=moveToY, button='left')
    pyautogui.mouseUp(x=moveToX, y=moveToY, button='left')

    # 鼠标滚轮滚动可以用scroll()函数和clicks次数参数来模拟。
    # 不同平台上的clicks次数不太一样。还有x和y参数可以在滚动之前定位到(x, y)位置。
    # 例如：
    #  向上滚动10格
    pyautogui.scroll(10)
    #  向下滚动10格
    pyautogui.scroll(-10)
    #  移动到(100, 100)位置再向上滚动10格
    pyautogui.scroll(10, x=100, y=100)

    # 在OS X和Linux平台上，PyAutoGUI还可以用hscroll()实现水平滚动。例如：
    #  向右滚动10格
    pyautogui.hscroll(10)
    #  向左滚动10格
    pyautogui.hscroll(-10)

    # scroll()函数是vscroll()的一个包装（wrapper），执行竖直滚动。

def mouseDrag():
    """
    PyAutoGUI的dragTo()和dragRel()函数与moveTo()和moveRel()函数类似。
    另外，他们有一个button参数可以设置成left，middle和right三个键。例如：
    
    :return: 
    """
    #  按住鼠标左键，把鼠标拖拽到(100, 200)位置
    pyautogui.dragTo(100, 200, button='left')
    #  按住鼠标左键，用2秒钟把鼠标拖拽到(300, 400)位置
    pyautogui.dragTo(300, 400, 2, button='left')
    #  按住鼠标右键，用2秒钟把鼠标拖拽到(30,0)位置
    pyautogui.dragTo(30, 0, 2, button='right')

    distance = 200
    while distance > 0:
        pyautogui.dragRel(distance, 0, duration=0.5)  # 向右
        distance -= 5
        pyautogui.dragRel(0, distance, duration=0.5)  # 向下
        pyautogui.dragRel(-distance, 0, duration=0.5)  # 向左
        distance -= 5
        pyautogui.dragRel(0, -distance, duration=0.5)  # 向上
        break

def mourseTween():
    """
    缓动/渐变函数的作用是让光标的移动更炫。如果你不需要用到的话，你可以忽略这些。
    缓动/渐变函数可以改变光标移动过程的速度和方向。通常鼠标是匀速直线运动，
    这就是线性缓动/渐变函数。PyAutoGUI有30种缓动/渐变函数，可以通过pyautogui.ease*?查看。
    其中，pyautogui.easeInQuad()函数可以用于moveTo()，moveRel()，dragTo()和dragRel()函数，
    光标移动呈现先慢后快的效果，整个过程的时间还是和原来一样。
    而pyautogui.easeOutQuad函数的效果相反：光标开始移动很快，然后慢慢减速。
    pyautogui.easeOutElastic是弹簧效果，首先越过终点，然后再反弹回来。
    例如：
    :return: 
    """
    #  开始很慢，不断加速
    pyautogui.moveTo(100, 100, 2, pyautogui.easeInQuad)
    #  开始很快，不断减速
    pyautogui.moveTo(100, 100, 2, pyautogui.easeOutQuad)
    #  开始和结束都快，中间比较慢
    pyautogui.moveTo(100, 100, 2, pyautogui.easeInOutQuad)
    #  一步一徘徊前进
    pyautogui.moveTo(100, 100, 2, pyautogui.easeInBounce)
    #  徘徊幅度更大，甚至超过起点和终点
    pyautogui.moveTo(100, 100, 2, pyautogui.easeInElastic)
    # 这些效果函数是模仿Al Sweigart的PyTweening模块，可以直接使用，不需要额外安装。
    # 如果你想创建自己的效果，也可以定义一个函数，其参数是(0.0,1.0)，表示起点和终点，返回值是介于[0.0,1.0]之间的数。

def keyboardOp():
    """
    键盘上可以按的键都可以调用
    每次键入的时间间隔: secs_between_keys = 0.1
    pyautogui.typewrite('Hello world!\n', interval=secs_between_keys)
    多个键也可以
    pyautogui.typewrite(['a', 'b', 'c', 'left', 'backspace', 'enter', 'f1'], interval=secs_between_keys)
    :return: 
    """
    #  在每次输入之间暂停0.25秒
    pyautogui.typewrite('Hello world!', interval=0.25)
    # 要按那些功能键，可以用press()函数把pyautogui.KEYBOARD_KEYS里面按键对应的字符串输入进去。
    # 例如：
    #  ENTER键
    pyautogui.press('enter')
    #  F1键
    pyautogui.press('f1')
    #  左方向键
    pyautogui.press('left')
    # esc
    pyautogui.press('esc')
    # press()函数其实是keyDown()和keyUp()函数的包装，模拟的按下然后松开两个动作。
    # 这两个函数可以单独调用。例如，按下shift键的同时按3次左方向键
    #  按下`shift`键
    pyautogui.keyDown('shift')
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('left')
    #  松开`shift`键
    pyautogui.keyUp('shift')

    # 和typewrite()函数一样，可以用数组把一组键传入press()。例如
    pyautogui.press(['left', 'left', 'left'])

    # 然后按着shift+左箭头，选中world! ,下面left有6个，也就是从!位置开始往左移动
    pyautogui.keyDown('shift')
    pyautogui.press(['left', 'left', 'left', 'left', 'left', 'left'])
    pyautogui.keyUp('shift')
    # 多个键也可以
    secs_between_keys = 0.1
    pyautogui.typewrite(['a', 'b', 'c', 'left', 'backspace', 'enter', 'f1'], interval=secs_between_keys)
    # 按键名称列表
    pyautogui.KEYBOARD_KEYS[:10]
    # 结果是：['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&']

    # 键盘的一些热键像Ctrl-S或Ctrl-Shift-1都可以用hotkey()函数来实现
    pyautogui.hotkey('ctrl', 'a')  # 全选
    pyautogui.hotkey('ctrl', 'c')  # 复制
    pyautogui.hotkey('ctrl', 'v')  # 粘贴

    # 每个按键的按下和松开也可以单独调用
    key_name = 'ctrl'
    pyautogui.keyDown(key_name)
    pyautogui.keyUp(key_name)

    pyautogui.hotkey('ctrl', 'shift', 'ese')
    # 等价于：
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')
    pyautogui.keyUp('shift')
    pyautogui.keyUp('ctrl')


def KEYBOARD_KEYS():
    """
    下面就是press()，keyDown()，keyUp()和hotkey()函数可以输入的按键名称：
    ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', 
    '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', 
    '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', 
    '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', 
    '|', '}', '~', 'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 
    'backspace', 'browserback', 'browserfavorites', 'browserforward', 'browserhome', 
    'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear', 'convert', 
    'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete', 'divide', 'down', 'end', 
    'enter', 'esc', 'escape', 'execute', 'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 
    'f16', 'f17', 'f18', 'f19', 'f2', 'f20', 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 
    'f6', 'f7', 'f8', 'f9', 'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 
    'insert', 'junja', 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail', 
    'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack', 'nonconvert', 
    'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9', 'numlock', 
    'pagedown', 'pageup', 'pause', 'pgdn', 'pgup', 'playpause', 'prevtrack', 'print', 
    'printscreen', 'prntscrn', 'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 
    'separator', 'shift', 'shiftleft', 'shiftright', 'sleep', 'stop', 'subtract', 'tab', 'up', 
    'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen', 'command', 
    'option', 'optionleft', 'optionright']
    :return: 
    """
    print(pyautogui.KEYBOARD_KEYS)


def fail_Safes():
    """
    就像《魔法师的学徒》(Sorcerer’s Apprentice)会担水的扫帚，可以担水，
    却无力阻止水漫浴室。你的程序也可能会失控（即使是按照你的意思执行的），
    那时就需要中断。如果鼠标还在自动操作，就很难在程序窗口关闭它。
    为了能够及时中断，PyAutoGUI提供了一个保护措施。当pyautogui.FAILSAFE = True时，
    如果把鼠标光标在屏幕左上角，PyAutoGUI函数就会产生pyautogui.FailSafeException异常。
    如果失控了，需要中断PyAutoGUI函数，就把鼠标光标在屏幕左上角。要禁用这个特性，
    就把FAILSAFE设置成False
    :return: 
    """
    pyautogui.FAILSAFE = False

def pause():
    """
    通过把pyautogui.PAUSE设置成float或int时间（秒），可以为所有的PyAutoGUI函数增加延迟。
    默认延迟时间是0.1秒。在函数循环执行的时候，这样做可以让PyAutoGUI运行的慢一点，非常有用。
    例如：
    :return: 
    """
    pyautogui.PAUSE = 2.5
    pyautogui.moveTo(100, 100)
    pyautogui.click()
    # 所有的PyAutoGUI函数在延迟完成前都处于阻塞状态（block）。
    # （未来计划增加一个可选的非阻塞模式来调用函数。）
    # 建议PAUSE和FAILSAFE一起使用。

def messageForm():
    """
    如果你需要消息弹窗，通过单击OK暂停程序，
    或者向用户显示一些信息，消息弹窗函数就会有类似JavaScript的功能
    :return: 
    """
    pyautogui.alert('这个消息弹窗是文字+OK按钮')
    pyautogui.confirm('这个消息弹窗是文字+OK+Cancel按钮')
    pyautogui.prompt('这个消息弹窗是让用户输入字符串，单击OK')
    # 在prompt()函数中，如果用户什么都不输入，就会返回None。

    # 显示一个简单的带文字和OK按钮的消息弹窗。用户点击后返回button的文字。
    pyautogui.alert(text='', title='', button='OK')
    #  OK和Cancel按钮的消息弹窗
    pyautogui.confirm(text='', title='', buttons=['OK', 'Cancel'])
    #  10个按键0-9的消息弹窗
    pyautogui.confirm(text='', title='', buttons=range(10))

def screenShot():
    """
    PyAutoGUI用Pillow/PIL库实现图片相关的识别和操作。
    在Linux里面，你必须执行sudo apt-get install scrot来使用截屏特性。
    
    :return: 
    """
    # screenshot()函数会返回Image对象（参考Pillow或PIL模块文档），也可以设置文件名
    #  返回一个Pillow/PIL的Image对象
    pyautogui.screenshot()
    pyautogui.screenshot('foo.png')

    im1 = pyautogui.screenshot()
    im1.save('my_screenshot.png')
    # 如果你有一个图片文件想在上面做点击操作，你可以用locateOnScreen()函数来定位。
    #  返回(最左x坐标，最顶y坐标，宽度，高度)
    pyautogui.locateOnScreen('pyautogui/looks.png')
    # 得到 (0, 1040, 48, 40)

    # locateAllOnScreen()函数会寻找所有相似图片，返回一个生成器
    for i in pyautogui.locateAllOnScreen('pyautogui/looks.png'):
        print(i)
    # 得到 (0, 1040, 48, 40)

    list(pyautogui.locateAllOnScreen('pyautogui/looks.png'))
    # 得到 (0, 1040, 48, 40)

    # locateCenterOnScreen()函数会返回图片在屏幕上的中心XY轴坐标值
    pyautogui.locateCenterOnScreen('pyautogui/looks.png')
    # (24, 1060)
    # 如果没找到图片会返回None。
    # 定位比较慢，一般得用1~2秒

    # 在一个 1920×10801920×1080 的屏幕上，screenshot()函数要消耗100微秒——不快也不慢。
    # 如果你不需要截取整个屏幕，还有一个可选的region参数。你可以把截取区域的左上角XY坐标值和宽度、高度传入截取。
    im = pyautogui.screenshot(region=(0, 0, 300, 400))

def gray():
    """
    灰度值匹配
    可以把grayscale参数设置为True来加速定位（大约提升30%），默认为False。
    这种去色（desaturate）方法可以加速定位，但是也可能导致假阳性（false-positive）匹配：
    :return: 
    """
    button7location = pyautogui.locateOnScreen('pyautogui/calc7key.png', grayscale=True)
    button7location

def pixel():
    """
    要获取截屏某个位置的RGB像素值，可以用Image对象的getpixel()方法：
    :return: 
    """
    im = pyautogui.screenshot()
    im.getpixel((100, 200))

    # 也可以用PyAutoGUI的pixel()函数，是之前调用的包装：
    pyautogui.pixel(100, 200)

    # 如果你只是要检验一下指定位置的像素值，可以用pixelMatchesColor()函数，
    # 把X、Y和RGB元组值穿入即可：
    pyautogui.pixelMatchesColor(100, 200, (255, 255, 255))
    # tolerance参数可以指定红、绿、蓝3种颜色误差范围：
    pyautogui.pixelMatchesColor(100, 200, (255, 255, 245), tolerance=10)
