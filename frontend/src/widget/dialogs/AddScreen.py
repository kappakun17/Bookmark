import tkinter as tk

class my_Dialogs_AddScreen(tk.Frame):
    def __init__(self, master=None, key=None):
        
        self.title_box_image = tk.PhotoImage(file='frontend/src/img/dialog/actions/title_box.png')
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
        
        self.actionTriger = {
            'category': self.add_title_screen,
            'folder': self.add_title_screen,
            'bookmark':self.add_bookmark_screen,
        }
        
        if key == None: return
        self.actionTriger[self.key]()
        
    def add_title_screen(self):
        self.get_title_entry()
        self.get_btns()
    
    def add_bookmark_screen(self):
        self.get_bookmark_entry()
        self.get_btns()
    
    def get_title_entry(self):
        title_entry_frame = tk.Frame(self, bg='#fffdf8')
        title_entry_frame.pack(pady=(0,50))
        title_label = tk.Label(title_entry_frame, text="新しく追加する名前を入力ください。", bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground='#fffdf8', height=2,  font=("HGPｺﾞｼｯｸE", "8", "bold"), foreground='#5B5B5B')
        title_label.pack(fill='x', anchor='e', ipady=3)
        
        title_text_box_image = tk.Label(title_entry_frame, image=self.title_box_image, bg='#fffdf8')
        title_text_box_image.pack(fill='x', anchor='w', ipady=5)

        title_text_box = tk.Entry(title_text_box_image, textvariable=self.name_var, bg='white',font=("HGPｺﾞｼｯｸE", "13", "bold"), borderwidth=0)
        title_text_box.place(x=23, y=10,width=500, height=45)

    def get_bookmark_entry(self):

        title_entry_frame = tk.Frame(self, bg='#fffdf8')
        title_entry_frame.pack(pady=(0,50))
        title_label = tk.Label(title_entry_frame, text="新しく追加する名前を入力ください。", bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground='#fffdf8', height=2,  font=("HGPｺﾞｼｯｸE", "8", "bold"), foreground='#5B5B5B')
        title_label.pack(fill='x', anchor='e', ipady=3)
        
        title_text_box_image = tk.Label(title_entry_frame, image=self.title_box_image, bg='#fffdf8')
        title_text_box_image.pack(fill='x', anchor='w', ipady=5)

        title_text_box = tk.Entry(title_text_box_image, bg='white',font=("HGPｺﾞｼｯｸE", "13", "bold"), borderwidth=0)
        title_text_box.place(x=23, y=10,width=500, height=45)



    def get_btns(self):
        btn_frame = tk.Frame(self, bg='#fffdf8')
        btn_frame.pack(side='bottom', pady=20, expand=False)
        self.submit_btn = tk.Button(btn_frame, image=self.submit_btn_image,command="re_render_Webview", cursor='hand2', bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat",)
        self.submit_btn.pack(side='right', padx=(0,10))
    
        self.cancel_btn = tk.Button(btn_frame, image=self.cancel_btn_image,command="re_render_Webview", cursor='hand2', bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat",)
        self.cancel_btn.pack(side='left',padx=(10,0))
        
    def get_params(self):
        
        params = {}
        
        if self.key == 'category' or self.key == 'folder':
            params = {'name':self.name_var.get()}

        elif self.key == 'bookmark':
            params = {
                'name':self.name_var.get(),
                'url':self.url_var.get(),
                'memo': self.memo_var.get(),
            }
        
        print(params)
        return params