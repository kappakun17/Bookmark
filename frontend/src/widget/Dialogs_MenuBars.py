from functools import partial
from tkinter import *
import tkinter as tk

from frontend.src.utilities.geometory.geometory import getGeometory
from frontend.src.widget.dialogs.BookmarkMenu import my_BookmarkMenu
from frontend.src.widget.dialogs.CategoryMenu import my_CategoryMenu
from frontend.src.widget.dialogs.FolderMenu import my_FolderMenu
from frontend.src.widget.dialogs.SettingsMenu import my_SettingsMenu

from frontend.src.widget.Dialogs_Actions import my_Dialogs_Actions

class my_Dialogs_MenuBars(tk.Frame):

    def __init__(self, master = None, DB=None, APP=None, JSON=None):
        super().__init__(master)
        self.app = APP
        self.db = DB
        self.json = JSON
        self.name = None
        
    def create_dialog(self, title):
        dialog = tk.Toplevel(self, bg='#fffdf8')
        dialog.title(title)
        dialog.geometry(getGeometory(self, 350, 500))
        dialog.grab_set()
        dialog.focus_set()
        dialog.transient(self.master)
        return dialog
    
    def create_category_menu(self):
        self.name = self.json['name']
        category_dialog = self.create_dialog("Category Menu")
        self.categoryMenu = my_CategoryMenu(category_dialog, name=self.name)
        self.categoryMenu.category_add_btn.bind("<Button-1>", partial(self.open_screen, key='category', action='add'))
        self.categoryMenu.folder_add_btn.bind("<Button-1>", partial(self.open_screen, key='folder', action='add'))
        self.categoryMenu.category_rename_btn.bind("<Button-1>", partial(self.open_screen, key='category', action='rename'))
        self.categoryMenu.category_delete_btn.bind("<Button-1>", partial(self.open_screen, key='category', action='delete'))
        
        
        self.wait_window(category_dialog)
        
    def create_folder_menu(self):
        self.name = self.json['name']
        folder_dialog = self.create_dialog("Folder Menu")
        self.folderMenu = my_FolderMenu(folder_dialog, name=self.name)
        self.folderMenu.folder_rename_btn.bind("<Button-1>", partial(self.open_screen, key='folder', action='rename'))
        self.folderMenu.bookmark_add_btn.bind("<Button-1>", partial(self.open_screen, key='bookmark', action='add'))
        self.folderMenu.folder_delete_btn.bind("<Button-1>", partial(self.open_screen, key='folder', action='delete'))
        self.wait_window(folder_dialog)
        
    def create_bookmark_menu(self):
        self.name = self.json['name']
        bookmark_dialog = self.create_dialog("Bookmark Menu")
        self.bookmarkMenu = my_BookmarkMenu(bookmark_dialog, title=self.name)
        self.bookmarkMenu.bookmark_add_btn.bind("<Button-1>", partial(self.open_screen, key='bookmark', action='add'))
        self.bookmarkMenu.bookmark_edit_btn.bind("<Button-1>", partial(self.open_screen, key='bookmark', action='edit'))
        self.bookmarkMenu.bookmark_delete_btn.bind("<Button-1>", partial(self.open_screen, key='bookmark', action='delete'))
        self.wait_window(bookmark_dialog)

    def create_settings_menu(self):
        self.name = self.json['name']
        settings_dialog = self.create_dialog("Settings Menu")
        self.settingsMenu = my_SettingsMenu(settings_dialog, title=self.name)
        self.settingsMenu.show_instructions_btn.bind("<Button-1>", partial(self.open_screen, key='settings', action='introduction'))
        self.settingsMenu.initialize_database_btn.bind("<Button-1>", partial(self.open_screen, key='settings', action='initialize database'))
        self.wait_window(settings_dialog)
        
    # key = bookmark, action= add || edit || rename
    def open_screen(self,event, key=None, action=None):
        if key==None or action==None : return
        if self.name is None: return print("タイトルがありません。") 
        self.destroy()
        master = self.master
        self.action_screen = my_Dialogs_Actions(master, JSON=self.json, key=key, action=action, DB=self.db, APP=self.app)