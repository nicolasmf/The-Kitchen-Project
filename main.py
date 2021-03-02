##=============================================== M A I N =============================================================
#Import
import tkinter as Tk
#other files
exec(open("./functions.py").read())
exec(open("./classes.py").read())

#Cretion of the window and the canvas
window =Tk.Tk()

#Dimension
width = 1000
height= 700
dimension = str(width) +"x"+ str(height)
window.geometry(dimension)

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
window.mainloop()