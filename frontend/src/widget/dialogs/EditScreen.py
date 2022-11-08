import tkinter as tk


class my_Dialogs_EditScreen(tk.Frame):
    def __init__(self, master=None, key=None, prev_json = None):
        
        self.title_box_image = tk.PhotoImage(file='frontend/src/img/dialog/actions/title_box.png')
        self.text_box_image = tk.PhotoImage(file='frontend/src/img/dialog/actions/text_box.png')
        self.modify_btn_image = tk.PhotoImage(file='frontend/src/img/dialog/actions/modify_btn.png')
        self.cancel_btn_image = tk.PhotoImage(file='frontend/src/img/dialog/actions/cancel_btn.png')
        
        super().__init__(master);
        self.config(bg='#fffdf8')
        self.pack(anchor='center', pady=(30,0), fill='y')

        # title
        self.key = key
        self.prev_json = prev_json
        self.name_var = tk.StringVar()
        self.url_var = tk.StringVar()
        self.memo_var = tk.StringVar()
        
        if self.key == 'bookmark':
            self.create_edit_screen()
            
    def create_edit_screen(self):
        entry_frame = self.create_entry_frame()
        self.name_label = tk.Label(entry_frame, text="修正する部分だけ、削除し、修正してください。", bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground='#fffdf8', height=2,  font=("HGPｺﾞｼｯｸE", "11", "bold"), foreground='#5B5B5B')
        self.name_label.pack(fill='x', anchor='e', ipady=3)
        
        e_name = self.create_title_box(master=entry_frame, textVar = self.name_var, text="修正する名前を入力ください。")
        e_name.insert(0, self.prev_json['name'])
        e_url = self.create_title_box(entry_frame, self.url_var, text="修正するURLを入力ください。")
        e_url.insert(0, self.prev_json['url'])
        e_memo = self.memo = self.create_text_box(entry_frame, text="修正するメモを入力ください。")
        e_memo.insert(1.0, self.prev_json['memo'])
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
        self.name_text_box.place(x=23, y=10,width=500, height=45)
        
        return self.name_text_box
        
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
        self.modify_btn = tk.Button(btn_frame, image=self.modify_btn_image,command="", cursor='hand2', bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat",)
        self.modify_btn.pack(side='right', padx=(0,10))
    
        self.cancel_btn = tk.Button(btn_frame, image=self.cancel_btn_image,command="", cursor='hand2', bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat",)
        self.cancel_btn.pack(side='left',padx=(10,0))
        
    def get_params(self):
        
        params = {}
        
        if self.key == 'bookmark':

            params = {
                'name':self.name_var.get(),
                'url':self.url_var.get(),
                'memo': self.memo.get('1.0', 'end -1c'),
            }
        
        return params