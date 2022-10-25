import tkinter as tk


class my_FolderMenu(tk.Frame):
    def __init__(self, master=None, title=None, cnf={}, **kw):
        
        self.Dialog_folder_rename_btn_image = tk.PhotoImage(file="frontend/src/img/dialog/dialog_folder_rename_btn.png")
        self.Dialog_bookmark_add_btn_image = tk.PhotoImage(file="frontend/src/img/dialog/dialog_bookmark_add_btn.png")
        self.Dialog_delete_image = tk.PhotoImage(file='frontend/src/img/dialog/dialog_delete_btn.png')
        
        super().__init__(master, cnf, **kw);
        super().configure(bg='#fffdf8')
        
        folder_title = title
        
        header_label = tk.Label(self, text=folder_title, bg='#E6E6E6', borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground='#fffdf8', height=2,  font=("HGPｺﾞｼｯｸE", "10", "bold"), foreground='#6251FA')
        header_label.pack(fill='x', anchor='ne', pady=(0,20))
        
        self.folder_rename_btn = tk.Button(self, image=self.Dialog_folder_rename_btn_image, cursor='hand2', bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground='#fffdf8')
        self.folder_rename_btn.pack(fill='x', anchor='ne', padx=10, pady=(0,10))
        
        self.bookmark_add_btn = tk.Button(self, image=self.Dialog_bookmark_add_btn_image, cursor='hand2', bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground='#fffdf8')
        self.bookmark_add_btn.pack(fill='x', anchor='ne', padx=10,pady=(0,10))
        
        self.folder_delete_btn = tk.Button(self, image=self.Dialog_delete_image,cursor='hand2', bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground='#fffdf8')
        self.folder_delete_btn.pack(fill='x', anchor='ne', padx=10, pady=(10,0))
        
        self.pack(padx=0, fill='x')
