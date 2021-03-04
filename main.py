## =============================================== M A I N =============================================================
# Import
import tkinter as tk
# Execute the other files
exec(open("./src/functions.py").read())
exec(open("./src/class.py").read())

# Creation of the window and the canvas
window = tk.Tk()

# Dimension
width = 1000
height = 700
dimension = str(width) +"x"+ str(height)
window.geometry(dimension)
window.resizable(width = False, height = False)

# Title
window.title("The_Kitchen_Project")

# Canvas
can = tk.Canvas(window, bg = "white", width = width, height = height)
can.place(x = 0, y = 0)

# To activate binding
#can.bind("<Button-1>",clic)

## Language by defaukt (EN)
lang = language("")
## ========================================================= V A R I A B L E S  &  D E C L A R A T I O N  ============================================= 

# Global variables to be define
    # img
searchIcon = tk.PhotoImage(file = r"img/magnifier_icon.png").subsample(20, 20)
    # Search bar
searchBar = tk.Entry(window, width = int((width*0.5/8)-1), justify = "center")
    # Buttons
        # Search
buttonSearch = tk.Button(window, image = searchIcon, background = "white", borderwidth = 0, highlightthickness = 0, command = sb_delete)
        # Language
buttonlanguage_en = tk.Button(window, text = "EN", font = ("Calibri",10), background = "white", borderwidth = 0, highlightthickness = 0, command = language_en)
buttonlanguage_fr = tk.Button(window, text = "FR", font = ("Calibri",10), background = "white", borderwidth = 0, highlightthickness = 0, command = language_fr)
        # Profile
button_profile = tk.Button(window, text = "My profile", font = ("Calibri",10), background = "white", borderwidth = 0, highlightthickness = 0, command = profile)
## =======================================================
#
# Launch first function (mainmenu)
mainmenu(width, height)
#
# Mainloop
window.mainloop()