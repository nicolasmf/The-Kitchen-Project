## =============================================== M A I N =============================================================
# Import
import tkinter as tk
# Execute the other files
exec(open("./src/functions.py").read())
exec(open("./src/class.py").read())

# Creation of the window and the canvas
window = tk.Tk()

window.protocol("WM_DELETE_WINDOW", window.destroy())

# Dimension
width = 1000
height = 700
dimension = str(width) +"x"+ str(height)
window.geometry(dimension)

# Title
window.title("The_Kitchen_Project")

# Canvas
can = tk.Canvas(window,bg="white",width=width,height=height)
can.place(x = 0,y = 0)

# To activate binding
#can.bind("<Button-1>",clic)

# Global variables to be define
    # img
searchIcon = tk.PhotoImage(file = r"img/magnifier_icon.png").subsample(20, 20)
searchBar = tk.Entry(window, width = 70, justify = "center")
buttonSearch = tk.Button(window, image = searchIcon, background = "white", borderwidth = 0, highlightthickness = 0, command = SBDelete)

# Launch first function (mainmenu)
mainmenu(width, height)

# Mainloop
window.mainloop()