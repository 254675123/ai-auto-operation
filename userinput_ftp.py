from pywinauto import application

def operateftptools(begindate,enddate):

    dirs = u"E:/Ftp.exe" #应用所在路径

    app = application.Application()
    app.start(dirs) #开始一个进程
    ftptool = app.window_(found_index = 0) #获取Ftp.exe的主窗口
    ftptool.window_(found_index = 7).TypeKeys(begindate)#发送快捷键，index 7是开始时间文本框
    ftptool.window_(found_index = 9).TypeKeys(enddate)#发送快捷键，index 9是结束时间文本框
    ftptool.window_(found_index = 3).Click() #index 3 is find data查询数据
    findresult=ftptool.child_window(found_index = 0,class_name = "Button", title = u"确定") #弹出子窗口，查询完成，点击确定  
    findresult.wait('exists',10000) #如果数据太多，需要把10000改大些   
    print('the end of finding-data')
    ftptool.child_window(found_index = 0,class_name = "Button", title = u"确定").DoubleClick()

    app.connect(path = dirs)#连接一个已经打开的进程
    ftptool = app.window_(found_index = 0) #回到主窗口句柄 
    ftptool.Window_(found_index = 0,class_name = "Button", title = u"保存CSV").Click()#点击保存CSV按钮
    ftptool.child_window(found_index = 0,class_name = "Button", title = u"确定").DoubleClick()#保存csv后弹出子窗口，点击确定，csv文件自动保存到Ftp.exe所在文件夹
    ftptool.close() #关闭Ftp.exe应用
    print("export blackbox-data successfully")
