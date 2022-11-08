import tkinter as tk


class my_SettingsMenu(tk.Frame):
    def __init__(self, master=None, title=None, cnf={}, **kw):
                
        super().__init__(master, cnf, **kw);
        super().configure(bg='#fffdf8')
        
        self.header_label = tk.Label(self, text=title, bg='#6251FA', borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground='#fffdf8', height=2,  font=("HGPｺﾞｼｯｸE", "10", "bold"), foreground='#CACACA')
        self.header_label.pack(fill='x', anchor='ne', pady=(0,20))
        
        self.show_instructions_btn = tk.Button(self, text='アプリの説明を読む', cursor='hand2', bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground='#fffdf8')
        self.show_instructions_btn.pack(fill='x', anchor='ne', padx=10, pady=(0,10))
        
        self.initialize_database_btn = tk.Button(self, text="データベースを初期化",cursor='hand2', bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground='#fffdf8')
        self.initialize_database_btn.pack(fill='x', anchor='ne', padx=10, pady=(10,0))
        
        self.pack(padx=0, fill='x')
