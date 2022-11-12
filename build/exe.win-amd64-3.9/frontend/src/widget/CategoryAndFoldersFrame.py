import tkinter as tk
from frontend.src.widget.Category import my_Category

import logging
logger = logging.getLogger(__name__)



class my_CategoryAndFoldersFrame(tk.Frame):
    
    def __init__(self, master=None, category=None, cnf={}, **kw):
        
        tk.Frame.__init__(self, master, cnf, **kw)
        self.configure(
            bg='#fffdf8'
        )
        self.pack(anchor="e", pady=10);
        
        self.category = None
        logger.debug('Created the category and folders frame.')
        
    def set_category(self, category):
        self.category = category