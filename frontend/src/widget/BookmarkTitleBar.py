import tkinter as tk

class my_BookmarkTitleBar(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        self.bookmarkTitleBarImage = tk.PhotoImage(file="frontend/src//img/bookmark/bookmark_title_bar.png")
        self.bookmarkTitleBtnImage = tk.PhotoImage(file="frontend/src//img/bookmark/bookmark_title_btn.png")
        
        tk.Frame.__init__(self, master, cnf, **kw)
        
        self.configure(height=80, bg='#6251FA')
 
        self.pack(anchor='nw', side='top', fill='x', pady=(0,0))
        
        self.l_side = tk.Frame(self.master, height=5, bg='#666666')
        self.l_side.pack(anchor='nw', side='top', fill='x', pady=(0,20))