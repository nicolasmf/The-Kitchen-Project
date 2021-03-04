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

## ========================================================= V A R I A B L E S  &  D E C L A R A T I O N  ============================================= 

# Global variables to be define
    # img
search_icon = tk.PhotoImage(file = r"img/magnifier_icon.png").subsample(20, 20)
favorite_star = tk.PhotoImage(file = r"img/star.png").subsample(20, 20)
    # Search bar
search_bar = tk.Entry(window, width = int(width*0.5/8-1), justify = "center")
    # Button
button_search = tk.Button(window, image = search_icon, background = "white", borderwidth = 0, highlightthickness = 0, command = SBDelete)

## =======================================================
#
# Launch first function (mainmenu)
mainmenu(width, height) # TODO: put the FULL creation of the main menu in the function (To use it when we want to open the main menu again)
#
# Mainloop
window.mainloop()