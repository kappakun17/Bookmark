import tkinter as tk
from tkinter import Frame
from tkscrolledframe import ScrolledFrame

class ScrolledFrameForLeft(ScrolledFrame):
    def __init__(self, master=None, **kw):
        ScrolledFrame.__init__(self, master, use_ttk=True, **kw);
        
        self._canvas.configure(bg='#fffdf8')
        self.config(
                        width=500, 
                        cursor='hand2', 
                        height=self.master.winfo_screenheight(), 
                        bg='#fffdf8', 
                        bd=0,
                    )
        self.pack()
        
        self.bind_arrow_keys(self.master)
        self.bind_scroll_wheel(self.master)
        self.inner_frame = self.display_widget(Frame,fit_width=False,bg='#fffdf8')