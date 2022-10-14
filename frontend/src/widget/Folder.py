import tkinter as tk

class my_Folder(tk.Canvas):
    def __init__(self, master=None, cnf={}, **kw):
        
        self.FolderImage = tk.PhotoImage(file="frontend/src/img/folder/folder.png");
        self.FolderBtnImage = tk.PhotoImage(fil="frontend/src/img/folder/folder_btn.png");
        
        # self.FolderImage = folder_img;
        # self.FolderBtnImage = kw.get('folder_btn_img', 0)
        
        
        tk.Canvas.__init__(self, master, cnf, **kw)
        self.configure(
            width=429,
            height=51,
            bg="#fffdf8",
            highlightthickness=0,
            relief='ridge',
        )
        
        self.create_image(0,0,image=self.FolderImage, anchor='nw')
        self.create_text(50,15, text="folderName", fill='#6251FA', anchor='nw', font=("MSゴシック", "11", "bold"))
        
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
            ).place(x=380,y=25)
        
        self.pack(anchor='e',pady=5)
        self.config(cursor='hand2')
        self.bind('<Button-1>', self.test)
    
    def test(self, event):
        print('click the folder')