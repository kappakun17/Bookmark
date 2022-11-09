import tkinter as tk

from frontend.src.widget.Dialogs_MenuBars import my_Dialogs_MenuBars

class my_Folder(tk.Canvas):
    def __init__(self, master=None, DB=None, APP=None, JSON=None, cnf={}, **kw):
        
        self.FolderImage = tk.PhotoImage(file="frontend/src/img/folder/folder.png");
        self.FolderBtnImage = tk.PhotoImage(fil="frontend/src/img/folder/folder_btn.png");
        self.id_var = tk.IntVar()
        # self.FolderImage = folder_img;
        # self.FolderBtnImage = kw.get('folder_btn_img', 0)
        
        tk.Canvas.__init__(self, master, cnf, **kw)
        self.app = APP
        self.db = DB
        self.json_folder = JSON
        self.id_var.set(self.json_folder['id'])
        
        self.configure(
            width=429,
            height=51,
            bg="#fffdf8",
            highlightthickness=0,
            relief='ridge',
        )
        
        self.create_image(0,0,image=self.FolderImage, anchor='nw')
        self.create_text(50,15, text=self.json_folder['name'], fill='#6251FA', anchor='nw', font=("HGPｺﾞｼｯｸE", "11", "bold"))
        
        self.folder_btn = tk.Button(
            self,
            image=self.FolderBtnImage,
            command="",
            cursor='hand2',
            # bg='#E893B1',
            borderwidth = 0,
            highlightthickness = 0,
            relief = "flat",
            # activebackground='#E893B1'
            )
        self.folder_btn.place(x=380,y=25)
        self.folder_btn.bind('<Button-1>', self.open_menu_bar)
        
        self.pack(anchor='e',pady=5)
        self.config(cursor='hand2')

        
    def open_menu_bar(self, event):
        print(self.json_folder)
        my_Dialogs_MenuBars(self, APP=self.app, DB=self.db, JSON =self.json_folder).create_folder_menu()