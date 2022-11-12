import tkinter as tk


class my_Dialogs_ErrorScreen(tk.Frame):
    def __init__(self, master=None, error=None):

        self.has_no_url_image = tk.PhotoImage(file='frontend/src/img/dialog/actions/has_no_url.png')
        self.return_btn_image = tk.PhotoImage(file='frontend/src/img/dialog/actions/return_btn.png')
        
        super().__init__(master);
        self.config(bg='#fffdf8')
        self.pack(anchor='center', pady=(50,0), fill='y')


        self.trigerError = {
            'unique':self.unique,
            'network':self.network,
            'no_name':self.no_name,
            'no_url':self.no_url,
            'no_category_and_folder':self.no_cf,
        }

        self.error_image = tk.Label(self, image=self.has_no_url_image, bg='#fffdf8')
        self.error_image.pack(pady= 20)
        
        self.trigerError[error]()

        btn_frame = tk.Frame(self, bg='#fffdf8')
        btn_frame.pack(side='bottom', pady=20, expand=False)

        self.return_btn = tk.Button(btn_frame, image=self.return_btn_image,command="", cursor='hand2', bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat",)
        self.return_btn.pack(pady=20)


    def unique(self):

        self.error_message = 'すでに存在しているカテゴリー名は登録できません。'
        
        self.error_label = tk.Label(self, text=self.error_message, font=("HGPｺﾞｼｯｸE", "13", "bold"), bg='#fffdf8')
        self.error_label.pack(pady=10)
        
    def network(self):
        self.error_message = 'ネットワークがオフラインのようです。\nネットワーク接続を確認してください。'
        
        self.error_label = tk.Label(self, text=self.error_message, font=("HGPｺﾞｼｯｸE", "13", "bold"), bg='#fffdf8')
        self.error_label.pack(pady=10)
        
    def no_name(self):
        self.error_message = '名前の入力が未記入のようです。\n名前を付けてください。'
        
        self.error_label = tk.Label(self, text=self.error_message, font=("HGPｺﾞｼｯｸE", "13", "bold"), bg='#fffdf8')
        self.error_label.pack(pady=10)
        
        
    def no_url(self):
        self.error_message = 'URLの入力が未記入のようです。\nURLを登録してください。'
        
        self.error_label = tk.Label(self, text=self.error_message, font=("HGPｺﾞｼｯｸE", "13", "bold"), bg='#fffdf8')
        self.error_label.pack(pady=10)
        
    def no_cf(self):
        self.error_message = 'カテゴリーとフォルダ―の作成がまだのようです。\nカテゴリーとフォルダ―を作成してください。'
        
        self.error_label = tk.Label(self, text=self.error_message, font=("HGPｺﾞｼｯｸE", "13", "bold"), bg='#fffdf8')
        self.error_label.pack(pady=10)