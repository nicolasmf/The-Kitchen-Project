## ================================ F U N C T I O N S ==============================================================
"""
File that contains all the functions.

Typo of a function::
def function():
    " " "Function that creates a function that make something cool
    " " "
    #Global Variables

    #Variables

    #New variables

    #Core
    (...)
"""
# Imports
import main as m
import tkinter as tk

# Solve warning "global declared variable is not declared in the global scope"
searchBar = None
buttonSearch = None
searchIcon = None 
can = None

## ======================================================  M a i n m e n u  ======================================================
def mainmenu(width, height):
    """Function that creates and places the main menu, with its button and the text that comes with it.
    """
    # Variables
        # Global
    global searchBar, buttonSearch, searchIcon
    # Core
        # Up border
    #m.can.create_rectangle(0,0,width-2,height*0.15, fill = 'orange', outline = 'white')
        # Title
    #m.can.create_text(width*0.5, height*0.075, text = "The Kitchen Project", fill = "black", font = ("Calibri light",30))
        # Menu
    #m.can.create_text(width*0.25, height*0.7, text="Search a Recipe", fill="black", font=("Calibri",20), anchor="n",justify="center")
    #m.can.create_text(width/2, height*0.4, text="Create a schedule\n(complete meal)", fill="black", font=("Calibri",20), anchor="n",justify="center")
    #m.can.create_text(width*0.75, height*0.7, text="New Ideas\nExplore", fill="black", font=("Calibri",20), anchor="n",justify="center")
        # Search bar
    searchBar.pack()
    searchBar.place(x = width*0.25, y = height*0.15 , height = 40, width= height*0.7)
    searchBar.focus()
        # Image
    buttonSearch.pack()
    buttonSearch.place(x = width*0.71, y = height*0.15+5)
    m.window.bind('<Return>', SBDelete) # Binding return key to SBDelete function

def deleteCanvas():
    """Function that deletes all the elements of the Canvas
    """
    global can
    can.delete("all")

# Search bar main menu
def SBDelete(*args): # *args to fix window.bind('<Return>', SBDelete) (Will raise an error otherwise) 
        searchBar.delete(0, "end")
        return None

## ======================================================  C a t e g o r i e s  ======================================================
#

#

#

## ====================================================== 

## ======================================================

## ======================================================

## ====================================================== Active Function
def clic(event):
    """ Function that dispaches what to launch in function of what is activated and how
    """
    # Global Variables

    # Variables
    X=event.x
    Y=event.y

    # New variables

    # Core
