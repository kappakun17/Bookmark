import tkinter as tk

from frontend.src.widget.Category import my_Category

class my_CategoryAndFoldersFrame(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        
        tk.Frame.__init__(self, master, cnf, **kw)
        self.configure(
            bg='#fffdf8'
        )
        self.pack(anchor="e", pady=10);
        
        my_Category(self)    