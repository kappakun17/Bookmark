import tkinter as tk
from tkinter import simpledialog

class MyDialog(simpledialog.Dialog):
    def body(self, master):
        '''ダイアログボックスの表示

        どのラジオボタンがクリックされたかself.varに格納(Red=1,Green=2,Blue=3)
        ラジオボタンをクリックした際にはswitchButtonStateメソッドでOKボタンをenableにする
        '''

        self.var = tk.IntVar()
        rdo1 = tk.Radiobutton(master, value=1, variable=self.var, command=self.switchButtonState, text='Red').pack(side=tk.LEFT, padx=5, pady=5)
        rdo2 = tk.Radiobutton(master, value=2, variable=self.var, command=self.switchButtonState, text='Green').pack(side=tk.LEFT, padx=5, pady=5)
        rdo3 = tk.Radiobutton(master, value=3, variable=self.var, command=self.switchButtonState, text='Blue').pack(side=tk.LEFT, padx=5, pady=5)

 

    def buttonbox(self):
        '''OK,キャンセルボタンの配置 

        OKボタンはデフォルトではdisableにしておく
        '''
        box = tk.Frame(self)

 

        self.button1 = tk.Button(box, text="OK", width=10, command=self.ok, state=tk.DISABLED)
        self.button1.pack(side=tk.LEFT, padx=5, pady=5)
        self.button2 = tk.Button(box, text="Cancel", width=10, command=self.cancel)
        self.button2.pack(side=tk.LEFT, padx=5, pady=5) 

        box.pack() 

    def switchButtonState(self):
        # ボタンの有効化
        if self.button1['state'] == tk.DISABLED:
            self.button1['state'] = tk.NORMAL 

    def apply(self):
        # ダイアログボックスを閉じた後にラジオボタン選択結果出力
        print(self.var.get()) 
        
        