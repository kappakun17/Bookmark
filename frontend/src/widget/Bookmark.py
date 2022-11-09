import base64
from concurrent.futures import ThreadPoolExecutor
import io
from PIL import ImageTk, Image, UnidentifiedImageError
import pyperclip
from frontend.src.utilities.text.text import textIndention,textCountChecker
import tkinter as tk
import favicon
import requests
import webbrowser
import re
import time

from frontend.src.widget.Dialogs_MenuBars import my_Dialogs_MenuBars


class my_Bookmark(tk.Canvas):
    def __init__(self, master=None, DB=None, APP=None, JSON = None, cnf={}, **kw):
        
        self.db = DB
        self.app = APP
        self.json = JSON
    
        # state
        self.name_var = tk.StringVar();
        self.url_var = tk.StringVar()
        self.memo_var = tk.StringVar();
        
        # set state
        self.name_var.set(self.json['name'])
        self.url_var.set(self.json['url']);
        self.memo_var.set(self.json['memo'])
        
        # image
        self.BookmarkCardImage = tk.PhotoImage(file="frontend/src/img/bookmark/bookmark_card.png")
        self.BookmarkBrowserImage = tk.PhotoImage(file="frontend/src/img/bookmark/bookmark_browser_btn.png")
        self.BookmarkMenuImage = tk.PhotoImage(file="frontend/src/img/bookmark/boomkark_menu_btn.png")
        self.BookmarkViewImage = tk.PhotoImage(file="frontend/src/img/bookmark/bookmark_view_btn.png")
        self.BookmarkLinkImage = tk.PhotoImage(file="frontend/src/img/bookmark/bookmark_copy_link_btn.png")
        self.BookmarkDescBrowserImage = tk.PhotoImage(file="frontend/src/img/bookmark/bookmark_description_browser.png")
        self.BookmarkDescCopyLinkImage = tk.PhotoImage(file="frontend/src/img/bookmark/bookmark_description_copy_link.png")
        self.BookmarkDescCopiedLinkImage = tk.PhotoImage(file="frontend/src/img/bookmark/bookmark_description_copied_link.png")
        self.BookmarkDescWebviewImage = tk.PhotoImage(file="frontend/src/img/bookmark/bookmark_description_webview.png")
        
        if self.json['icon'] is None:
            self.BookmarkFaviconImage = tk.PhotoImage(file="frontend/src/img/bookmark/bookmark_no_icon.png")
            
        # icon blobデータがあれば、バイナリ変換し、pngへエンコードする。
        else:
            try:
                icon = self.convertBynaryToImage(self.convertStrToBynary(self.json['icon']))
                self.BookmarkFaviconImage = ImageTk.PhotoImage(self.resizeImage(icon))
            except UnidentifiedImageError:
                self.BookmarkFaviconImage = tk.PhotoImage(file="frontend/src/img/bookmark/bookmark_no_icon.png")


        # bookmark card
        tk.Canvas.__init__(self, master, cnf, **kw);
        self.configure(
            width=780,
            height=240,
            bg="#fffdf8",
            highlightthickness=0,
            relief='ridge',
        )
        
        # background image
        self.create_image(0, 0, image=self.BookmarkCardImage, anchor='nw')
        # favicon image
        self.create_image(30, 30, image=self.BookmarkFaviconImage, anchor='nw')
        
        # title name
        self.create_text(140,45, text=textCountChecker(self.name_var.get(),10), fill='#6251FA', anchor="nw",font=("HGPｺﾞｼｯｸE", "17", "bold"))
        # url
        self.create_text(140,90, text=textCountChecker(self.url_var.get(), 35), fill='#B9B9B9', anchor="nw",font=("HGPｺﾞｼｯｸE", "10", "bold"))
        # memo
        self.create_text(140,150, text=textIndention(self.memo_var.get(), 35), fill='#6C6C6C', anchor="nw",font=("HGPｺﾞｼｯｸE", "10", "bold"))
        
        # browser button
        self.browser_btn = tk.Button(
            self,
            image=self.BookmarkBrowserImage,
            command=lambda:self.OpenUrlToBrowser(),
            cursor='hand2',
            bg='#fffdf8',
            borderwidth = 0,
            highlightthickness = 0,
            relief = "flat",
            activebackground='#fffdf8'
            )
        self.browser_btn.place(x=540,y=50)
        
        # link button
        self.copy_link_btn = tk.Button(
            self,
            image=self.BookmarkLinkImage,
            command=lambda:self.CopyUrlToClipBoard(),
            cursor='hand2',
            bg='#fffdf8',
            borderwidth = 0,
            highlightthickness = 0,
            relief = "flat",
            activebackground='#fffdf8'
            )
        self.copy_link_btn.place(x=600,y=50)
        
        # view button
        self.view_btn = tk.Button(
            self,
            image=self.BookmarkViewImage,
            command="",
            cursor='hand2',
            bg='#fffdf8',
            borderwidth = 0,
            highlightthickness = 0,
            relief = "flat",
            activebackground='#fffdf8'
            )
        self.view_btn.place(x=660,y=50)
        
        # menu button
        self.menu_btn = tk.Button(
            self,
            image=self.BookmarkMenuImage,
            command="",
            cursor='hand2',
            bg='#fffdf8',
            borderwidth = 0,
            highlightthickness = 0,
            relief = "flat",
            activebackground='#fffdf8'
            )
        self.menu_btn.place(x=725,y=70)
        self.menu_btn.bind('<Button-1>', self.open_menu_bar)
        
        self.desc_browser = tk.Label(self, image=self.BookmarkDescBrowserImage, bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground='#fffdf8')
        # self.desc_browser.place(x=505, y=5)
        
        self.desc_copyLink = tk.Label(self, image=self.BookmarkDescCopyLinkImage, bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground='#fffdf8')
        # self.desc_copyLink.place(x=570, y=5)
        
        self.desc_copiedLink = tk.Label(self, image=self.BookmarkDescCopiedLinkImage, bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground='#fffdf8')
        # self.desc_copiedLink.place(x=570, y=0)
        
        self.desc_webview = tk.Label(self, image=self.BookmarkDescWebviewImage, bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground='#fffdf8')
        # self.desc_webview.place(x=635, y=5)
        
        self.pack(padx=(0,0))
        self.config(cursor='hand2')
        # self.bind('<Button-1>', self.test_category)
    
    def convertStrToBynary(self, icon_s):
        if icon_s is None: return icon_s
        return base64.b64decode(icon_s.encode())
    
    def convertBynaryToImage(self, icon_b):
        if icon_b is None: return icon_b
        # print(icon_b)
        # print(type(icon_b))
        return Image.open(io.BytesIO(icon_b))
    
    def resizeImage(self, icon):
        return icon.resize((70,70))
    
    def OpenUrlToBrowser(self):
        if self.url_var.get():
            webbrowser.open_new(self.url_var.get());
        else:
            print("cant' open web browser. because not having url")
            
    def CopyUrlToClipBoard(self):
        if self.url_var.get():
            pyperclip.copy(self.url_var.get())
        else:
            print("can't copy because no having url")
    
    def display_description(self,event,desc, x, y):
        time.sleep(0.6)
        desc.place(x=x, y=y)

    def no_display_description(self, event, desc):
        desc.place_forget()
    
    def alert_description(self, event,off_desc, on_desc, x, y):
        off_desc.place_forget()
        on_desc.place(x=x, y=y)
        
        on_desc.after(1500, on_desc.place_forget)
    
    def open_menu_bar(self, event):
        my_Dialogs_MenuBars(self, DB=self.db, APP=self.app, JSON=self.json).create_bookmark_menu()
    
    
    
            