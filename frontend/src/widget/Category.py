from msilib.schema import CreateFolder
import tkinter as tk
from tkinter import messagebox
from frontend.src.widget.Folders import my_Folders
from frontend.src.widget.ModalDialogSampleApp import ModalDialogSampleApp
from frontend.src.widget.dialog.dialog import MyDialog
class my_Category(tk.Canvas):
    def __init__(self, master=None, cnf={}, **kw) -> None:
        
        # foldersを作るときに登録
        self.folders = None;
        self.isFolders = tk.BooleanVar(False);
        
        # my_Categoryで使う画像
        self.CategoryImage = tk.PhotoImage(file=f'frontend/src/img/category/category.png');
        self.CategoryBtnImage = tk.PhotoImage(file=f'frontend/src/img/category/category_btn.png');
        
        tk.Canvas.__init__(self, master, cnf, **kw);
        self.configure(
            width=449,
            height=60,
            bg="#fffdf8",
            highlightthickness=0,
            relief='ridge',
        )
        
        self.create_image(0,0, image=self.CategoryImage, anchor='nw')
        self.create_text(40,20, text="test", fill='#ffffff', anchor="nw",font=("MSゴシック", "11", "bold"))
        
        self.category_btn = tk.Button(
            self,
            image=self.CategoryBtnImage,
            command="",
            cursor='hand2',
            bg='#E893B1',
            borderwidth = 0,
            highlightthickness = 0,
            relief = "flat",
            activebackground='#E893B1'
            )
        self.category_btn.place(x=400,y=30)
        self.category_btn.bind('<Button-1>', self.test_category_btn)
        self.pack()
        self.config(cursor='hand2')
        self.bind('<Button-1>', self.test_category)
        
    
        
    def test_category(self, event):
        # True -> folders非表示
        if self.isFolders.get():
            self.folders.destory()
            self.isFolders.set(False)            

        # False -> folders表示
        else:
            self.createFolders(self.master)
            self.isFolders.set(True)
            
    def test_category_btn(self, event):
        ModalDialogSampleApp(self).create_modal_dialog()
        # MyDialog(self)
        self.update_idletasks()
        
        pass
            
        
    def createFolders(self, master):
        self.folders = my_Folders(master)