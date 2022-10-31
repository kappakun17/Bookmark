import tkinter as tk

class my_Dialogs_HasNoUrl(tk.Frame):
    def __init__(self, master=None, url=None):
        
        self.has_no_url_image = tk.PhotoImage(file='frontend/src/img/dialog/actions/has_no_url.png')
        self.return_btn_image = tk.PhotoImage(file='frontend/src/img/dialog/actions/return_btn.png')
        
        super().__init__(master)
        self.configure( bg='#fffdf8')
        self.pack()
        
        self.error_image = tk.Label(self, image=self.has_no_url_image, bg='#fffdf8')
        self.error_image.pack(pady= 20)
        
        self.error_message = url + 'は存在していないようです。'
        
        self.error_label = tk.Label(self, text=self.error_message, font=("HGPｺﾞｼｯｸE", "13", "bold"), bg='#fffdf8')
        self.error_label.pack(pady=10)
        
        self.error_label_2 = tk.Label(self, text='URLを再確認してください。',font=("HGPｺﾞｼｯｸE", "13", "bold"), bg='#fffdf8')
        self.error_label_2.pack(pady=10)
        
        self.return_btn = tk.Button(self, image=self.return_btn_image,command="", cursor='hand2', bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat",)
        self.return_btn.pack(pady=20)
        
        