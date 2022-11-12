import tkinter as tk

class my_FrameLeft(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        tk.Frame.__init__(self, master, cnf, **kw)
        
        self.configure(bg='#fffdf8')
        self.pack(anchor='nw', fill='y',side='left')
        