import wx

app = wx.App()
frame = wx.Frame(None, title="123", pos=(1000, 200), size=(500, 400))
open_button = wx.Button(frame, label="打开", pos=(50, 200), size=(50, 40))
save_button = wx.Button(frame, label="保存", pos=(100, 200), size=(50, 40))

frame.Show()
app.MainLoop()
