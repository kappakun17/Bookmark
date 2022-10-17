from io import BytesIO
from PIL import ImageTk, Image
from frontend.src.plugin.text.text import textIndention
import tkinter as tk
import favicon
import requests


class my_Bookmark(tk.Canvas):
    def __init__(self, master=None, cnf={}, **kw):
        
        # state
        self.titlename_var = tk.StringVar("");
        self.url_var = tk.StringVar()
        self.memo_var = tk.StringVar("");
        
        # image
        self.BookmarkCardImage = tk.PhotoImage(file="frontend/src/img/bookmark/bookmark_card.png")
        self.BookmarkFaviconImage = self.getUrlImage();
        
        # bookmark card
        tk.Canvas.__init__(self, master, cnf, **kw);
        self.configure(
            width=780,
            height=240,
            bg="#fffdf8",
            highlightthickness=0,
            relief='ridge',
        )
        
        # background image
        self.create_image(0, 0, image=self.BookmarkCardImage, anchor='nw')
        # favicon image
        self.create_image(30, 30, image=self.BookmarkFaviconImage, anchor='nw')
        # title name
        self.create_text(140,45, text="Figma", fill='#6251FA', anchor="nw",font=("HGPｺﾞｼｯｸE", "17", "bold"))
        # url
        self.create_text(140,90, text="https://figma.com", fill='#B9B9B9', anchor="nw",font=("HGPｺﾞｼｯｸE", "10", "bold"))
        # memo
        self.create_text(140,150, text=textIndention("Figmaのホームページです。3.30までに完成し、○○さんへお渡しする。間に合わなかったら、5.1までに渡す。", 35), fill='#6C6C6C', anchor="nw",font=("HGPｺﾞｼｯｸE", "10", "bold"))
        # browser btn
        
        
        
        
        self.pack(padx=(0,0))
        self.config(cursor='hand2')
        # self.bind('<Button-1>', self.test_category)
        
        
    def getUrlImage(self):
        self.url_var.set("https://figma.com/")
        if not self.url_var.get(): return None
        
        icons = favicon.get(self.url_var.get());
        icon = icons[1];
        response = requests.get(icon.url, stream=True)
        img_data = response.content
        re_image_data = Image.open(BytesIO(img_data))
        re_image_data = re_image_data.resize((80,80))
        return ImageTk.PhotoImage(re_image_data)
            
            
            