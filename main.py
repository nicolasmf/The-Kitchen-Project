##=============================================== M A I N =============================================================
<<<<<<< HEAD
#Import
import tkinter as Tk
#other files
exec(open("./functions.py").read())
exec(open("./classes.py").read())

#Cretion of the window and the canvas
window =Tk.Tk()

#Dimension
=======
# Import
from tkinter import *

# Creation of the window and the canvas
window = Tk()

# Dimension
>>>>>>> TKP_vers0.1
width = 1000
height= 700
dimension = str(width) +"x"+ str(height)
window.geometry(dimension)

<<<<<<< HEAD
#Title
window.title("The_Kitchen_Project")

#Canvas
can=Tk.Canvas(window,bg="white",width=width,height=height)
can.place(x=0,y=0)

#Placing the title
mainmenu(width, height)

#To activate binding
#can.bind("<Button-1>",clic)

#Mainloop
=======
# Title
window.title("The_Kitchen_Project")

# Canvas
can=Canvas(window, bg = "white", width = 1000, height = 700)
can.place(x = 0, y = 0)

# Placing the title
can.create_text(width/2, height*0.05, text = "The Kitchen Project", fill = "black", font = ("Calibri",30))

# Search Bar 

searchBar = Entry(window, width = 70, justify = CENTER)
searchBar.pack()
searchBar.place(relx = 0.5, rely = 0.5, anchor = CENTER, height = 50)
searchBar.focus()

searchIcon = PhotoImage(file = r"img/magnifier_icon.png").subsample(20, 20)

def SBDelete(*args): # *args to fix window.bind('<Return>', SBDelete) (Will raise an error otherwise) 
    searchBar.delete(0, END)
    return None

buttonSearch = Button(window, image = searchIcon, background = "white", borderwidth = 0, highlightthickness = 0, command = SBDelete)
buttonSearch.pack()
buttonSearch.place(x = 750, y = 337)
window.bind('<Return>', SBDelete) # Binding return key to SBDelete function

# Mainloop
>>>>>>> TKP_vers0.1
window.mainloop()