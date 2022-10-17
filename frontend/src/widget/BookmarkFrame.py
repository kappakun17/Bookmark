import tkinter as tk
from frontend.src.widget.Bookmark import my_Bookmark

class my_BookmarkFrame(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        
        self.BookmarkAddBtnImage = tk.PhotoImage(file="frontend/src/img/bookmark/bookmark_add_btn.png")
        
        tk.Frame.__init__(self, master, cnf, **kw)
        self.configure(
            bg='#fffdf8'
        )
        self.pack(anchor='e', pady=10)
        
        my_Bookmark(self)
        my_Bookmark(self)
        my_Bookmark(self)
        my_Bookmark(self)
        my_Bookmark(self)
        
        
        self.addBtn = tk.Button(
            self,
            image=self.BookmarkAddBtnImage,
            command="",
            cursor='hand2',
            bg='#fffdf8',
            borderwidth = 0,
            highlightthickness = 0,
            relief = "flat",
            activebackground='#fffdf8'
        )
    
        self.addBtn.pack(side='top', pady=(20, 0))
        # self.addBtn.bind('<Button-1>', self.test_category_btn)
    