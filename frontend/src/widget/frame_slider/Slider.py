import tkinter as tk

class my_Slider(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        tk.Frame.__init__(self, master, cnf, **kw)
        
        self.configure(height=80, bg='#6251FA')
 
        self.pack(anchor='nw', side='top', fill='x', pady=(0,0))
        
        self.l_side = tk.Frame(self.master, height=5, bg='#666666')
        self.l_side.pack(anchor='nw', side='top', fill='x', pady=(0,20))
        
        self.sliderbar = tk.Button(self.master, width=1, height=self.master.winfo_screenheight(), cursor='sb_h_double_arrow', bg='#6251FA',activebackground='#AB77FF',relief = "flat",)
        self.sliderbar.pack(anchor='nw', side='top', fill='y')
 

        
        