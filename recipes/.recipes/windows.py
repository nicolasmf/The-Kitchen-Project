import tkinter as tk
from tkinter import *

root = Tk()
root.title("Recipes")
root.geometry('700x600')


def moelleux_txt():
    text_file = open("recipes\.recipes\Moelleux.txt", 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()


def tarte_txt():
    text_file = open("recipes\.recipes\Tarte_citron.txt", 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()


def muffin_txt():
    text_file = open("recipes\.recipes\Muffins.txt", 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()

def yaourt_txt():
    text_file = open("recipes\.recipes\Gateau_Yaourt.txt", 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()

def far_txt():
    text_file = open("recipes\.recipes\Far_Breton.txt", 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()


my_text = Text(root)
my_text.pack()

open_moelleux = Button(root, text="Moelleux au Chocolat", command=moelleux_txt)
open_moelleux.pack()

open_tarte = Button(root, text="Tarte au Citron", command=tarte_txt)
open_tarte.pack()

open_muffin = Button(root, text="Muffins au Pepites de Chocolat", command=muffin_txt)
open_muffin.pack()

open_yaourt = Button(root, text="Gateau au Yaourt", command=yaourt_txt)
open_yaourt.pack()

open_far = Button(root, text="Far Breton", command=far_txt)
open_far.pack()


root.mainloop()
