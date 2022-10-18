# library
from logging import root
from sqlite3 import Cursor
# from threading import Thread
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

from frontend.src.widget.frame_left.FrameLeft import my_FrameLeft
from frontend.src.widget.frame_center.FrameCenter import my_FrameCenter
from frontend.src.widget.frame_right.FrameRight import my_FrameRight

from frontend.src.widget.frame_left.ScrolledFrameForLeft import ScrolledFrameForLeft
from frontend.src.widget.frame_center.ScrolledFrameForCenter import ScrolledFrameForCenter
from frontend.src.widget.Logo import my_Logo
from frontend.src.widget.BookmarkTitleBar import my_BookmarkTitleBar

from frontend.src.widget.CategoryAndFoldersFrame import my_CategoryAndFoldersFrame
from frontend.src.utilities.geometory.geometory import getGeometory
from frontend.src.widget.BookmarkFrame import my_BookmarkFrame
from frontend.src.widget.WebviewFrame import my_WebviewFrame
from frontend.src.widget.NoWebview import my_NoWebview
from frontend.src.widget.Webview import my_Webview
# from widget.TitleLabel import display_title_label

from System.Threading import Thread,ApartmentState,ThreadStart

import gc

user32=ctypes.windll.user32

# 高画質に変換するため
# デフォルトでは拡大設定になり、ぼけてしまうそう。
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass


# # アプリケーションFrameの設定
# # the setting for the application Frame
class Application(tk.Frame):

    # 初期配置
    def __init__(self, master=None):
        super().__init__(master)
        
        self.startup();
        
        self.create_widgets()
        
        
        
        
        # create category & folders
        for _ in self.database:
            my_CategoryAndFoldersFrame(self.sf_1.inner_frame)
            
        self.bookmarkFrame = my_BookmarkFrame(self.sf_2.inner_frame)
        
        self.webviewFrame = my_WebviewFrame(self.frame3)
        self.webview = my_NoWebview(self.webviewFrame)
        self.webview.goToEdgeBtn.bind('<Button-1>', self.openWebview)
        
        # self.master.protocol("WM_DELETE_WINDOW", self.quite)
    
            
    def startup(self):
        # test db
        self.database = test_data
        
        # state
        self.webview = None;
        self.current_url_var = tk.StringVar()
        self.current_url_var.set("https://www.bing.com")
        self.data_categoryAndFolders = [self.database];
        self.data_bookmarks = []
        
        # consist of application    
        self.master.geometry("2200x1200")
        self.master.title("ITL Bookmark")
        self.master.configure(
            bg = "#fffdf8"
            )
        self.pack()
        
        # setting
        # over ride: no display horizontal scroll bar
        ScrolledFrame._DEFAULT_SCROLLBARS = "vertical"

        # image instance
        self.bookmarkTitleBarImage = tkinter.PhotoImage(file="frontend/src//img/bookmark/bookmark_title_bar.png")
        self.bookmarkTitleBtnImage = tkinter.PhotoImage(file="frontend/src//img/bookmark/bookmark_title_btn.png")
        
        # style 設定
        self.style = ttk.Style()
        self.style.theme_use('vista')
    
    def create_widgets(self):
        # left frame + scrolledFrame / category & folders 配置
        # center frame + scrolledFrame / bookmarks 配置
        # right frame / webview 配置
        self.frame1 = my_FrameLeft(self.master);
        self.frame2 = my_FrameCenter(self.master);
        self.frame3 = my_FrameRight(self.master)
        
        # logo 配置
        # bookmark title bar 配置
        self.logo =my_Logo(self.frame1)
        self.bookmarkTitleBar = my_BookmarkTitleBar(self.frame2);
        
        # scrolled frame
        #1. for category and folders
        #2. for bookmarks
        self.sf_1 = ScrolledFrameForLeft(self.frame1)
        self.sf_2 = ScrolledFrameForCenter(self.frame2)
    
    
    def openWebview(self, event):
        self.webview.destroy()
        self.webview = my_Webview(self.webviewFrame, self.current_url_var.get())
        
    def openBookmarkUrlToWebview(self, event):
        # self.bookmarkFrame.bookmarks.
        pass
    
    # def quite(self):
    #     self.master.destroy()

    
def main():
    global root
    
    root = Tk();
    
    # initial top screen size
    window_width = 2200
    window_height = 1200
    
    root.title()
    root.geometry(getGeometory(root, window_width, window_height))

    app = Application(master=root);

    # ここで、アプリが動き続ける / アプリを終了するまで
    app.mainloop();
    
    # force - quite for thread
    # メモリを解放してくれる（thread）
    gc.collect()
    
def go():
    
    try:
        main()
    except Exception as err:
        print(err)   
        
        
if __name__ == "__main__":
    # t = Thread(ThreadStart(go))
    # t.ApartmentState = ApartmentState.STA
    # t.Start()
    # t.Join()
    go


