from tkinter import ttk
import g

def setup():
    ######## Pre-defined Styles ########
    styles = ttk.Style()
    
    styles.configure('labelSmall.TLabel',
                     font=('Arial', 12, 'bold'),
                     background=g.bgColor)
    
    styles.configure('entryMedium.TLabel',
                     font=('Arial', 12, 'bold'))
    
    styles.configure('btnBig.TLabel',
                     font=('Arial', 20, 'bold'),
                     background=g.bgColor)

    

    
    styles.configure('labelTest.TLabel',
                     font=('Arial', 20, 'bold'),
                     background=g.bgColor)
    

    
    
    ### KEYBOAD FONTS
    styles.configure('keyboard.TButton', font=('Verdana', 16, 'bold'))

    return styles