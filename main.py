from frontend.src.main import go
from System.Threading import Thread,ApartmentState,ThreadStart
import clr
clr.AddReference("System.Windows.Forms")
# from threading import Thread

# import ctypes
# ctypes.windll.ole32.Coinitialize()

import gc
# start the path from Bookmark/
import sys
sys.path.append('.../')

if __name__=="__main__":

    t = Thread(ThreadStart(go))
    t.ApartmentState = ApartmentState.STA
    t.Start()
    t.Join()
    
    gc.collect()
