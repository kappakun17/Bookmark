from tkwebview2.tkwebview2 import WebView2, have_runtime, install_runtime

# from System.Windows.Forms import Key
if not have_runtime():#没有webview2 runtime
            WebView2.install_runtime()

class my_Webview(WebView2):
    def __init__(self,master=None,url=None):
        WebView2.__init__(self,master,width=800, height=700, url=url);
        self.pack(side='left',fill='both', expand=True)
        
