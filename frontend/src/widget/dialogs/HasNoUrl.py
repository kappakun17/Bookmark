import tkinter as tk

class my_Dialogs_HasNoUrl(tk.Frame):
    def __init__(self, master=None, db_params=None):
        
        self.has_no_url_image = tk.PhotoImage(file='frontend/src/img/dialog/actions/has_no_url.png')
        self.submit_btn_image = tk.PhotoImage(file='frontend/src/img/dialog/actions/submit_btn.png')
        self.return_btn_image = tk.PhotoImage(file='frontend/src/img/dialog/actions/return_btn.png')
        
        super().__init__(master)
        self.configure( bg='#fffdf8')
        self.pack()

        self.db_params = db_params
        
        self.error_image = tk.Label(self, image=self.has_no_url_image, bg='#fffdf8')
        self.error_image.pack(pady= 20)
        
        self.error_message = self.db_params['url'] + 'は\nアクセス権限が必要なページか存在していないようです。'
        
        self.error_label = tk.Label(self, text=self.error_message, font=("HGPｺﾞｼｯｸE", "13", "bold"), bg='#fffdf8')
        self.error_label.pack(pady=10)
        
        self.error_label_2 = tk.Label(self, text='それでも登録する場合は、登録をクリックしてください。',font=("HGPｺﾞｼｯｸE", "13", "bold"), bg='#fffdf8')
        self.error_label_2.pack(pady=10)

        btn_frame = tk.Frame(self, bg='#fffdf8')
        btn_frame.pack(side='bottom', pady=20, expand=False)
        
        self.submit_btn = tk.Button(btn_frame, image=self.submit_btn_image,command="", cursor='hand2', bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat",)
        self.submit_btn.pack(side='right', padx=(0,10))

        self.return_btn = tk.Button(btn_frame, image=self.return_btn_image,command="", cursor='hand2', bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat",)
        self.return_btn.pack(pady=20)


    def get_params(self):
        return self.db_params