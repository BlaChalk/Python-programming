# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import win32api
import win32file
import os
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import threading
import time


###########################################################################
## Class MainFrame
###########################################################################

class MainFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(676, 466), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWFRAME))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.lblName = wx.StaticText(self, wx.ID_ANY, u"MP3下載", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblName.Wrap(-1)
        self.lblName.SetFont(wx.Font(24, 73, 90, 92, False, "標楷體"))
        self.lblName.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOBK))

        bSizer2.Add(self.lblName, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer1.Add(bSizer2, 1, wx.EXPAND, 5)

        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

        self.lblSongName = wx.StaticText(self, wx.ID_ANY, u"歌手/歌名", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblSongName.Wrap(-1)
        self.lblSongName.SetFont(wx.Font(12, 73, 90, 90, False, "標楷體"))
        self.lblSongName.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizer3.Add(self.lblSongName, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.txtSong = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.txtSong, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.btnSearch = wx.Button(self, wx.ID_ANY, u"搜尋(&S)", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.btnSearch, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer1.Add(bSizer3, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.SHAPED, 5)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        checkListBoxChoices = []
        self.checkListBox = wx.CheckListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, checkListBoxChoices, 0)
        bSizer4.Add(self.checkListBox, 1, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(bSizer4, 5, wx.EXPAND, 5)

        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWFRAME))

        bSizer5.Add(self.m_panel1, 2, wx.EXPAND, 5)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.btnDownload = wx.Button(self, wx.ID_ANY, u"下載(&D)", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.btnDownload, 1, wx.EXPAND, 5)

        bSizer5.Add(bSizer7, 1, 0, 5)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel2.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWFRAME))

        bSizer8.Add(self.m_panel2, 1, wx.ALL | wx.EXPAND, 5)

        self.lblPath = wx.StaticText(self, wx.ID_ANY, u"D:Mp3", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblPath.Wrap(-1)
        self.lblPath.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVEBORDER))

        bSizer8.Add(self.lblPath, 0, wx.ALL, 5)

        self.btnPath = wx.Button(self, wx.ID_ANY, u"儲存目錄(&P)", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.btnPath, 0, 0, 5)

        bSizer5.Add(bSizer8, 2, 0, 5)

        bSizer1.Add(bSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.EXPAND, 5)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.lblStatus = wx.StaticText(self, wx.ID_ANY, u"準備搜尋", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lblStatus.Wrap(-1)
        self.lblStatus.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))

        bSizer6.Add(self.lblStatus, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer1.Add(bSizer6, 0, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        self.Init()


    def __del__(self):
        pass
    def Init(self):
        self.Bind(wx.EVT_BUTTON, self.BtnSearchClick, self.btnSearch)
        self.Bind(wx.EVT_BUTTON, self.BtnDownloadClick, self.btnDownload)
        self.Bind(wx.EVT_BUTTON, self.BtnPathClick, self.btnPath)
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        # 設定快速鍵
        entries = [wx.AcceleratorEntry() for i in range(3)]
        entries[0].Set(wx.ACCEL_ALT, ord('S'), self.btnSearch.GetId())
        entries[1].Set(wx.ACCEL_ALT, ord('D'), self.btnDownload.GetId())
        entries[2].Set(wx.ACCEL_ALT, ord('P'), self.btnPath.GetId())
        table = wx.AcceleratorTable(entries)
        self.SetAcceleratorTable(table)

        # 載入 chromedriver
        opt = Options()
        # opt.add_argument('--headless')
        opt.add_argument('--disable-gpu')
        # opt.add_experimental_option('excludeSwitches', ['enable-loggin'])
        self.web = webdriver.Chrome('chromedriver.exe', options=opt)

        # 選取硬碟
        disk = []
        for i in win32api.GetLogicalDriveStrings().split('\000'):
            if win32file.GetDriveType(i) == 3:
                disk.append(i[:-2])
        # print(disk)
        if not os.path.isdir(self.lblPath.GetLabelText()):
            os.mkdir(self.lblPath.GetLabelText())
        self.lblPath.SetLabelText('{0}:\mp3_tmp'.format(disk[len(disk)-1]))

    def BtnSearchClick(self, event):
        self.checkListBox.Clear()
        self.song = self.txtSong.GetValue() #產生物件變數
        if self.song == '':
            wx.MessageBox('請輸入歌曲名')
            return
        self.lblStatus.SetLabelText('搜尋中...')
        self.Layout()
        t = threading.Thread(target=self.SearchMp3) #啟動新執行緒
        t.start()
    def SearchMp3(self):
        links = {}
        url = "https://www.youtube.com/results?search_query={0}".format(self.song)
        self.web.get(url)
        # print(self.web.page_source)
        tags = self.web.find_elements_by_tag_name('a')
        # print(tags)
        for tag in tags:
            print(tag.get_attribute('href'))
            href = tag.get_attribute('href')
            if str(href).find('watch')!=-1 and str(href).find('list')==-1:
                title = tag.get_attribute('title')
                if title == '':
                    try:
                        t = tag.find_element_by_id('video-title')
                        title = t.get_attribute('title')
                    except:
                        pass
                if title != '':
                    links[title] = '{0} url={1}'.format(title, href)
        if len(links) == 0: return #沒有任何結果
        wx.CallAfter(self.AddList, links) #等待UI主執行緒有空才執行
    def AddList(self, links):
        for key in links.keys():
            self.checkListBox.Append(links[key])
        self.lblStatus.SetLabelText('搜尋完成')
        self.Layout()
    def BtnDownloadClick(self, event):
        self.path = self.lblPath.GetLabelText() # 物件變數
        if self.path == '':
            wx.MessageBox('請選取儲存路徑')
            return
        self.btnDownload.Enable(False)
        self.btnSearch.Enable(False)
        self.btnPath.Enable(False)
        t = threading.Thread(target=self.DownloadMp3, args=(self.checkListBox.GetCheckedStrings(),))
        t.start()
    def DownloadMp3(self, items):
        self.web.command_executor._commands['send_command'] = ('POST', '/session/$sessionId/chromium/send_command') #允許 webdriver 下載檔案
        params = {'cmd':'Page.setDownloadBehavior', 'params':{'behavior':'allow', 'downloadPath':self.path}} #設定預存路徑
        for item in items:
            title = item.split('url=')[0]
            wx.CallAfter(self.DrawUI, '正在下載:{0}'.format(title))
            self.web.get('https://www.youtubeto.com/zh/')
            txt = self.web.find_element_by_id('url')
            txt.send_keys(item.split('url=')[1])
            btn = self.web.find_element_by_id('DownloadMP3_text')
            btn.click()
            command_result = self.web.execute('send_command', params) #傳送允許下載指令並下載儲存到目錄中
            time.sleep(3)
        while self.web.page_source.find('allow-same-origin') == -1: #判定是否下載完成但有時會失效
            time.sleep(0.1)
        wx.CallAfter(self.DrawUI, '下載完成')
        wx.CallAfter(self.DownloadFinished)
    def DrawUI(self, s):
        self.lblStatus.SetLabel(s)
        self.Layout()
    def DownloadFinished(self):
        for i in range(self.checkListBox.GetCount()):
            self.checkListBox.Check(i, check=False)
        self.btnDownload.Enable(True)
        self.btnSearch.Enable(True)
        self.btnPath.Enable(True)
    def BtnPathClick(self, event):
        dlg = wx.DirDialog(self, '選取目錄', style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.lblPath.SetLabelText(dlg.GetPath())
        dlg.Destroy()
    def OnClose(self, event):
        self.web.quit()
        app.ExitMainLoop()



app = wx.App()
frame = MainFrame(None)
frame.Show()
app.MainLoop()



# 寫入資料庫
# cmd = "insert into table (f1, f2, f3) values "
# for in range (1, 100):
#     cmd += "('{0}', '{1}', '{2}'),".format(v1, v2, v3)
# cursor.excute(cmd 