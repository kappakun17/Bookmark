

def getGeometory(master, window_width, window_height):
    
    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()
    
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))    
    
    return '{}x{}+{}+{}'.format(window_width, window_height, x_cordinate, y_cordinate)