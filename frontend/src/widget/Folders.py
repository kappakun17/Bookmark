import tkinter as tk
from frontend.src.widget.Folder import my_Folder

class my_Folders(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        tk.Frame.__init__(self, master, cnf, **kw);
        
        self.configure(
            bg = "#fffdf8",

        )
        self.pack(anchor='e', pady=10);
        # self.place(anchor="e")
        for _ in range(5):
            my_Folder(self);
            
    
    def destory(self):
        self.destroy()