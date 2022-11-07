import tkinter as tk

class my_Dialogs_RenameScreen(tk.Frame):
    def __init__(self, master=None, key=None, prev_name=None):
        
        self.title_box_image = tk.PhotoImage(file='frontend/src/img/dialog/actions/title_box.png')
        self.text_box_image = tk.PhotoImage(file='frontend/src/img/dialog/actions/text_box.png')
        self.modify_btn_image = tk.PhotoImage(file='frontend/src/img/dialog/actions/modify_btn.png')
        self.cancel_btn_image = tk.PhotoImage(file='frontend/src/img/dialog/actions/cancel_btn.png')
        
        super().__init__(master);
        self.config(bg='#fffdf8')
        self.pack(anchor='center', pady=(50,0), fill='y')
        
        self.key = key
        self.prev_name = prev_name
        self.name_var = tk.StringVar()
        
        self.actionTriger = {
            'category': self.rename_screen,
            'folder': self.rename_screen,
        }
        
        if self.key in self.actionTriger:
            self.rename_screen()
        
    def rename_screen(self):
        entry_frame = self.create_entry_frame()
        self.create_title_box(master = entry_frame, textVar = self.name_var, text="{}から修正する名前を入力してください。".format(self.prev_name))
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
    
    def get_btns(self):
        btn_frame = tk.Frame(self, bg='#fffdf8')
        btn_frame.pack(side='bottom', pady=20, expand=False)
        self.modify_btn = tk.Button(btn_frame, image=self.modify_btn_image,command="re_render_Webview", cursor='hand2', bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat",)
        self.modify_btn.pack(side='right', padx=(0,10))
    
        self.cancel_btn = tk.Button(btn_frame, image=self.cancel_btn_image,command="re_render_Webview", cursor='hand2', bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat",)
        self.cancel_btn.pack(side='left',padx=(10,0))
    
        
    def get_params(self):
        
        params = {}
        
        params = {'name':self.name_var.get()}

        return params