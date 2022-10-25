import tkinter as tk

from frontend.src.utilities.geometory.geometory import getGeometory

class my_Dialogs_Actions(tk.Frame):

    def __init__(self, master = None, key=None, action=None):
        super().__init__(master)
        
        self.actionTrigger = {
            'add':self.create_add_screen,
            'edit':self.create_edit_screen,
            'rename':self.create_rename_screen,
            'delete':self.create_delete_screen
        }
        
        if action not in self.actionTrigger: return
        else:
            event = self.actionTrigger[action]
            event(key)
            
    def create_dialog(self, title):
        dialog = tk.Toplevel(self, bg='#fffdf8')
        dialog.title(title)
        dialog.geometry(getGeometory(self, 1000, 700))
        dialog.grab_set()
        dialog.focus_set()
        dialog.transient(self.master)
        return dialog
    
    def create_add_screen(self, key):
        self.create_dialog()
    
    def create_rename_screen(self, key):
        self.create_dialog()
    
    def create_edit_screen(self, key):
        self.create_dialog()
        
    def create_delete_screen(self, key):
        self.create_dialog()