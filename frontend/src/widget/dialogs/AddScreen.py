import tkinter as tk

class my_Dialogs_AddScreen(tk.Frame):
    def __init__(self, master=None, key=None):
        super().__init__(master);
        self.pack()
        
        self.title_box_image = tk.PhotoImage(file='frontend/src/img/dialog/actions/title_box.png')
        
        # title
        self.key = key
        
        self.actionTriger = {
            'category': self.add_title_screen,
            'folder': self.add_title_screen,
            'bookmark':self.add_bookmark_screen,
        }
        
        if key == None: return
        self.actionTriger[self.key]()
        
    def add_title_screen(self):
        self.get_title_entry() 
    
    def add_bookmark_screen(self):
        pass
    
    def get_title_entry(self):
        title_label = tk.Label(self, text="新しく追加する名前を入力ください。", bg='#fffdf8', borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground='#fffdf8', height=2,  font=("HGPｺﾞｼｯｸE", "8", "bold"), foreground='#5B5B5B')
        title_label.pack(fill='x', anchor='ne', ipady=3)
        
        title_text_box = tk.Entry(self, image=self.title_box_image)
        title_text_box.pack()