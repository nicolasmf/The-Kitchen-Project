##=============================================== M A I N =============================================================
#Import
from tkinter import *

#Cretion of the window and the canvas
window =Tk()

#Dimension
width = 1000
height= 700
dimension = str(width) +"x"+ str(height)
window.geometry(dimension)

#Title
window.title("The_Kitchen_Project")

#Canvas
can=Canvas(window,bg="white",width=1000,height=700)
can.place(x=0,y=0)

#Placing the title
can.create_text(width/2, height*0.05, text="The Kitchen Project", fill="black", font=("Calibri",30))

#Mainloop
window.mainloop()