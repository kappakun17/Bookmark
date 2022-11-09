# library
from concurrent.futures import ProcessPoolExecutor
import os
from sqlite3 import Cursor
# tk
import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import BooleanVar, Frame, PhotoImage,Tk,Button,Entry,Label, Canvas
from winreg import LoadKey
from tkscrolledframe import ScrolledFrame

from concurrent.futures.thread import ThreadPoolExecutor

import json
import gc
import ctypes
from functools import partial
from PIL import Image, ImageTk

import logging

# module
# backend
from backend.database import Database

from test_front import test_data

# frontend
from frontend.src.widget.frame_left.FrameLeft import my_FrameLeft
from frontend.src.widget.frame_center.FrameCenter import my_FrameCenter
from frontend.src.widget.frame_right.FrameRight import my_FrameRight

from frontend.src.widget.frame_left.ScrolledFrameForLeft import ScrolledFrameForLeft
from frontend.src.widget.frame_center.ScrolledFrameForCenter import ScrolledFrameForCenter
from frontend.src.widget.Logo import my_Logo
from frontend.src.widget.BookmarkTitleBar import my_BookmarkTitleBar

from frontend.src.widget.CategoryAndFoldersFrame import my_CategoryAndFoldersFrame
from frontend.src.widget.Category import my_Category
from frontend.src.utilities.geometory.geometory import getGeometory
from frontend.src.widget.Folders import my_Folders
from frontend.src.widget.Folder import my_Folder
from frontend.src.widget.BookmarkFrame import my_BookmarkFrame
from frontend.src.widget.Bookmark import my_Bookmark
from frontend.src.widget.WebviewFrame import my_WebviewFrame
from frontend.src.widget.NoWebview import my_NoWebview
from frontend.src.widget.Webview import my_Webview
from frontend.src.widget.GitPlayer import TkGif
from frontend.src.widget.Dialogs_Actions import my_Dialogs_Actions
# from widget.TitleLabel import display_title_label


user32=ctypes.windll.user32

# 高画質に変換するため
# デフォルトでは拡大設定になり、ぼけてしまうそう。
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass

# ログの設定
ITL_BOOKMARK_LOG = 'debug'

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter =logging.Formatter('%(levelname)s %(asctime)s [%(name)s] %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

log_level = logging.DEBUG if ITL_BOOKMARK_LOG == 'debug' else logging.INFO
logger.setLevel(log_level)

# # アプリケーションFrameの設定
# # the setting for the application Frame
class Application(tk.Frame):

    # 初期配置
    def __init__(self, master=None):
        super().__init__(master)
        
        self.startup();
        
        
        loading = self.run_loading()
        self.after(5000,loading.destroy)
        self.after(5050,self.create_widgets)
        
        # self.master.protocol("WM_DELETE_WINDOW", self.quite)
        logger.debug('Compleated to initial running the app.')
            
    def startup(self):
        print(self)
        # db
        self.db = self.start_db()
        
        # state
        self.categoryAndFolders = None
        self.webview = None;
        
        self.loading_path = './frontend/src/img/loading/loading.gif'
        
        self.current_url_var = tk.StringVar()
        self.current_url_var.set("https://www.bing.com")
        
        self.set_JsonCategoryAndFolders()
        logger.debug('json data: {}'.format(self.json_categoryAndFolders))
        
         
        self.folder_key_var = tk.IntVar()
        self.folder_key_var.set(1);
        self.set_JsonBookmarks()
        logger.debug('json data: {}'.format(self.json_bookmarks))
        
        # image instance
        self.bookmarkTitleBarImage = tkinter.PhotoImage(file="frontend/src//img/bookmark/bookmark_title_bar.png")
        self.bookmarkTitleBtnImage = tkinter.PhotoImage(file="frontend/src//img/bookmark/bookmark_title_btn.png")
        self.CategoryAddBtnImage = tk.PhotoImage(file='frontend/src/img/category/category_add_btn.png')
        self.BookmarkAddBtnImage = tk.PhotoImage(file="frontend/src/img/bookmark/bookmark_add_btn.png")
        # style 設定
        self.style = ttk.Style()
        self.style.theme_use('vista')
    
        # setting
        # over ride: no display horizontal scroll bar
        ScrolledFrame._DEFAULT_SCROLLBARS = "vertical"
        logger.debug('Successed run the startup func.')
        
        # consist of application
        self.master.geometry("2700x1200")
        self.master.title("ITL Bookmark")
        self.master.configure(bg = "#fffdf8")
        self.pack()
        logger.debug('Created the window.')

        # introduction dialog
        self.show_introduction()
        
    def start_db(self):
        db = Database()
        db.rebuildDB()
        db.consistOfDB()
        test_data(db)
        
        logger.debug('Successed to consist of db.')
        return db
    
    def create_widgets(self):
        
        
        
        # each frame widget
        self.frame1 = my_FrameLeft(self.master);
        self.frame2 = my_FrameCenter(self.master);
        self.frame3 = my_FrameRight(self.master)
        logger.debug('Created the main 3 frames.')
        
        # logo / bookmark title bar
        self.logo =my_Logo(self.frame1)
        self.bookmarkTitleBar = my_BookmarkTitleBar(self.frame2);
        logger.debug('Created the Logo and Bookmark Title Bar.')
        
        # scrolled frame
        self.sf_1 = ScrolledFrameForLeft(self.frame1)
        self.sf_2 = ScrolledFrameForCenter(self.frame2)
        logger.debug('Created the 2 scrolled frame.')
        
        # 並列処理
        with ThreadPoolExecutor(max_workers=20) as executor:
            executor.submit(self.render_categoryAndFolders())
            executor.submit(self.render_bookmarks())
            executor.submit(self.render_Webview())
        
        logger.debug('Successed to create the widgets.')
        
    def create_category_and_folders(self):
        # create category & folders
        self.categoryAndFolders = []
        self.set_JsonCategoryAndFolders()

        for category in self.json_categoryAndFolders:
            cf = my_CategoryAndFoldersFrame(self.sf_1.inner_frame, category=category)
            self.categoryAndFolders.append(cf)
        print('test')    
        self.create_category()
        print('test')
        self.create_folders_frame()
        print('test')
        self.create_folder()
        
        self.addCategoryBtn = tk.Button(
            self.sf_1.inner_frame,
            image=self.CategoryAddBtnImage,
            command="",
            cursor='hand2',
            bg='#fffdf8',
            borderwidth = 0,
            highlightthickness = 0,
            relief = "flat",
            activebackground='#fffdf8'
        )
    
        self.addCategoryBtn.pack(side='top', pady=(20, 0))
        self.addCategoryBtn.configure(command=lambda:self.call_my_dialogs_Action_add_category())
        logger.debug('Successed to create the bookmarks.')
        

    def create_category(self):
        category = self.json_categoryAndFolders
        for i, cf in enumerate(self.categoryAndFolders):
            category_obj = my_Category(cf, DB=self.db, APP=self, JSON=category[i],)
            category_obj.bind('<Button-1>', partial(self.toggle_categoryBtn, category = category_obj))
            cf.set_category(category_obj)
            print('testf')
            
    def create_folders_frame(self):
        for cf in self.categoryAndFolders:
            cf.category.set_folders_frame(my_Folders(cf))
        
    def create_folder(self):
        category = self.json_categoryAndFolders
        for i, cf in enumerate(self.categoryAndFolders):
            for j ,folders in enumerate(category[i]['folders']):
                print(folders)
                folder_obj = my_Folder(cf.category.folders_frame,DB=self.db, APP=self, JSON=category[i]['folders'][j])
                folder_obj.bind('<Button-1>', partial(self.re_render_bookmarks,folder_key=folder_obj.id_var.get()))
                cf.category.folders_frame.append_folders(folder_obj)
        
    def create_bookmarks(self):
        self.set_JsonBookmarks()
        for bookmark in self.json_bookmarks:
            bm = my_Bookmark(self.sf_2.inner_frame, DB=self.db, APP=self, JSON=bookmark)
            bm.view_btn.configure(command=partial(self.re_render_Webview, url=bookmark['url']))
            
            bm.browser_btn.bind("<Enter>", partial(bm.display_description,desc=bm.desc_browser, x=505, y=5))
            bm.browser_btn.bind("<Leave>", partial(bm.no_display_description, desc=bm.desc_browser))
            
            bm.copy_link_btn.bind("<Enter>", partial(bm.display_description, desc=bm.desc_copyLink, x=570, y=5))
            bm.copy_link_btn.bind("<Leave>", partial(bm.no_display_description, desc=bm.desc_copyLink))
            bm.copy_link_btn.bind("<Button-1>", partial(bm.alert_description,off_desc=bm.desc_copyLink, on_desc=bm.desc_copiedLink, x=570, y=0))
            
            bm.view_btn.bind("<Enter>", partial(bm.display_description,desc=bm.desc_webview, x=635, y=5))
            bm.view_btn.bind("<Leave>", partial(bm.no_display_description, desc=bm.desc_webview))
        
        logger.debug("Created the Bookmarks widget.")
        
        self.addBookmarksBtn = tk.Button(
            self.sf_2.inner_frame,
            image=self.BookmarkAddBtnImage,
            command="",
            cursor='hand2',
            bg='#fffdf8',
            borderwidth = 0,
            highlightthickness = 0,
            relief = "flat",
            activebackground='#fffdf8'
        )
    
        self.addBookmarksBtn.pack(side='top', pady=(20, 0))
        self.addBookmarksBtn.configure(command=lambda:self.call_my_Dialogs_Action_add_bookmark())
        logger.debug('Successed to create the bookmarks.')
    
    def create_Webview(self):
        self.webviewFrame = my_WebviewFrame(
            self.frame3, DB=self.db, APP=self)
        self.webview = my_NoWebview(self.webviewFrame)
        self.webview.goToEdgeBtn.bind('<Button-1>', self.re_render_Webview)
        
    def toggle_categoryBtn(self, event, category):
        print(category.isFolders.get())
        if category.isFolders.get():
            category.folders_frame.pack(anchor='e', pady=10)
            category.isFolders.set(False)         
        else:
            category.folders_frame.pack_forget()
            category.isFolders.set(True)  
            
    
    def render_categoryAndFolders(self):
        self.create_category_and_folders()
    
    def render_bookmarks(self):
        self.create_bookmarks()
        
    def render_Webview(self,):
        self.create_Webview()
    
    def re_render_categoryAndFolders(self):
        categoryAndoFolders = self.sf_1.inner_frame.winfo_children()
        for cf in categoryAndoFolders:
            cf.destroy()
        time.sleep(4)
        self.render_categoryAndFolders()
        
    
    def re_render_bookmarks(self,event=None, folder_key=None, is_force_reload=False):
        if not is_force_reload:
            if folder_key == self.folder_key_var.get(): return
        
        bookmarks = self.sf_2.inner_frame.winfo_children()
        for bookmark in bookmarks:
            bookmark.destroy()
            
        self.addBookmarksBtn.destroy()
        print(folder_key)
        self.folder_key_var.set(folder_key);
        print(str(self.folder_key_var.get()))
        self.render_bookmarks()
    
    def re_render_Webview(self,event=None, url=None):
        self.webview.destroy()
        URL = url if url else self.current_url_var.get()
        self.webview = my_Webview(self.webviewFrame, url=URL)
        logger.debug('Successed to update the webview screen.')
    
    def call_my_dialogs_Action_add_category(self):
        json = {
            'name':'新規登録',
        }
        my_Dialogs_Actions(master=self, key='category', action='add', DB=self.db, APP=self, JSON=json)
        
    
    def call_my_Dialogs_Action_add_bookmark(self):
        json = {
            'name':'新規追加',
            'id':self.folder_key_var.get()
        }
        my_Dialogs_Actions(master=self, key='bookmark', action='add', DB=self.db, APP=self, JSON=json)
    
    def set_JsonCategoryAndFolders(self):
        self.json_categoryAndFolders = json.loads(self.db.select_all_categorys_and_folders())
        print(self.json_categoryAndFolders)

    def set_JsonBookmarks(self):
        folder_key = self.folder_key_var.get()
        self.json_bookmarks = json.loads(self.db.select_relate_folder_bookmark(folder_key));
        
    def run_loading(self):
        # initial top screen size
        self.master.configure( bg='#FCFCFF')
        main_frame = tk.Frame(self.master, bg='#FCFCFF')
        main_frame.pack(fill='both', anchor='center', pady=400)

        label = tk.Label(main_frame, borderwidth=0, bg='#FCFCFF')
        label.pack()
        
        gif_player = TkGif(self.loading_path, label)
        gif_player.play()
        
        return main_frame

    def show_introduction(self):
        if self.db.get_setting('hide_introduction'):
            return

        json = {
            'name':'"ITL Bookmark" の説明',
        }
        return my_Dialogs_Actions(master = self, key='introduction', action='introduction', DB=self.db, APP=self, JSON=json)


import time    
def main():
    root = Tk();
    # initial top screen size
    window_width = 2700
    window_height = 1200
    
    root.title()
    root.geometry(getGeometory(root, window_width, window_height))
    root.state('zoomed')
    # アプリの起動まで3秒かかる。
    s_time = time.perf_counter()
    app = Application(master=root);
    e_time = time.perf_counter()
    logger.debug("実行時間: {}秒".format(e_time - s_time))

    # ここで、アプリが動き続ける / アプリを終了するまで

    app.mainloop()

    # メモリを解放してくれる（thread）
    gc.collect()

def go():
    try:
        main()
    except Exception as err:
        print(err)   
        
        
if __name__ == "__main__":
    go()


