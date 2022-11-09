from cgitb import text
import tkinter as tk

class my_Dialogs_AddScreen(tk.Frame):
    def __init__(self, master=None, key=None, on_default=None):
        self.on_default = on_default
        self.title_box_image = tk.PhotoImage(file='frontend/src/img/dialog/actions/title_box.png')
        self.text_box_image = tk.PhotoImage(file='frontend/src/img/dialog/actions/text_box.png')
        self.submit_btn_image = tk.PhotoImage(file='frontend/src/img/dialog/actions/submit_btn.png')
        self.cancel_btn_image = tk.PhotoImage(file='frontend/src/img/dialog/actions/cancel_btn.png')
        
        super().__init__(master);
        self.config(bg='#fffdf8')
        self.pack(anchor='center', pady=(50,0), fill='y')

        # title
        self.key = key
        self.name_var = tk.StringVar()
        self.url_var = tk.StringVar()
        self.memo_var = tk.StringVar()
        
        self.test = 'test'
        
        self.actionTriger = {
            'category': self.add_title_screen,
            'folder': self.add_title_screen,
            'bookmark':self.add_bookmark_screen,
        }
        
        if key == None: return
        self.actionTriger[self.key]()
        
    def add_title_screen(self):
        entry_frame = self.create_entry_frame()
        self.create_title_box(master = entry_frame, textVar = self.name_var, text="新しく追加する名前を入力ください。")
        self.get_btns()
    
    def add_bookmark_screen(self):
        entry_frame = self.create_entry_frame()
        self.create_title_box(master=entry_frame, textVar = self.name_var, text="新しく追加する名前を入力ください。")
        self.create_title_box(entry_frame, self.url_var, text="新しく追加するURLを入力ください。")
        self.memo = self.create_text_box(entry_frame, text="新しく追加するメモを入力ください。")
        self.get_btns()
        
    def create_entry_frame(self):
        entry_frame = tk.Frame(self, bg='#fffdf8')
        entry_frame.pack(pady=(0,50))
        
        return entry_frame
    
    def create_title_box(self, master, textVar, text):
        self.name_label = tk.Label(master, text=text, bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground='#fffdf8', height=2,  font=("HGPｺﾞｼｯｸE", "8", "bold"), foreground='#5B5B5B')
        self.name_label.pack(fill='x', anchor='e', ipady=3)
        
        name_text_box_image = tk.Label(master, image=self.title_box_image, bg='#fffdf8')
        name_text_box_image.pack(fill='x', anchor='w', ipady=5)

        self.name_text_box = tk.Entry(name_text_box_image, textvariable=textVar, bg='white',font=("HGPｺﾞｼｯｸE", "13", "bold"), borderwidth=0)
        self.name_text_box.bind('<Return>', self.on_default)
        self.name_text_box.place(x=23, y=10,width=500, height=45)
        
    def create_text_box(self, master, text):
        memo_label = tk.Label(master, text=text, bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground='#fffdf8', height=2,  font=("HGPｺﾞｼｯｸE", "8", "bold"), foreground='#5B5B5B')
        memo_label.pack(fill='x', anchor='e', ipady=3)
        
        memo_text_box_image = tk.Label(master, image=self.text_box_image, bg='#fffdf8')
        memo_text_box_image.pack(fill='x', anchor='w', ipady=5)

        self.memo_text_box = tk.Text(memo_text_box_image, undo=True, bg='white',font=("HGPｺﾞｼｯｸE", "13", "bold"), borderwidth=0, wrap='word')
        self.memo_text_box.place(x=30, y=10,width=500, height=110)
        
        return self.memo_text_box

    def get_btns(self):
        btn_frame = tk.Frame(self, bg='#fffdf8')
        btn_frame.pack(side='bottom', pady=20, expand=False)
        
        self.submit_btn = tk.Button(btn_frame, image=self.submit_btn_image,command="", cursor='hand2', bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat",)
        self.submit_btn.pack(side='right', padx=(0,10))
    
        self.cancel_btn = tk.Button(btn_frame, image=self.cancel_btn_image,command="", cursor='hand2', bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat",)
        self.cancel_btn.pack(side='left',padx=(10,0))
        
    def get_params(self):
        
        params = {}
        
        if self.key == 'category' or self.key == 'folder':
            params = {'name':self.name_var.get()}

        elif self.key == 'bookmark':

            params = {
                'name':self.name_var.get(),
                'url':self.url_var.get(),
                'memo': self.memo.get('1.0', 'end -1c'),
            }
        
        return params