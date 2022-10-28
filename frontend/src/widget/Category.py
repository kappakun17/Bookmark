from msilib.schema import CreateFolder
import tkinter as tk
from tkinter import messagebox
from frontend.src.widget.Dialogs_MenuBars import my_Dialogs_MenuBars

import logging
logger = logging.getLogger(__name__)

class my_Category(tk.Canvas):
    def __init__(self, master=None, DB=None, APP=None, JSON=None, cnf={}, **kw):
        
        self.db = DB
        self.app = APP
        self.json = JSON

        print(self.app)


        self.folders_frame = None;
        self.isFolders = tk.BooleanVar();
        self.isFolders.set(False)
        
        self.CategoryImage = tk.PhotoImage(file=f'frontend/src/img/category/category.png');
        self.CategoryBtnImage = tk.PhotoImage(file=f'frontend/src/img/category/category_btn.png');
        
        tk.Canvas.__init__(self, master, cnf, **kw);
        self.configure(width=449,height=60,bg="#fffdf8",highlightthickness=0,relief='ridge')
        self.create_image(0,0, image=self.CategoryImage, anchor='nw')
        self.create_text(40,20, text=self.json['name'], fill='#ffffff', anchor="nw",font=("HGPｺﾞｼｯｸE", "11", "bold"))
        
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
        self.category_btn.bind('<Button-1>', self.open_menuBar)
        self.pack()
        self.config(cursor='hand2')
        
        logger.debug('Create the category widget.')
    
            
    def open_menuBar(self, event):
        self.menu_bar = my_Dialogs_MenuBars(self, DB=self.db, APP=self.app, JSON=self.json).create_category_menu()
        
    def set_folders_frame(self, folders_frame):
        self.folders_frame = folders_frame
        