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
##import
import main as m

## ======================================================  M a i n m e n u
def mainmenu(width, height):
    """Function that creates and places the main menu, with its button and of the text that comes with it.
    """
    #Core
        #up border
    m.can.create_rectangle(0,0,width-2,height*0.15, fill='orange',outline='white')
        #title
    m.can.create_text(width*0.5, height*0.075, text="The Kitchen Project", fill="black", font=("Calibri light",30))
        #menu
    m.can.create_text(width*0.25, height*0.7, text="Search a Recipe", fill="black", font=("Calibri",20), anchor="n",justify="center")
    m.can.create_text(width/2, height*0.4, text="Create a schedule\n(complete meal)", fill="black", font=("Calibri",20), anchor="n",justify="center")
    m.can.create_text(width*0.75, height*0.7, text="New Ideas\nExplore", fill="black", font=("Calibri",20), anchor="n",justify="center")

## ======================================================  C a t e g o r i e s
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
    #Global Variables

    #Variables
    X=event.x
    Y=event.y
    #New variables

    #Core
