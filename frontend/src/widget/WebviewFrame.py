import tkinter as tk

class my_WebviewFrame(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        
        self.GoToEdgeImage = tk.PhotoImage(file='frontend/src/img/webview/goToEdge.png')
        self.GoToEdgeBtnImage = tk.PhotoImage(file='frontend/src/img/webview/goToEdge_btn.png')
        
        tk.Frame.__init__(self, master, cnf, **kw)
        self.configure(bg='#fffdf8')
        
        self.webviewheader = tk.Frame(self, height=80, bg='#6251FA')
        self.webviewheader.pack(anchor='nw', side='top', fill='x', pady=(0,0))
        
        self.webviewheaderside = tk.Frame(self, height=5, bg='#666666')
        self.webviewheaderside.pack(anchor='nw', side='top', fill='x', pady=(0,0))
        
        self.pack(anchor='center',fill='both', expand=True, padx=(0,0), pady=0)

