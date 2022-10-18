import tkinter as tk

class my_NoWebview(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        
        self.GoToEdgeImage = tk.PhotoImage(file='frontend/src/img/webview/goToEdge.png')
        self.GoToEdgeBtnImage = tk.PhotoImage(file='frontend/src/img/webview/goToEdge_btn.png')
        
        
        tk.Frame.__init__(self, master, cnf, **kw)
        
        # add setting for self frame 
        self.configure( bg='#fffdf8')
        
        # image
        self.goToEdgeImage = tk.Label(self, image=self.GoToEdgeImage,bg='#fffdf8')
        self.goToEdgeImage.pack(fill='both')
        
        # button
        self.goToEdgeBtn = tk.Button(
            self,
            image=self.GoToEdgeBtnImage,
            command="openWebview",
            cursor="hand2",
            bg='#fffdf8',
            borderwidth=0,
            highlightthickness=0,
            relief='flat',
            activebackground='#fffdf8',
        )
        self.goToEdgeBtn.pack(fill='both')
        
        # label
        self.goToEdgeLabel = tk.Label(self.goToEdgeBtn, text='Open Webview!',foreground='#fffdf8',bg='#6251FA', font=("MSゴシック", "11", "bold"))
        self.goToEdgeLabel.pack(pady=10)
        # label event
        # self.goToEdgeLabel.bind('<Button-1>')
        

        self.pack(fill='both', pady=(400,400))
        
