import tkinter as tk


class my_BookmarkMenu(tk.Frame):
    def __init__(self, master=None, title=None, cnf={}, **kw):
        
        self.Dialog_bookmark_fix_btn_image = tk.PhotoImage(file="frontend/src/img/dialog/dialog_bookmark_fix_btn.png")
        self.Dialog_bookmark_add_btn_image = tk.PhotoImage(file="frontend/src/img/dialog/dialog_bookmark_add_btn.png")
        self.Dialog_delete_image = tk.PhotoImage(file='frontend/src/img/dialog/dialog_delete_btn.png')
        
        super().__init__(master, cnf, **kw);
        super().configure(bg='#fffdf8')
        
        bookmark_title = title
        
        self.header_label = tk.Label(self, text=bookmark_title, bg='#6251FA', borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground='#fffdf8', height=2,  font=("HGPｺﾞｼｯｸE", "10", "bold"), foreground='#CACACA')
        self.header_label.pack(fill='x', anchor='ne', pady=(0,20))
        
        self.bookmark_add_btn = tk.Button(self, image=self.Dialog_bookmark_add_btn_image, cursor='hand2', bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground='#fffdf8')
        self.bookmark_add_btn.pack(fill='x', anchor='ne', padx=10,pady=(0,10))
        
        self.bookmark_edit_btn = tk.Button(self, image=self.Dialog_bookmark_fix_btn_image, cursor='hand2', bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground='#fffdf8')
        self.bookmark_edit_btn.pack(fill='x', anchor='ne', padx=10, pady=(0,10))
        
        self.bookmark_delete_btn = tk.Button(self, image=self.Dialog_delete_image,cursor='hand2', bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground='#fffdf8')
        self.bookmark_delete_btn.pack(fill='x', anchor='ne', padx=10, pady=(10,0))
        
        self.pack(padx=0, fill='x')
