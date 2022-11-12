import tkinter as tk

class my_Dialogs_ConfirmInitializeDBScreen(tk.Frame):
    def __init__(self, master=None):
        
        self.delete_btn_image = tk.PhotoImage(file='frontend/src/img/dialog/actions/delete_btn.png')
        self.cancel_btn_image = tk.PhotoImage(file='frontend/src/img/dialog/actions/cancel_btn.png')
        
        super().__init__(master);
        
        self.config(bg='#fffdf8')
        self.pack(anchor='center', pady=(50,0), fill='y')
        
        self.create_confirm_screen()
        
        
    def create_confirm_screen(self):
        message_frame = self.create_message_frame()
        self.create_message(master=message_frame)
        self.get_btns()
        
    def create_message_frame(self):
        message_frame = tk.Frame(self, bg='#fffdf8')
        message_frame.pack(pady=(0,50))
        
        return message_frame
    
    def create_message(self, master):
        text = "データベースを初期化します。\n問題なければ、削除をクリックしてください。"
        self.message = tk.Label(master, text=text, bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground='#fffdf8', height=2,  font=("HGPｺﾞｼｯｸE", "13", "bold"), foreground='#5B5B5B')
        self.message.pack(fill='x', anchor='e', ipady=3)
        
    
    
    def get_btns(self):
        btn_frame = tk.Frame(self, bg='#fffdf8')
        btn_frame.pack(side='bottom', pady=20, expand=False)
        
        self.delete_btn = tk.Button(btn_frame, image=self.delete_btn_image,command="", cursor='hand2', bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat",)
        self.delete_btn.pack(side='right', padx=(0,10))
    
        self.cancel_btn = tk.Button(btn_frame, image=self.cancel_btn_image,command="", cursor='hand2', bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat",)
        self.cancel_btn.pack(side='left',padx=(10,0))