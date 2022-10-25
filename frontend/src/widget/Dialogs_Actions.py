import tkinter as tk

from frontend.src.utilities.geometory.geometory import getGeometory
from frontend.src.widget.dialogs.AddScreen import my_Dialogs_AddScreen

class my_Dialogs_Actions(tk.Frame):

    def __init__(self, master=None,title=None, key=None, action=None, DB=None):
        super().__init__(master)
        
        self.screen = None
        self.db = DB
        self.title = title
        self.key = key
        self.action = action
        
        print(self.key)
        print(self.action)
        
        print(self.db)
        
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
        
        if self.action not in self.actionTrigger: return
        else:
            event = self.actionTrigger[self.action]
            event()
            
    def create_dialog(self):
        dialog = tk.Toplevel(self, bg='#fffdf8')
        dialog.title("Bookmark Action")
        dialog.geometry(getGeometory(self, 1000, 600))
        dialog.grab_set()
        dialog.focus_set()
        dialog.transient(self.master)
        
        self.create_header_bar(dialog)
        self.create_title_bar(dialog)
        
        return dialog
    
    def create_add_screen(self):
        dialog = self.create_dialog()
        self.screen = my_Dialogs_AddScreen(dialog, self.key)
    
    def create_rename_screen(self):
        dialog = self.create_dialog()
        self.screen = my_Dialogs_RenameScreen(dialog)
        
    def create_edit_screen(self):
        dialog = self.create_dialog()
        self.screen = my_Dialogs_EditScreen(dialog)
        
    def create_delete_screen(self):
        dialog = self.create_dialog()
        self.screen = my_Dialogs_DeleteScreen(dialog)
    
    
    def create_header_bar(self, master):
        header_label = tk.Label(master, text=self.title, bg='#E893B1', borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground='#fffdf8', height=2,  font=("HGPｺﾞｼｯｸE", "10", "bold"), foreground='white')
        header_label.pack(fill='x', anchor='ne', ipady=15)
        
    def create_title_bar(self,master):
        title_label = tk.Label(master, text=self.get_title_name(key=self.key, action=self.action), bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground='#fffdf8', height=2,  font=("HGPｺﾞｼｯｸE", "13", "bold"), foreground='#5B5B5B')
        title_label.pack(fill='x', anchor='ne', ipady=15)
        
    def get_title_name(self, key, action):
        return "{}の{}".format(self.keyName[key], self.actionTitle[action])