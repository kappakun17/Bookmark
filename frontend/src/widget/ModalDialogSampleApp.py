from tkinter import *
import tkinter as tk

from frontend.src.utilities.geometory.geometory import getGeometory

class ModalDialogSampleApp(tk.Frame):

    def __init__(self, master = None):
        super().__init__(master)


    def create_modeless_dialog(self):
        '''モードレスダイアログボックスの作成'''
        dlg_modeless = tk.Toplevel(self)
        dlg_modeless.title("Modeless Dialog")   # ウィンドウタイトル
        dlg_modeless.geometry("300x200")        # ウィンドウサイズ(幅x高さ)

    def create_modal_dialog(self):
        '''モーダルダイアログボックスの作成'''
       
        # x = self['event_x'];
        # y = self['event_y'];
    
        dlg_modal = tk.Toplevel(self)
        dlg_modal.title("Modal Dialog") # ウィンドウタイトル
        dlg_modal.geometry(getGeometory(self, 300, 200))   # ウィンドウサイズ(幅x高さ)
        # モーダルにする設定
        dlg_modal.grab_set()        # モーダルにする
        dlg_modal.focus_set()       # フォーカスを新しいウィンドウをへ移す
        dlg_modal.transient(self.master)   # タスクバーに表示しない
        
        # ダイアログが閉じられるまで待つ
        self.wait_window(dlg_modal)  
        print("ダイアログが閉じられた")
        