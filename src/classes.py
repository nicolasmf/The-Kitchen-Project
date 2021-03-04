# ========================================== C L A S S E S ==========================================
"""
File that contains all the classes of The_Kitchen_Project.

"""

import tkinter as tk


class MainMenu:
    def __init__(self, root, width, height, lang):

        # ================= Window parameters =================

        self.root = root
        self.root.geometry(str(width) + "x" + str(height))
        self.lang = Language(lang)
        self.root.title(self.lang.title)
        self.root.configure(bg='white')
        self.can = tk.Canvas(self.root, bg="white",
                             width=width, height=height)
        self.can.place(x=0, y=0)

        # ================= Images initialization =================

        self.search_icon = tk.PhotoImage(
            file=r"img/magnifier_icon.png").subsample(20, 20)
        self.favorite_star = tk.PhotoImage(
            file=r"img/star.png").subsample(20, 20)

        # ================= Entries and Buttons initialization =================

        # ================= Menu design =================

        # ========== Up border ==========

        self.can.create_rectangle(
            0, 0, width, height*0.20, fill='orange', outline='white')

        # ===== Title =====
        self.can.create_text(width*0.5, height*0.05, text=self.lang.title,
                             fill="black", font=("Calibri light", 30))

        # ===== Search Bar =====
        self.search_bar = tk.Entry(
            self.root, width=int(width*0.5/8-1), justify="center")
        self.search_bar.pack()
        self.search_bar.place(x=width*0.25, y=height*0.13,
                              height=40, width=height*0.7)
        self.search_bar.insert(0, self.lang.searchbartxt)
        self.search_bar.bind(
            "<FocusIn>", func=lambda e: self.search_bar.delete('0', "end"))

        self.button_search = tk.Button(self.root, image=self.search_icon, background="white",
                                       borderwidth=0, highlightthickness=0, command=self.SBDelete)
        self.button_search.pack()
        self.button_search.place(x=width*0.71, y=height*0.14)

        # Binding return key to SBDelete function
        self.root.bind('<Return>', self.SBDelete)

        # ===== Favorite =====
        self.buttonFavorite = tk.Button(self.root, image=self.favorite_star, background="orange",
                                        borderwidth=0, highlightthickness=0, command=self.favoriteWindow)
        self.buttonFavorite.pack()
        self.buttonFavorite.place(x=width*0.83, y=height*0.14)
        self.can.create_text(width*0.93, height*0.16, text=self.lang.fav,
                             fill="black", font=("Calibri light", 15))

        # ===== Language =====
        self.buttonlanguage_en = tk.Button(self.root, text="EN", font=(
            "Calibri", 10), background="white", borderwidth=0, highlightthickness=0, command=self.language_en)
        self.buttonlanguage_fr = tk.Button(self.root, text="FR", font=(
            "Calibri", 10), background="white", borderwidth=0, highlightthickness=0, command=self.language_fr)
        self.buttonlanguage_en.pack()
        self.buttonlanguage_en.place(x=width*0.96, y=height*0.95)
        self.buttonlanguage_fr.pack()
        self.buttonlanguage_fr.place(x=width*0.92, y=height*0.95)

        # ================= Main Loop =================

        self.root.mainloop()

    # ================= Functions =================

    def deleteCanvas(self):
        """Function that deletes all the elements of the Canvas
        """
        can.delete("all")

    # Search bar main menu
    # Parameter *args is to fix window.bind('<Return>', SBDelete) (Will raise an error otherwise)
    def SBDelete(self, *args):
        self.search_bar.delete(0, "end")

    def favoriteWindow(self):
        self.newWindow = tk.Toplevel(self.root)
        self.newWindow.title("Favorites")
        self.newWindow.geometry("1000x700")

    def searchBarDelete(self):
        """Function to delete what's inside the search bar
        """
        self.search_bar.delete('0', "end")

    def language_fr(self):
        """Function that changes the language to French
        """
        if self.lang.language == 'FR':  # Check if the language is already English
            return
        else:
            self.lang = 'FR'
            self.root.destroy()
            MainMenu(tk.Tk(), 1000, 700, 'FR')

    def language_en(self):
        """Function that changes the language to French
        """
        if self.lang.language == 'EN':  # Check if the language is already English
            return
        else:
            self.lang = 'EN'
            self.root.destroy()
            MainMenu(tk.Tk(), 1000, 700, 'EN')


class Language():
    """Class that allow the user to change language
    """

    def __init__(self, lang):
        """Initialisation of the class language
        """
        self.language = lang
        # French
        if lang == "FR":
            self.searchbartxt = "Taper votre recherche ici..."
            self.profile = "Mon profil"
            self.title = "Le Projet Couisine"
            self.fav = "Favoris"
        # English (by default)
        else:
            self.searchbartxt = "Type something here..."
            self.profile = "My profile"
            self.title = "The Kitchen Project"
            self.fav = "Favorites"
