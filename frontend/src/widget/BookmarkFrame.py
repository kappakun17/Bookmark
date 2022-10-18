import tkinter as tk
from frontend.src.widget.Bookmark import my_Bookmark

class my_BookmarkFrame(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        self.bookmarks = [];
        self.BookmarkAddBtnImage = tk.PhotoImage(file="frontend/src/img/bookmark/bookmark_add_btn.png")
        
        tk.Frame.__init__(self, master, cnf, **kw)
        self.configure(bg='#fffdf8')
        self.pack(anchor='e', pady=10)
        
        test = [
            {'title':'figma','url':'https://figma.com', 'memo':'Figmaのホームページです。'},
            {'title':'qiita','url':'https://qiita.com/yaju/items/1575375a126315326fc9', 'memo':'正規表現の書き方。'},
            {'title':'メソッド関数をbuttonから呼び出す方法','url':'https://www.geeksforgeeks.org/how-to-pass-arguments-to-tkinter-button-command/', 'memo':'メソッド関数を呼び出すときは、lamdaで実行することでクリアできるらしい。lamda:○○○'},
            {'title':'Google','url':'https://www.google.com/', 'memo':'Googleのホームページ'},
     
        ]
        
        for bookmark in test:
            bookmark = my_Bookmark(self, bookmark=bookmark)
            self.bookmarks.append(bookmark)
        
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
    