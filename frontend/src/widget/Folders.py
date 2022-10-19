import tkinter as tk

class my_Folders(tk.Frame):
    def __init__(self, master=None, folders=None, cnf={}, **kw):
        tk.Frame.__init__(self, master, cnf, **kw);
        self.folders = []
        self.json_folders = folders
        
        self.configure(bg = "#fffdf8")
        self.pack(anchor='e', pady=10);
        # self.place(anchor="e")
        
            
    def append_folders(self, folder):
        self.folders.append(folder)
    
    def destory(self):
        self.destroy()