import tkinter as tk


class my_Logo(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        
        self.LogoImage = tk.PhotoImage(file="frontend/src/img/logo/itl_bookmark.png")
        
        tk.Frame.__init__(self, master, cnf, **kw)
        
        self.configure(height=80, bg='#6251FA')
        self.pack(anchor='nw', side='top', fill='x', pady=(0,0))
        
        self.l_side = tk.Frame(self.master, height=5, bg='#666666')
        self.l_side.pack(anchor='nw', side='top', fill='x', pady=(0,20)) 
        
        self.logo = tk.Label(
            self,
            image= self.LogoImage,
            borderwidth=0,
            highlightthickness=0,
            relief='flat',
            bg='#6251FA'
        )
        self.logo.place(x=40, y=20)