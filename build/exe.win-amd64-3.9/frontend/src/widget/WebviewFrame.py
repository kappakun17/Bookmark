import tkinter as tk

from frontend.src.widget.Dialogs_MenuBars import my_Dialogs_MenuBars

class my_WebviewFrame(tk.Frame):
    def __init__(self, master=None, cnf={}, DB=None, APP=None, JSON={}, **kw):
        self.db = DB
        self.app = APP
        self.json = JSON
        self.GoToEdgeImage = tk.PhotoImage(file='frontend/src/img/webview/goToEdge.png')
        self.GoToEdgeBtnImage = tk.PhotoImage(file='frontend/src/img/webview/goToEdge_btn.png')
        self.SettingBtnImage = tk.PhotoImage(file='frontend/src/img/webview/setting_btn.png')
        tk.Frame.__init__(self, master, cnf, **kw)
        self.configure(bg='#fffdf8')
        
        self.webviewheader = tk.Frame(self, height=80, bg='#6251FA')
        self.settingsButton = tk.Button(self.webviewheader, image=self.SettingBtnImage, bg="#6251FA", command=lambda: self.open_settings(),cursor='hand2',highlightthickness = 0, borderwidth = 0, relief = "flat",activebackground='#6251FA')
    
        self.settingsButton.pack(side='right', padx=(0,20), pady=(15, 1))
        self.webviewheader.pack(anchor='nw', side='top', fill='x', pady=(0, 0))
        
        self.webviewheaderside = tk.Frame(self, height=5, bg='#666666')
        self.webviewheaderside.pack(anchor='nw', side='top', fill='x', pady=(0,0))
        
        self.pack(anchor='center',fill='both', expand=True, padx=(0,0), pady=0)

    def open_settings(self):
        my_Dialogs_MenuBars(self, DB=self.db, APP=self.app, JSON={
                            'name': 'Settings'}).create_settings_menu()
        pass
