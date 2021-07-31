import wx
import wx.adv

import utils
from data import data

app = wx.App()
mainFrame = wx.Frame(None, title="自动点检", pos=(80, 50), size=(1000, 500))


def findPanel(panelName):
    for i in range(0, len(mainFrame.Children)):
        if mainFrame.Children[i].GetName() == panelName:
            return i


def buttonInit():
    cpu = data(1, 'cpu', 7, [1, 3, 4, 5, 6, 7])
    cpuSave = wx.Button(mainFrame, label="CPU报表点检", pos=(50, 50), size=(150, 40))
    cpuSave.Bind(wx.EVT_BUTTON, cpu.save_OnClick)

    ram = data(2, 'ram', 8, [1, 3, 4, 5, 8])
    ramSave = wx.Button(mainFrame, label="RAM报表点检", pos=(50, 100), size=(150, 40))
    ramSave.Bind(wx.EVT_BUTTON, ram.save_OnClick)

    disk = data(3, 'disk', 9, [0, 2, 3, 4, 6])
    diskSave = wx.Button(mainFrame, label="磁盘报表点检", pos=(50, 150), size=(150, 40))
    diskSave.Bind(wx.EVT_BUTTON, disk.save_OnClick)

    linuxLoad = data(4, 'linuxLoad', 10, [1, 3, 4, 5, 8, 11])
    linuxLoadSave = wx.Button(mainFrame, label="linux负载报表点检", pos=(50, 200), size=(150, 40))
    linuxLoadSave.Bind(wx.EVT_BUTTON, linuxLoad.save_OnClick)

    DBIncrease = data(5, 'DBIncrease', 11, [0, 1, 3, 7, 8])
    DBIncreaseSave = wx.Button(mainFrame, label="数据库大小增长报表点检", pos=(50, 250), size=(150, 40))
    # DBIncreaseSave.Bind(wx.EVT_BUTTON, DBIncrease.save_OnClick)

    tableSpaceIncrease = data(6, 'tableSpaceIncrease', 14, [1, 2, 3, 7, 8])
    tableSpaceIncreaseSave = wx.Button(mainFrame, label="表空间增长报表点检", pos=(50, 300), size=(150, 40))
    tableSpaceIncreaseSave.Bind(wx.EVT_BUTTON, tableSpaceIncrease.save_OnClick)

    tableSpaceUsage = data(7, 'tableSpaceUsage', 15, [1, 2, 4, 6, 7])
    tableSpaceUsageSave = wx.Button(mainFrame, label="表空间使用率报表点检", pos=(50, 350), size=(150, 40))
    tableSpaceUsageSave.Bind(wx.EVT_BUTTON, tableSpaceUsage.save_OnClick)


def textInit():
    utils.jIdInput = wx.TextCtrl(mainFrame, id=1, name="jId", pos=(300, 50), size=(150, 40), value="")
    utils.startDateInput = wx.adv.DatePickerCtrl(mainFrame, id=2, name='startDate', pos=(300, 100), size=(150, 40),
                                                 style=2)
    utils.startTimeInput = wx.adv.TimePickerCtrl(mainFrame, id=5, name='startTime', pos=(500, 100), size=(150, 40),
                                                 style=2)
    utils.endDateInput = wx.adv.DatePickerCtrl(mainFrame, id=3, name="endDate", pos=(300, 150), size=(150, 40), style=2)
    utils.endTimeInput = wx.adv.TimePickerCtrl(mainFrame, id=6, name="endTime", pos=(500, 150), size=(150, 40), style=2)

    utils.selectTimeInput = wx.TextCtrl(mainFrame, id=4, name="selectTime", pos=(700, 100), size=(100, 20),
                                        value="间隔时间默认=6")

    utils.bigTextBox = wx.TextCtrl(mainFrame, id=5, name="bigTextBox", pos=(300, 200), size=(550, 200), value="这里显示数据",
                                   style=wx.TE_MULTILINE)
