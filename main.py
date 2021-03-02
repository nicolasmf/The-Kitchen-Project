##=============================================== M A I N =============================================================
# Import
from tkinter import *

# Creation of the window and the canvas
window = Tk()

# Dimension
width = 1000
height= 700
dimension = str(width) +"x"+ str(height)
window.geometry(dimension)

# Title
window.title("The_Kitchen_Project")

# Canvas
can=Canvas(window, bg = "white", width = 1000, height = 700)
can.place(x = 0, y = 0)

# Placing the title
can.create_text(width/2, height*0.05, text = "The Kitchen Project", fill = "black", font = ("Calibri",30))

# Search Bar 

searchBar = Entry(window, width = 20, justify = CENTER)
searchBar.pack()
searchBar.place(relx = 0.5, rely = 0.5, anchor = CENTER)
searchBar.focus()

searchIcon = PhotoImage(file = r"img/magnifier_icon.png").subsample(20, 20)

def SBDelete(*args): # *args to fix window.bind('<Return>', SBDelete) (Will raise an error otherwise) 
    searchBar.delete(0, END)
    return None

buttonSearch = Button(window, image = searchIcon, background = "white", borderwidth = 0, highlightthickness = 0, command = SBDelete)
buttonSearch.pack()
buttonSearch.place(x = 585, y = 337)
window.bind('<Return>', SBDelete) # Binding return key to SBDelete function

# Mainloop
window.mainloop()