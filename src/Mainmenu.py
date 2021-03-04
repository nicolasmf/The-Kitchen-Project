# ========================================== C L A S S E S ====================================
"""
File that contains all the classes of The_Kitchen_Project.

"""
import tkinter as tk


class MainMenu:
    def __init__(self, root, width, height):

        # ================= Window parameters =================

        self.root = root
        self.root.geometry(str(width) + "x" + str(height))
        self.root.title("The Kitchen Project")
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

        self.search_bar = tk.Entry(
            self.root, width=int(width*0.5/8-1), justify="center")

        self.button_search = tk.Button(self.root, image=self.search_icon, background="white",
                                       borderwidth=0, highlightthickness=0, command=self.SBDelete)

        # ================= Menu design =================

        # ========== Up border ==========
        self.can.create_rectangle(
            0, 0, width, height*0.20, fill='orange', outline='white')

        # ===== Title =====
        self.can.create_text(width*0.5, height*0.05, text="The Kitchen Project",
                             fill="black", font=("Calibri light", 30))

        # ===== Search Bar =====
        self.search_bar.pack()
        self.search_bar.place(x=width*0.25, y=height*0.13,
                              height=40, width=height*0.7)
        self.search_bar.insert(0, "Type something here...")
        self.search_bar.bind(
            "<FocusIn>", func=lambda e: self.search_bar.delete('0', "end"))

        self.button_search.pack()
        self.button_search.place(x=width*0.71, y=height*0.14)

        # Binding return key to SBDelete function
        self.root.bind('<Return>', self.SBDelete)

        # ===== Favorite =====
        self.buttonFavorite = tk.Button(self.root, image=self.favorite_star, background="orange",
                                        borderwidth=0, highlightthickness=0, command=self.favoriteWindow)
        self.buttonFavorite.pack()
        self.buttonFavorite.place(x=width*0.83, y=height*0.14)
        self.can.create_text(width*0.93, height*0.16, text="Favorites",
                             fill="black", font=("Calibri light", 15))

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
        self.search_bar.delete('0', "end")