import wx

class TextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Text Entry Example', size=(300, 100))
        panel = wx.Panel(self, -1) 
        basicText = wx.TextCtrl(panel, -1, "Enter Hero Here", size=(175, -1))
        basicText.SetInsertionPoint(0)
        basicText.AutoComplete(["one", "two", "three"])

app = wx.PySimpleApp()
frame = TextFrame()
frame.Show()
app.MainLoop()

