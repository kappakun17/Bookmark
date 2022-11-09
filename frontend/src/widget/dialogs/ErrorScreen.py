import tkinter as tk


class my_Dialogs_ErrorScreen(tk.Frame):
    def __init__(self, master=None, error=None):

        self.has_no_url_image = tk.PhotoImage(file='frontend/src/img/dialog/actions/has_no_url.png')
        self.cancel_btn_image = tk.PhotoImage(file='frontend/src/img/dialog/actions/cancel_btn.png')
        
        super().__init__(master);
        self.config(bg='#fffdf8')
        self.pack(anchor='center', pady=(50,0), fill='y')


        self.trigerError = {
            'unique':self.unique,
        }

        self.error_image = tk.Label(self, image=self.has_no_url_image, bg='#fffdf8')
        self.error_image.pack(pady= 20)
        
        self.trigerError[error]()

        btn_frame = tk.Frame(self, bg='#fffdf8')
        btn_frame.pack(side='bottom', pady=20, expand=False)

        self.cancel_btn = tk.Button(btn_frame, image=self.cancel_btn_image,command="", cursor='hand2', bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat",)
        self.cancel_btn.pack(pady=20)


    def unique(self):

        self.error_message = 'すでに存在しているカテゴリー名は登録できません。'
        
        self.error_label = tk.Label(self, text=self.error_message, font=("HGPｺﾞｼｯｸE", "13", "bold"), bg='#fffdf8')
        self.error_label.pack(pady=10)
        