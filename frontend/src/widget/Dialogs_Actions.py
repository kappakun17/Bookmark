from collections import deque
from functools import partial

import re
import tkinter as tk

import sqlite3
import urllib.request

import favicon
import requests

from initialize_dataset import initialize_dataset

from frontend.src.utilities.geometory.geometory import getGeometory
from frontend.src.widget.dialogs.AddScreen import my_Dialogs_AddScreen
from frontend.src.widget.dialogs.RenameScreen import my_Dialogs_RenameScreen
from frontend.src.widget.dialogs.EditScreen import my_Dialogs_EditScreen
from frontend.src.widget.dialogs.DeleteScreen import my_Dialogs_DeleteScreen
from frontend.src.widget.dialogs.ConfirmInitializeDBScreen import my_Dialogs_ConfirmInitializeDBScreen
from frontend.src.widget.dialogs.ErrorScreen import my_Dialogs_ErrorScreen

from frontend.src.widget.dialogs.HasNoUrl import my_Dialogs_HasNoUrl
from frontend.src.widget.dialogs.IntroductionScreen import my_Dialogs_IntroductionScreen

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
        
        # ==== keyとactionを使うことで、どのジャンルのどの処理を求めているかを判定する
        # ==== key -> category or folder or bookmark
        # ==== action -> add or rename or edit or delete
        self.key = key
        self.action = action
        
        self.actionTrigger = {
            'add':self.create_add_screen,
            'edit':self.create_edit_screen,
            'rename':self.create_rename_screen,
            'delete':self.create_delete_screen,
            'introduction':self.create_introduction_screen,
            'initialize_database':self.create_confirm_initialize_database_screen,
        }
        
        self.actionTitle = {
            'add':"新規登録",
            'edit':"修正",
            'rename':"名前変更",
            'delete':"削除",
            'introduction':'ITL Bookmarkへ',
            'initialize_database':'データベースの初期化'
        }
        
        self.keyName = {
            'category':"カテゴリー",
            'folder':"フォルダー",
            'bookmark':"ブックマーク",
            'introduction':"説明",
            'settings':"設定",
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
            },
            'introduction':{
                'background-color':'#6251FA',
                'font-color':'#FFFDF8',
            },
            'settings':{
                'background-color':'#6251FA',
                'font-color':'#FFFDF8',
            },
        }
        
        self.keyDbTriger = {
            'category':{
                'add':self.DB_insert_category_name,
                'rename':self.DB_update_category_name,
                'delete':self.DB_delete_category,

            },
            'folder':{
                'add':self.DB_insert_folder_name,
                'rename':self.DB_update_folder_name,
                'delete':self.DB_delete_folder,
            },
            'bookmark':{
                'add':self.DB_insert_bookmark,
                'edit':self.DB_update_bookmark,
                'delete':self.DB_delete_bookmark,
            },
            'has_no_url':{
                'add':self.DB_insert_has_no_url,
                'edit':self.DB_update_has_no_url,
            },
            'settings':{
                'initialize_database':self.initialize_database,
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

        eventHandler = None

        self.screen = my_Dialogs_AddScreen(master=self.dialog, key=self.key,)
        eventHandler = self.screen.get_params
                
        self.screen.submit_btn.configure(command = partial(self.keyDbTriger[self.key][self.action], eventHandler=eventHandler))
        self.screen.cancel_btn.configure(command = lambda:self.close_action_screen())
        
        self.dialog.bind("<Return>", partial(self.keyDbTriger[self.key][self.action], eventHandler=eventHandler))
        self.dialog.bind("<Escape>", self.close_action_screen)
        
       
    
    def create_rename_screen(self):
        self.dialog = self.create_dialog()
        self.screen = my_Dialogs_RenameScreen(self.dialog, key = self.key, prev_name=self.json['name'])
        
        eventHandler = self.screen.get_params
        
        self.screen.modify_btn.configure(command= partial(self.keyDbTriger[self.key][self.action], eventHandler=eventHandler))
        self.screen.cancel_btn.configure(command = lambda:self.close_action_screen())
        
        self.dialog.bind("<Return>", partial(self.keyDbTriger[self.key][self.action], eventHandler=eventHandler))
        self.dialog.bind("<Escape>", self.close_action_screen)
    
    def create_edit_screen(self):
        self.dialog = self.create_dialog()
        self.screen = my_Dialogs_EditScreen(self.dialog, key=self.key, prev_json = self.json)
        
        eventHandler = self.screen.get_params
        
        self.screen.modify_btn.configure(command=partial(self.keyDbTriger[self.key][self.action], eventHandler=eventHandler))
        self.screen.cancel_btn.configure(command=lambda:self.close_action_screen())
        
        self.dialog.bind("<Return>", partial(self.keyDbTriger[self.key][self.action], eventHandler=eventHandler))
        self.dialog.bind("<Escape>", self.close_action_screen)
    
    def create_delete_screen(self):
        self.dialog = self.create_dialog()
        self.screen = my_Dialogs_DeleteScreen(self.dialog, JSON=self.json)
        
        self.screen.delete_btn.configure(command=partial(self.keyDbTriger[self.key][self.action]))
        self.screen.cancel_btn.configure(command=lambda:self.close_action_screen())
        
        self.dialog.bind("<Return>", partial(self.keyDbTriger[self.key][self.action]))
        self.dialog.bind("<Escape>", self.close_action_screen)

    def create_introduction_screen(self):
        self.dialog = tk.Toplevel(self, bg='#fffdf8')
        self.dialog.title("説明")
        self.dialog.geometry(getGeometory(self.master.master, 1000, 1150))
        self.dialog.grab_set()
        self.dialog.focus_set()
        self.dialog.transient(self.master)
        self.create_header_bar(self.dialog)

        self.screen = my_Dialogs_IntroductionScreen(self.dialog, db=self.db)
        self.dialog.bind("<Escape>", self.close_action_screen)
        
    def create_confirm_initialize_database_screen(self):
        self.dialog = self.create_dialog()
        self.screen = my_Dialogs_ConfirmInitializeDBScreen(self.dialog)
        
        self.screen.delete_btn.configure(command=partial(self.keyDbTriger[self.key][self.action]))
        self.screen.cancel_btn.configure(command=lambda:self.close_action_screen())
        
        self.dialog.bind("<Return>", partial(self.keyDbTriger[self.key][self.action]))
        self.dialog.bind("<Escape>", self.close_action_screen)
        
    def create_error_screen(self, error):
        dialog = tk.Toplevel(self.dialog, bg='#fffdf8')
        dialog.title("Bookmark Action")
        dialog.geometry(getGeometory(self.master.master, 1000, 800))
        dialog.grab_set()
        dialog.focus_set()
        dialog.transient(self.master)
        
        self.create_header_bar(dialog)
        self.create_title_bar(dialog)
        
        self.screen = my_Dialogs_ErrorScreen(dialog, error=error)
        self.screen.return_btn.configure(command=partial(self.close_action_screen, widget=dialog))
        dialog.bind("<Escape>", partial(self.close_action_screen, widget=dialog))
    
    def create_header_bar(self, master):
        header_label = tk.Label(master, text=self.json['name'], bg=self.keyColor[self.key]['background-color'], borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground='#fffdf8', height=2,  font=("HGPｺﾞｼｯｸE", "10", "bold"), foreground=self.keyColor[self.key]['font-color'])
        header_label.pack(fill='x', anchor='ne', ipady=15)
        
    def create_title_bar(self,master):
        title_label = tk.Label(master, text=self.get_title_name(key=self.key, action=self.action), bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground='#fffdf8', height=2,  font=("HGPｺﾞｼｯｸE", "13", "bold"), foreground='#5B5B5B')
        title_label.pack(fill='x', anchor='ne', ipady=15)

    def has_no_url(self, db_params):
        if self.screen is None: return
        
        dialog = tk.Toplevel(self.dialog, bg='#fffdf8')
        dialog.title("Bookmark Action")
        dialog.geometry(getGeometory(self.master.master, 1000, 800))
        dialog.grab_set()
        dialog.focus_set()
        dialog.transient(self.master)
        
        self.create_header_bar(dialog)
        self.create_title_bar(dialog)
        
        self.screen = my_Dialogs_HasNoUrl(dialog, db_params)
        
        self.screen.submit_btn.configure(command=partial(self.keyDbTriger['has_no_url'][self.action], db_params=db_params))
        self.screen.cancel_btn.configure(command=partial(self.close_action_screen, widget=dialog))
        
        dialog.bind("<Return>", partial(self.keyDbTriger['has_no_url'][self.action], db_params=db_params))
        dialog.bind("<Escape>", partial(self.close_action_screen, widget=dialog))
        
    def get_title_name(self, key, action):
        return "{}の{}".format(self.keyName[key], self.actionTitle[action])

    def initialize_database(self, event=None):
        self.db.rebuildDB()
        self.app.re_render_categoryAndFolders()
        self.app.re_render_bookmarks(folder_key=1, is_force_reload=True)
        self.dialog.destroy()

    # === **kw -> データベース登録に必要なparameter
    
    def DB_insert_category_name(self,event=None, eventHandler=None):
        
        # the eventHandler which is for getting the name data
        db_params = eventHandler()
        
        if db_params is None: return
        
        if self.check_input_data(db_params) != True: return
        
        try:
            self.db.insert_category(category_name = db_params['name'])
        except sqlite3.IntegrityError:
            return self.create_error_screen('unique')
        
        logger.debug('カテゴリー[{}]をデータベースに追加しました。'.format(db_params['name']))
        
        # reload category and folders
        self.app.re_render_categoryAndFolders()
        self.dialog.destroy()
        
        
    def DB_insert_folder_name(self,event=None, eventHandler=None):

        db_params = eventHandler()
        JSON_category_id = self.json['id']
        
        if db_params is None or JSON_category_id is None: return
        
        if self.check_input_data(db_params) != True: return

        self.db.insert_folder(folder_name=db_params['name'], category_id = JSON_category_id)
        logger.debug('フォルダー[{}]をデータベースに追加しました。'.format(db_params['name']))
        
        self.app.re_render_categoryAndFolders()
        self.dialog.destroy()

    def DB_insert_bookmark(self,event=None, eventHandler=None):
        db_params = eventHandler()
        JSON_folder_id = self.json['folder_id'][0]
        
                
        if db_params is None or JSON_folder_id is None: return
        
        if self.check_input_data(db_params) != True: return

        if self.checkInternetHTTPLib(url=db_params['url']) == False: return self.create_error_screen('network')
        
        if self.is_url(db_params['url']) == False: return self.has_no_url(db_params)
        
    
        try:
            icon = self.getUrlImage(db_params['url'])
        except requests.exceptions.HTTPError:
            return self.has_no_url(db_params)
        
        try:
            self.db.insert_bookmark(bookmark_name=db_params['name'], bookmark_url=db_params['url'], bookmark_memo=db_params['memo'], folder_id=JSON_folder_id, icon=icon)
        except sqlite3.IntegrityError:
            return self.create_error_screen('no_category_and_folder')
    
        logger.debug('ブックマーク[{}]をデータベースに追加しました。'.format(db_params['name']))
        
        
        self.app.re_render_bookmarks(folder_key=JSON_folder_id, is_force_reload=True)
        self.dialog.destroy()

    def DB_insert_has_no_url(self,event=None, db_params=None):
        icon = None
        JSON_folder_id = self.json['folder_id'][0]

        try:
            self.db.insert_bookmark(bookmark_name=db_params['name'], bookmark_url=db_params['url'], bookmark_memo=db_params['memo'], folder_id=JSON_folder_id, icon=icon)
        except sqlite3.IntegrityError:
            return self.create_error_screen('no_category_and_folder')
        self.app.re_render_bookmarks(folder_key=JSON_folder_id, is_force_reload=True)
        self.dialog.destroy()
        
    def DB_update_category_name(self,event=None, eventHandler=None):
        db_params = eventHandler()
        JSON_category_id = self.json['id']
        if db_params is None: return
        
        if self.check_input_data(db_params) != True: return
        
        self.db.update_categoryName(category_id=JSON_category_id, category_name=db_params['name'])
        logger.debug('カテゴリーを[{}]に修正しました。'.format(db_params['name']))
        
        self.app.re_render_categoryAndFolders()
        self.dialog.destroy()
        
    def DB_update_folder_name(self,event=None, eventHandler=None):
        db_params = eventHandler()
        JSON_folder_id = self.json['id']
        
        if db_params is None: return
        
        if self.check_input_data(db_params) != True: return
        
        self.db.update_folderName(folder_id=JSON_folder_id, folder_name=db_params['name'])
        logger.debug('フォルダーを[{}]に修正しました。'.format(db_params['name']))
        
        self.app.re_render_categoryAndFolders()
        self.dialog.destroy()

    def DB_update_bookmark(self,event=None, eventHandler=None):
        db_params = eventHandler()
        JSON_bookmark_id = self.json['id']
        JSON_folder_id = self.json['folder_id'][0]
        
        if db_params is None: return
        
        if self.check_input_data(db_params) != True: return
        
        if self.checkInternetHTTPLib(url=db_params['url']) == False: return self.create_error_screen('network')
        
        if self.is_url(db_params['url']) == False: return self.has_no_url(db_params)
        
        try:
            icon = self.getUrlImage(db_params['url'])
        except requests.exceptions.HTTPError:
            return self.has_no_url(db_params)
        
        self.db.update_bookmark(bookmark_id=JSON_bookmark_id, bookmark_name=db_params['name'], bookmark_url=db_params['url'], bookmark_memo=db_params['memo'], folder_id=JSON_folder_id, icon=icon)
        
        self.app.re_render_bookmarks(folder_key=JSON_folder_id, is_force_reload=True)
        self.dialog.destroy()

    def DB_update_has_no_url(self,event=None, db_params=None):
        JSON_bookmark_id = self.json['id']
        JSON_folder_id = self.json['folder_id'][0]
        icon = None

        self.db.update_bookmark(bookmark_id=JSON_bookmark_id, bookmark_name=db_params['name'], bookmark_url=db_params['url'], bookmark_memo=db_params['memo'], folder_id=JSON_folder_id, icon=icon)

        self.app.re_render_bookmarks(folder_key=JSON_folder_id, is_force_reload=True)
        self.dialog.destroy()
    
    def DB_delete_category(self,event=None):
        self.db.delete_category(category_id=self.json['id'])
        self.app.re_render_categoryAndFolders()
        self.app.re_render_bookmarks(folder_key=self.json['id'], is_force_reload=True)
        self.dialog.destroy()
        
    def DB_delete_folder(self,event=None):
        self.db.delete_folder(folder_id=self.json['id'])
        self.app.re_render_categoryAndFolders()
        self.dialog.destroy()
        
    def DB_delete_bookmark(self, event=None):
        JSON_folder_id = self.json['folder_id'][0]

        self.db.delete_bookmark(bookmark_id=self.json['id'])
        
        self.app.re_render_bookmarks(folder_key=JSON_folder_id, is_force_reload=True)
        self.dialog.destroy()
        
    def is_url(self, url):
        flag = True
        try:
            f = urllib.request.urlopen(url)
            f.close()
        except urllib.request.HTTPError:
            flag=True
        except ValueError:
            flag = False
        
        return flag
    
    def getUrlImage(self, url):
        if not url: return None
        icons = favicon.get(url);
        # print(icons)
        
        re_icons=deque()
        for icon in icons:
            if bool(re.match(r"(https?)(:\/\/[-_.!~*\'()a-zA-Z0-9;\/?:\@&=+\$,%#]+)\.((jpg|jpeg|png|ico)$)", icon.url)):
                if icon.format == 'ico':
                    re_icons.appendleft(icon)
                else:
                    re_icons.append(icon);
                
        # print(re_icons)
        
        if len(re_icons) <= 0:
            if len(icons) <=0:
                icon = None
            else:
                icon = icons[0]
        
        else:
            icon = re_icons[0]
        
        if icon is None: return icon
        # print(icon)
        response = requests.get(icon.url, stream=True)
        img_data = response.content
    
        return img_data
    
    def close_action_screen(self,event=None, widget=None):
        if widget is None: return self.dialog.destroy()
        widget.destroy()
        
        
    def checkInternetHTTPLib(self, url=None):
        flag = True
        timeout = 5

        try:
            requests.get(url, timeout=timeout)
            return flag
        except requests.exceptions.MissingSchema:
            return flag
        except (requests.ConnectionError, requests.Timeout) as exception:
            flag = False
            return flag
        
    
    def check_input_data(self, db_params):
        
        if db_params['name'] == '': return self.create_error_screen('no_name');
            
        if self.key == 'bookmark':
            if db_params['url'] == '': return self.create_error_screen('no_url')
            
        return True