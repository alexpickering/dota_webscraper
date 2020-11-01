import wx

class TextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Text Entry Example', size=(300, 100))
        panel = wx.Panel(self, -1) 
        basicLabel = wx.StaticText(panel, -1, "Basic Control:")
        basicText = wx.TextCtrl(panel, -1, "Enter Hero Here", size=(175, -1))
        basicText.SetInsertionPoint(0)
        basicText.AutoComplete(["one", "two", "three"])

        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        sizer.AddMany([basicLabel, basicText])
        panel.SetSizer(sizer)

app = wx.PySimpleApp()
frame = TextFrame()
frame.Show()
app.MainLoop()

