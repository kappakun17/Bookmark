# library
from sqlite3 import Cursor
from threading import Thread
from tkinter import BooleanVar, Frame, PhotoImage,Tk,Button,Entry,Label, Canvas
import tkinter as tk
from tkinter import ttk
import ctypes
import tkinter
from turtle import window_width
from webbrowser import BackgroundBrowser
from PIL import Image, ImageTk
# from widget.ScrollFrame import ScrollableFrame
# from widget.ScrolledFrame import ScrolledFrame
from tkscrolledframe import ScrolledFrame

# module
from testDataBase import test_data
from frontend.src.widget.CategoryAndFoldersFrame import my_CategoryAndFoldersFrame
from frontend.src.plugin.geometory.geometory import getGeometory
from frontend.src.widget.BookmarkFrame import my_BookmarkFrame
# from widget.TitleLabel import display_title_label

# 高画質に変換するため
# デフォルトでは拡大設定になり、ぼけてしまうそう。
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass

import os

ScrolledFrame._DEFAULT_SCROLLBARS = 'vertical'

path = os.getcwd()
print(path)

# # アプリケーションFrameの設定
# # the setting for the application Frame
class Application(tk.Frame):

    def __init__(self, master=None):
       
        super().__init__(master)
       
        # consist of application    
        self.master.geometry("2200x1200")
        self.master.title("ITL Bookmark")
        self.master.configure(
            bg = "#fffdf8"
            )
        self.pack()
        
        # image instance
        self.LogoImage = tkinter.PhotoImage(file="frontend/src/img/logo/itl_bookmark.png")
        self.bookmarkTitleBarImage = tkinter.PhotoImage(file="frontend/src//img/bookmark/bookmark_title_bar.png")
        self.bookmarkTitleBtnImage = tkinter.PhotoImage(file="frontend/src//img/bookmark/bookmark_title_btn.png")
        
        # style
        self.style = ttk.Style()
        self.style.theme_use('vista')
        # self.style.configure("Vertical.TScrollbar", gripcount=0,
        #         background="red", darkcolor="DarkGreen", lightcolor="LightGreen",
        #         troughcolor="gray", bordercolor="blue", arrowcolor="white")
        
        # left frame / category & folders
        self.frame1 = Frame(self.master)
        self.frame1.configure(bg='#fffdf8')
        self.frame1.pack(anchor='nw', fill='y',side='left')
        
        # center frame / bookmarks
        self.frame2 = Frame(self.master)
        self.frame2.configure(bg='#fffdf8')
        self.frame2.pack(anchor='nw', fill='y', side='left', padx=(20, 0))

        # logo
        self.create_logo()
        
        # bookmark title bar
        self.create_bookmarkTitlebar()
        
        # over ride: no display horizontal scroll bar
        ScrolledFrame._DEFAULT_SCROLLBARS = "vertical"

        # scrolled frame
        #1. for category and folders
        self.sf1 = ScrolledFrame(self.frame1, use_ttk=True)
        self.sf1._canvas.configure(bg='#fffdf8')
        self.sf1.config(
                        width=500, 
                        cursor='hand2', 
                        height=self.master.winfo_screenheight(), 
                        bg='#fffdf8', 
                        bd=0,
                        )
        self.sf1.pack()
        
        self.sf1.bind_arrow_keys(self.frame1)
        self.sf1.bind_scroll_wheel(self.frame1)
        self.sf1_inner_frame = self.sf1.display_widget(Frame,fit_width=False,bg='#fffdf8')
        
        #2. for bookmarks
        self.sf2 = ScrolledFrame(self.frame2, use_ttk=True)
        self.sf2._canvas.configure(bg='#fffdf8')
        self.sf2.config(
            width=820, 
            cursor='hand2', 
            height=self.master.winfo_screenheight(), 
            bg='#fffdf8', 
            bd=0,
        )
        self.sf2.pack(anchor='center')
        self.sf2.bind_arrow_keys(self.frame2)
        self.sf2.bind_scroll_wheel(self.frame2)
        self.sf2_inner_frame = self.sf2.display_widget(Frame,fit_width=False,bg='#fffdf8')
        
        

        # db
        self.database = test_data
        
        # create category & folders
        for category in self.database:
            my_CategoryAndFoldersFrame(self.sf1_inner_frame)
            
        my_BookmarkFrame(self.sf2_inner_frame)
                
            
    # Logo表示
    def create_logo(self):
        l = Label(
            self.frame1,
            image= self.LogoImage,
            borderwidth=0,
            highlightthickness=0,
            relief='flat',
            bg='#fffdf8'
        )
        l.pack(pady=(20,20), padx=(20,0))
        
    def create_bookmarkTitlebar(self):
        l = tk.Canvas(
            self.frame2,
            width=761,
            height=63,
            bg="#fffdf8",
            highlightthickness=0,
            relief='ridge',
        )
        l.create_image(0,0, image=self.bookmarkTitleBarImage,anchor='nw')
        l.create_text(40,8, text="test", fill='#ffffff', anchor="nw",font=("HGS創英角ｺﾞｼｯｸUB", "19", "bold"))
        btn = tk.Button(
            self.frame2,
            image=self.bookmarkTitleBtnImage,
            command="",
            cursor="hand2",
            bg='#E893B1',
            borderwidth=0,
            highlightthickness=0,
            relief='flat',
            activebackground='#E893B1'
        ).place(x=710, y=29)
        
        l.pack(pady=(20,10), padx=(10,20), anchor='nw')
        
            

        
        
def main():
    root = Tk();
    
    
    
    # アプリを開いたときの初期画面サイズ 
    window_width = 2200
    window_height = 1200
    # root.update_idletasks()
    root.title()
    root.geometry(getGeometory(root, window_width, window_height))

    app = Application(master=root);

    app.mainloop();

# def go():
#     try:
#         main()
#     except Exception as err:
#         print(err)      
        
if __name__ == "__main__":
    main()



