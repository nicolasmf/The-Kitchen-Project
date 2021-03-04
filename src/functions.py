## ================================ F U N C T I O N S ==============================================================
"""
File that contains all the functions.

Typo of a function::
def function():
    " " "Function that creates a function that make somthing cool
    " " "
    #Global Variables

    #Variables

    #New variables

    #Core
    (...)
"""
# Import
import tkinter as tk

# Fix warning "global variable is not defined in the global scope"
can = None
searchBar = None
buttonSearch = None
searchIcon = None
window = None
lang = None
language = None
buttonlanguage_en = None
buttonlanguage_fr = None
width, height = None, None

## ======================================================  M a i n m e n u  ======================================================
def mainmenu(width, height):
    """Function that creates and places the main menu, with its button and of the text that comes with it.
    """
    # Variables
        # Global
    global can, searchBar, buttonSearch, searchIcon, window, buttonlanguage_fr, buttonlanguage_en
    # Core
        # Up border
    can.create_rectangle(0, 0, width-2, height*0.20, fill = 'orange', outline = 'white')
        # Title
    can.create_text(width*0.5, height*0.05, text = "The Kitchen Project", fill = "black", font = ("Calibri light",30))
        # Menu
    #m.can.create_text(width*0.25, height*0.7, text="Search a Recipe", fill="black", font=("Calibri",20), anchor="n",justify="center")
    #m.can.create_text(width/2, height*0.4, text="Create a schedule\n(complete meal)", fill="black", font=("Calibri",20), anchor="n",justify="center")
    #m.can.create_text(width*0.75, height*0.7, text="New Ideas\nExplore", fill="black", font=("Calibri",20), anchor="n",justify="center")
        # Search bar
    searchBar.pack()
    searchBar.place(x = width*0.25, y = height*0.13, height=40, anchor ="nw")
    sb_delete()
    searchBar.insert(0, lang.searchbartxt)
    searchBar.bind("<FocusIn>", func=lambda e: searchBar.delete('0', "end")) 
    # \|/ Focus pas obligatoire à l'arrivé du mainmenu
    #searchBar.focus() 
        # Search button
    buttonSearch.pack()
    buttonSearch.place(x = width*0.71, y = height*0.14)
    window.bind('<Return>', sb_delete) # Binding return key to sb_delete function
        # My Profile
    
        # Language parameter
    buttonlanguage_en.pack()
    buttonlanguage_en.place(x=width*0.96, y=height*0.95)
    buttonlanguage_fr.pack()
    buttonlanguage_fr.place(x=width*0.92, y=height*0.95)
    

def delete_canva():
    """Function that deletes all the elements of the Canvas
    """
    global can
    can.delete("all")

# Search bar main menu
def sb_delete(*args): # *args to fix window.bind('<Return>', sb_delete) (Will raise an error otherwise) 
        searchBar.delete(0, "end")
        return None

## ======================================================  C a t e g o r i e s  ======================================================
# Profile
def profile():
    """Function that allows the user to either sign-in or register
    """
    key = 0
    ### global variables

    ### use a key-acces to signup or register

    ###decide if it either in the side bar // new window or specific page that the group wants
#

#

## ====================================================== 

## ======================================================

## ====================================================== Parameters Functions
def reload_mm():
    """Functions that reloads the mainmenu (or allow you to return to mainmenu)
    """
    delete_canva()
    forget_buttons()
    mainmenu(width, height)

def forget_buttons():
    """Functions that erase all the buttons of the canvas
    """
    # M A I N M E N U
    buttonlanguage_en.place_forget()
    buttonlanguage_fr.place_forget()
    buttonSearch.place_forget()
    searchBar.place_forget()

def language_fr():
    """Functions that changes the language to French
    """
    global lang
    lang = language("FR")
    reload_mm()

def language_en():
    """Functions that changes the language to French
    """
    global lang
    lang = language("EN")
    reload_mm()


## ====================================================== Receptive Canvas Functions ( clic & s u c h )
def clic(event):
    """ Function that dispaches what to launch in function of what is activated and how
    """
    # Global Variables

    # Variables
    X = event.x
    Y = event.y
    # New variables

    # Core
