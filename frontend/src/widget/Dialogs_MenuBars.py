from functools import partial
from tkinter import *
import tkinter as tk

from frontend.src.utilities.geometory.geometory import getGeometory
from frontend.src.widget.dialogs.BookmarkMenu import my_BookmarkMenu
from frontend.src.widget.dialogs.CategoryMenu import my_CategoryMenu
from frontend.src.widget.dialogs.FolderMenu import my_FolderMenu

from frontend.src.widget.Dialogs_Actions import my_Dialogs_Actions

class my_Dialogs_MenuBars(tk.Frame):

    def __init__(self, master = None, DB=None):
        super().__init__(master)
        self.db = DB
        self.title = None
        
    def create_dialog(self, title):
        dialog = tk.Toplevel(self, bg='#fffdf8')
        dialog.title(title)
        dialog.geometry(getGeometory(self, 350, 500))
        dialog.grab_set()
        dialog.focus_set()
        dialog.transient(self.master)
        return dialog
    
    def create_category_menu(self, title):
        self.title = title
        category_dialog = self.create_dialog("Category Menu")
        self.categoryMenu = my_CategoryMenu(category_dialog, title=self.title)
        self.categoryMenu.category_add_btn.bind("<Button-1>", partial(self.open_screen, key='category', action='add'))
        self.categoryMenu.folder_add_btn.bind("<Button-1>", partial(self.open_screen, key='folder', action='add'))
        self.categoryMenu.category_rename_btn.bind("<Button-1>", partial(self.open_screen, key='category', action='rename'))
        self.categoryMenu.category_delete_btn.bind("<Button-1>", partial(self.open_screen, key='category', action='delete'))
        
        
        self.wait_window(category_dialog)
        
    def create_folder_menu(self, title):
        self.title = title
        folder_dialog = self.create_dialog("Folder Menu")
        self.folderMenu = my_FolderMenu(folder_dialog, title=self.title)
        self.folderMenu.folder_rename_btn.bind("<Button-1>", partial(self.open_screen, key='folder', action='rename'))
        self.folderMenu.bookmark_add_btn.bind("<Button-1>", partial(self.open_screen, key='bookmark', action='add'))
        self.folderMenu.folder_delete_btn.bind("<Button-1>", partial(self.open_screen, key='folder', action='delete'))
        self.wait_window(folder_dialog)
        
    def create_bookmark_menu(self, title):
        self.title = title
        bookmark_dialog = self.create_dialog("Bookmark Menu")
        self.bookmarkMenu = my_BookmarkMenu(bookmark_dialog, title=self.title)
        self.bookmarkMenu.bookmark_add_btn.bind("<Button-1>", partial(self.open_screen, key='bookmark', action='add'))
        self.bookmarkMenu.bookmark_edit_btn.bind("<Button-1>", partial(self.open_screen, key='bookmark', action='edit'))
        self.bookmarkMenu.bookmark_delete_btn.bind("<Button-1>", partial(self.open_screen, key='bookmark', action='delete'))
        self.wait_window(bookmark_dialog)
    
    # key = bookmark, action= add || edit || rename
    def open_screen(self,event, key=None, action=None):
        if key==None or action==None : return
        if self.title is None: return print("タイトルがありません。") 
        self.destroy()
        master = self.master
        self.action_screen = my_Dialogs_Actions(master, title=self.title, key=key, action=action, DB=self.db)