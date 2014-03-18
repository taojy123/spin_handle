#Boa:Frame:Frame1

import wx
import os
import random
import shutil

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON2, wxID_FRAME1BUTTON3, 
 wxID_FRAME1PANEL1, wxID_FRAME1RADIOBUTTON1, wxID_FRAME1RADIOBUTTON2, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, 
 wxID_FRAME1STATICTEXT4, wxID_FRAME1TEXTCTRL1, wxID_FRAME1TEXTCTRL2, 
] = [wx.NewId() for _init_ctrls in range(13)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(752, 366), size=wx.Size(396, 363),
              style=wx.DEFAULT_FRAME_STYLE, title='spin_handle')
        self.SetClientSize(wx.Size(380, 325))
        self.SetToolTipString('')

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(380, 325),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetToolTipString('')

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label='Title',
              name='button1', parent=self.panel1, pos=wx.Point(72, 24),
              size=wx.Size(75, 24), style=0)
        self.button1.SetToolTipString('')
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2, label='Txt',
              name='button2', parent=self.panel1, pos=wx.Point(72, 64),
              size=wx.Size(75, 24), style=0)
        self.button2.SetToolTipString('')
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAME1BUTTON2)

        self.radioButton1 = wx.RadioButton(id=wxID_FRAME1RADIOBUTTON1,
              label='LineByLine', name='radioButton1', parent=self.panel1,
              pos=wx.Point(80, 120), size=wx.Size(91, 14), style=0)
        self.radioButton1.SetValue(True)

        self.radioButton2 = wx.RadioButton(id=wxID_FRAME1RADIOBUTTON2,
              label='Random', name='radioButton2', parent=self.panel1,
              pos=wx.Point(192, 120), size=wx.Size(91, 14), style=0)
        self.radioButton2.SetValue(False)

        self.button3 = wx.Button(id=wxID_FRAME1BUTTON3, label='Run',
              name='button3', parent=self.panel1, pos=wx.Point(72, 256),
              size=wx.Size(75, 24), style=0)
        self.button3.SetToolTipString('')
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_FRAME1BUTTON3)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1, label='-',
              name='staticText1', parent=self.panel1, pos=wx.Point(160, 32),
              size=wx.Size(4, 14), style=0)
        self.staticText1.SetToolTipString('')

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2, label='-',
              name='staticText2', parent=self.panel1, pos=wx.Point(160, 64),
              size=wx.Size(4, 14), style=0)
        self.staticText2.SetToolTipString('')

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label='Lines number', name='staticText3', parent=self.panel1,
              pos=wx.Point(80, 176), size=wx.Size(73, 14), style=0)
        self.staticText3.SetToolTipString('')

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label='Files number', name='staticText4', parent=self.panel1,
              pos=wx.Point(80, 208), size=wx.Size(68, 14), style=0)
        self.staticText4.SetToolTipString('')

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self.panel1, pos=wx.Point(184, 176), size=wx.Size(100, 22),
              style=0, value='5')
        self.textCtrl1.SetToolTipString('')

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2, name='textCtrl2',
              parent=self.panel1, pos=wx.Point(184, 208), size=wx.Size(100, 22),
              style=0, value='5')
        self.textCtrl2.SetToolTipString('')

    def __init__(self, parent):
        self._init_ctrls(parent)
        if not os.path.exists('output'):
            os.makedirs('output')
        if not os.path.exists('txts'):
            os.makedirs('txts')

    def OnButton1Button(self, event):
    
        wildcard = "TXT (*.txt)|*.txt|"   \
                   "All files (*.*)|*.*"
        dlg = wx.FileDialog(
            self, 
            message="Chose the title file",
            defaultDir=os.getcwd(), 
            defaultFile="",
            wildcard=wildcard,
            style=wx.OPEN
            )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.staticText1.SetLabel(path)
        dlg.Destroy()
        
        event.Skip()

    def OnButton2Button(self, event):
        
        dlg = wx.DirDialog(self, 
        "Choose the directory of txts:",
        defaultPath=os.getcwd(),
        style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            dir=dlg.GetPath()
            self.staticText2.SetLabel(dir)
        dlg.Destroy()
            
        event.Skip()



    def OnButton3Button(self, event):
        
        path = self.staticText1.GetLabel()
        dir = self.staticText2.GetLabel()
        
        if len(path) < 3 or len(dir) < 3:
            wx.MessageBox("Choose the title and txt files first!")
            event.Skip()
            return
            
        order = self.radioButton1.GetValue()
        lnum = int(self.textCtrl1.GetValue())
        fnum = int(self.textCtrl2.GetValue())

        
        titles = open(path).readlines()
        txts = os.listdir(dir)
        
        try:
            for i in range(fnum):
                f = open("output/"+str(i)+".csv", "w")
                for j in range(lnum):
                    if order:
                        title = titles[j%len(titles)]
                    else:
                        title = random.choice(titles)
                    title = title.strip().replace(",",  "").replace("\xef\xbb\xbf", "")
                    name = txts.pop()
                    txt = open(dir + "/" + name).read()
                    txt = txt.strip().replace("\r", "").replace("\xef\xbb\xbf", "")
                    print [txt]
                    txt = "<p>" + txt + "</p>"
                    txt = txt.replace("\n", "</p><p>").replace('"', '""')
                    txt = txt.replace("<p></p>", "")
                    f.write('%s,"%s"\n'%(title, txt))
                    
                    shutil.move(dir + "/" + name, "txts/" + name)
                f.close()
                
            wx.MessageBox("Finish!")
        except:
            wx.MessageBox("Error!")
            
        event.Skip()
