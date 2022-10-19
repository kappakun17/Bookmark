import tkinter as tk

class my_BookmarkFrame(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        
        tk.Frame.__init__(self, master, cnf, **kw)
        self.configure(bg='#fffdf8')
        self.pack(anchor='e', pady=10)
        
        # self.addBtn.bind('<Button-1>', self.test_category_btn)
    