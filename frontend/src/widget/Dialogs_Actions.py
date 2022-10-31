import base64
from collections import deque
from functools import partial
from io import BytesIO
import re
import tkinter as tk
from venv import create

import urllib.request

import favicon
import requests

from PIL import Image

from frontend.src.utilities.geometory.geometory import getGeometory
from frontend.src.widget.dialogs.AddScreen import my_Dialogs_AddScreen
from frontend.src.widget.dialogs.HasNoUrl import my_Dialogs_HasNoUrl

import logging
logger = logging.getLogger(__name__)

class my_Dialogs_Actions(tk.Frame):

    def __init__(self, master=None, key=None, action=None, DB=None, APP=None, JSON=None):
        super().__init__(master)
        
        self.dialog = None
        self.master = master
        self.dialog = None
        self.screen = None
        self.app = APP
        self.db = DB
        self.json = JSON
        
        print(self.json)
        
        # ==== keyとactionを使うことで、どのジャンルのどの処理を求めているかを判定する
        # ==== key -> category or folder or bookmark
        # ==== action -> add or rename or edit or delete
        self.key = key
        self.action = action
        
        self.actionTrigger = {
            'add':self.create_add_screen,
            'edit':self.create_edit_screen,
            'rename':self.create_rename_screen,
            'delete':self.create_delete_screen
        }
        
        self.actionTitle = {
            'add':"新規登録",
            'edit':"修正",
            'rename':"名前変更",
            'delete':"削除"
        }
        
        self.keyName = {
            'category':"カテゴリー",
            'folder':"フォルダー",
            'bookmark':"ブックマーク"
        }

        self.keyColor = {
            'category': {
                'background-color':'#E893B1',
                'font-color':'#FFFFFF'
            },
            'folder': {
                'background-color':'#E6E6E6',
                'font-color':'#6251FA'
            },
            'bookmark':{
                'background-color':'#6251FA',
                'font-color':'#FFFDF8',
            }
        }
        
        self.keyDbTriger = {
            'category':{
                'add':self.DB_insert_category_title,

            },
            'folder':{
                'add':self.DB_insert_folder_title
            },
            'bookmark':{
                'add':self.DB_insert_bookmark,
            }
        }
        
        if self.action not in self.actionTrigger: return
        else:
            event = self.actionTrigger[self.action]
            event()
        
    def create_dialog(self):
        dialog = tk.Toplevel(self, bg='#fffdf8')
        dialog.title("Bookmark Action")
        dialog.geometry(getGeometory(self.master.master, 1000, 800))
        dialog.grab_set()
        dialog.focus_set()
        dialog.transient(self.master)
        
        self.create_header_bar(dialog)
        self.create_title_bar(dialog)
        
        return dialog
    
    def create_add_screen(self):
        self.dialog = self.create_dialog()
        self.screen = my_Dialogs_AddScreen(self.dialog, self.key)
        
        eventHander = self.screen.get_params
                
        self.screen.submit_btn.configure(command = partial(self.keyDbTriger[self.key][self.action], eventHandler=eventHander))
        self.screen.cancel_btn.configure(command = lambda:self.close_action_screen())
       
    
    def create_rename_screen(self):
        self.dialog = self.create_dialog()
        self.screen = my_Dialogs_RenameScreen(self.dialog)
        
    def create_edit_screen(self):
        self.dialog = self.create_dialog()
        self.screen = my_Dialogs_EditScreen(self.dialog)
        
    def create_delete_screen(self):
        self.dialog = self.create_dialog()
        self.screen = my_Dialogs_DeleteScreen(self.dialog)
    
    
    def create_header_bar(self, master):
        header_label = tk.Label(master, text=self.json['name'], bg=self.keyColor[self.key]['background-color'], borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground='#fffdf8', height=2,  font=("HGPｺﾞｼｯｸE", "10", "bold"), foreground=self.keyColor[self.key]['font-color'])
        header_label.pack(fill='x', anchor='ne', ipady=15)
        
    def create_title_bar(self,master):
        title_label = tk.Label(master, text=self.get_title_name(key=self.key, action=self.action), bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground='#fffdf8', height=2,  font=("HGPｺﾞｼｯｸE", "13", "bold"), foreground='#5B5B5B')
        title_label.pack(fill='x', anchor='ne', ipady=15)
        
    def get_title_name(self, key, action):
        return "{}の{}".format(self.keyName[key], self.actionTitle[action])

    # === **kw -> データベース登録に必要なparameter
    
    def DB_insert_category_title(self,eventHandler=None):
        
        # the eventHandler which is for getting the name data
        db_params = eventHandler()
        
        if db_params is None: return
        
        self.db.insert_category(category_name = db_params['name'])
        logger.debug('カテゴリー[{}]をデータベースに追加しました。'.format(db_params['name']))
        
        # reload category and folders
        self.app.re_render_categoryAndFolders()
        
        
    def DB_insert_folder_title(self, eventHandler=None):

        db_params = eventHandler()
        JSON_category_id = self.json['id']
        
        if db_params is None or JSON_category_id is None: return

        self.db.insert_folder(folder_name=db_params['name'], category_id = JSON_category_id)
        logger.debug('フォルダー[{}]をデータベースに追加しました。'.format(db_params['name']))
        
        self.app.re_render_categoryAndFolders()

    def DB_insert_bookmark(self, eventHandler=None):
        db_params = eventHandler()
        JSON_folder_id = self.json['id']
        
        if db_params is None or JSON_folder_id is None: return

        # if self.is_url(db_params['url']) == False: return self.has_no_url(db_params)
        
        icon = self.getUrlImage(db_params['url'])
        
        self.db.insert_bookmark(bookmark_name=db_params['name'], bookmark_url=db_params['url'], bookmark_memo=db_params['memo'], folder_id=JSON_folder_id, icon=icon)
        logger.debug('ブックマーク[{}]をデータベースに追加しました。'.format(db_params['name']))
        
        
        self.app.re_render_bookmarks(folder_key=JSON_folder_id, is_force_reload=True)
        self.dialog.destroy()
        
    def has_no_url(self, db_params):
        if self.screen is None: return
        self.screen.destroy()
        self.screen = my_Dialogs_HasNoUrl(self.dialog, url=db_params['url'])
        
        # self.screen.return_btn.configure(command=partial())
        
        self.dialog = self.create_dialog
        
        
    def is_url(self, url):
        flag = True
        try:
            f = urllib.request.urlopen(url)
            f.close()
        except urllib.request.HTTPError:
            flag = False
        except ValueError:
            flag = False
        
        return flag
    
    def getUrlImage(self, url):
        if not url: return None
        icons = favicon.get(url);
        print(icons)
        
        re_icons=deque()
        for icon in icons:
            if bool(re.match(r"(https?)(:\/\/[-_.!~*\'()a-zA-Z0-9;\/?:\@&=+\$,%#]+)\.((jpg|jpeg|png|ico)$)", icon.url)):
                if icon.format == 'ico':
                    re_icons.appendleft(icon)
                else:
                    re_icons.append(icon);
                
        print(re_icons)
        
        if len(re_icons) <= 0:
            if len(icons) <=0:
                icon = None
            else:
                icon = icons[0]
        
        else:
            icon = re_icons[0];
        
        if icon is None: return icon
        print(icon)
        response = requests.get(icon.url, stream=True)
        img_data = response.content
    
        return img_data
    
    def close_action_screen(self):
        self.dialog.destroy()