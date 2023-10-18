import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        super(MyFrame, self).__init__(parent, id, title, size=(600, 400))
        
        # 创建一个主面板
        panel = wx.Panel(self)
        
        # 设置整体面板的背景颜色为普鲁士蓝
        panel.SetBackgroundColour(wx.Colour(0, 49, 83))  # 普鲁士蓝
        
        # 创建垂直BoxSizer来组织界面元素
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # 创建标题并添加到主Sizer
        title = wx.StaticText(panel, label="MAMA-Delight-BaseDemo", style=wx.ALIGN_LEFT)
        title.SetForegroundColour(wx.Colour(255, 255, 255))  # 橙色
        font = wx.Font(32, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        title.SetFont(font)
        main_sizer.Add(title, 0, wx.ALL | wx.EXPAND, 5)
        
        # 创建水平BoxSizer来组织按钮和图片
        content_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # 创建左侧的垂直BoxSizer
        left_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # 创建五个按钮并添加到左侧Sizer
        for i in range(5):
            button = wx.Button(panel, label=f"Button {i+1}")
            # 设置按钮的默认背景颜色为稍微深一些的普鲁士蓝
            button_color = wx.Colour(0, 39, 73)  # 偏深色的普鲁士蓝
            button.SetBackgroundColour(button_color)
            button.SetForegroundColour(wx.Colour(255, 160, 0))  # 橙色
            font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
            button.SetFont(font)
            left_sizer.Add(button, 0, wx.ALL | wx.EXPAND, 5)
        
        # 创建右侧的静态图片
        image = wx.Image("path_to_your_image.jpg", wx.BITMAP_TYPE_ANY)
        image = image.Scale(300, 300, wx.IMAGE_QUALITY_HIGH)
        image = image.ConvertToBitmap()
        static_bitmap = wx.StaticBitmap(panel, -1, image)
        
        # 将左侧和右侧添加到水平Sizer
        content_sizer.Add(left_sizer, 1, wx.ALL | wx.EXPAND, 5)
        content_sizer.Add(static_bitmap, 1, wx.ALL | wx.EXPAND, 5)
        
        # 将水平Sizer添加到主Sizer
        main_sizer.Add(content_sizer, 1, wx.ALL | wx.EXPAND, 5)
        
        # 设置主Sizer为面板的Sizer
        panel.SetSizer(main_sizer)

        self.Centre()
        self.Show()

app = wx.App()
MyFrame(None, -1, 'Prussian Blue GUI with Title, Buttons, and Image')
app.MainLoop()
