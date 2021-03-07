# ========================================== C L A S S E S ==========================================
"""
File that contains all the classes of The_Kitchen_Project.

"""
# === Import
import tkinter as tk
calibri ="Calibri light"

class MainMenu:
    def __init__(self, root, width, height, lang):
        # ================= Root 
        self.root = root
        self.lang= Language(lang)
        # ================= Window parameters =================
        self.can = tk.Canvas(self.root, bg="white",
                             width=width, height=height)
        self.can.place(x=0, y=0)

        # ================= Images initialization =================

        self.search_icon = tk.PhotoImage(
            file=r"img/magnifier_icon.png").subsample(20, 20)
        self.favorite_star = tk.PhotoImage(
            file=r"img/star.png").subsample(20, 20)
        self.schedule_icon = tk.PhotoImage(
            file=r"img/schedule.png").subsample(20, 20)
        # ================= Menu design =================
        # ========== Up border ==========

        self.can.create_rectangle(
            0, 0, width, height*0.20, fill='orange', outline='white')

        # ===== Title =====
        self.can.create_text(width*0.5, height*0.05, text=self.lang.title, fill="black", font=(calibri, 30))

        # ===== Search Bar =====
        self.search_bar = tk.Entry(
            self.root, width=int(width*0.5/8-1), justify="center")
        self.search_bar.pack()
        self.search_bar.place(x=width*0.25, y=height*0.13,
                              height=40, width=height*0.7)
        self.search_bar.insert(0, self.lang.searchbartxt)
        self.search_bar.bind(
            "<FocusIn>", func=lambda e: self.search_bar.delete('0', "end"))
        # ===== Buttons =====
        self.button_search = tk.Button(self.root, image=self.search_icon, background="white",
                                       borderwidth=0, highlightthickness=0, command=self.sb_delete)
        self.button_search.pack()
        # placement
        self.button_search.place(x=width*0.71, y=height*0.14)
        # =========== Schedule Buttons ====
        self.button_schedule = tk.Button(self.root ,image = self.schedule_icon, background="orange",
                                       borderwidth=0, highlightthickness=0, command=self.schedule)
        self.button_schedule.pack()
        self.button_schedule.place(x=width*0.83, y=height*0.10)
        # Binding return key to sb_delete function
        self.root.bind('<Return>', self.sb_delete)

        # ===== Favorite =====
        self.buttonfavorite = tk.Button(self.root, image=self.favorite_star, background="orange",
                                        borderwidth=0, highlightthickness=0, command=self.favoritewindow)
        self.buttonfavorite.pack()
        self.buttonfavorite.place(x=width*0.83, y=height*0.14)
        # ======= Text
        self.can.create_text(width*0.93, height*0.16, text=self.lang.fav,
                             fill="black", font=(calibri, 15))
        self.can.create_text(width*0.93, height*0.12, text=self.lang.schedule,
                             fill="black", font=(calibri, 15))
        # ===== Language =====
        self.buttonlanguage_en = tk.Button(self.root, text="EN", font=(
            "Calibri", 10), background="white", borderwidth=0, highlightthickness=0, command=self.language_en)
        self.buttonlanguage_fr = tk.Button(self.root, text="FR", font=(
            "Calibri", 10), background="white", borderwidth=0, highlightthickness=0, command=self.language_fr)
        self.buttonlanguage_en.pack()
        self.buttonlanguage_en.place(x=width*0.96, y=height*0.95)
        self.buttonlanguage_fr.pack()
        self.buttonlanguage_fr.place(x=width*0.92, y=height*0.95)



    # ================= Functions =================

    def deletecanvas(self):
        """Function that deletes all the elements of the Canvas
        """
        can.delete("all")

    # Search bar main menu
    # Parameter *args is to fix window.bind('<Return>', sb_delete) (Will raise an error otherwise)
    def sb_delete(self, *args):
        self.search_bar.delete(0, "end")

    def favoritewindow(self):
        self.can.destroy()
        Favourites(self.root, 1000, 700, 'EN')
        
    def searchbardelete(self):
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
            MainFrame(tk.Tk(), 1000, 700, 'FR')

    def language_en(self):
        """Function that changes the language to French
        """
        if self.lang.language == 'EN':  # Check if the language is already English
            return
        else:
            self.lang = 'EN'
            self.root.destroy()
            MainFrame(tk.Tk(), 1000, 700, 'EN')
    
    # ====== Funcion Schedule
    def schedule(self):
        """Function that lanches the schedule-page // detroy main menu
        """
        self.can.destroy()
        Schedule(self.root, 1000, 700, self.lang)

# ===================================================================== L A N G U A G E ===============================
class Language():
    """Class that allow the user to change language
    """

    def __init__(self, lang):
        """Initialisation of the class language
        """
        self.lang = lang
        # French
        if lang == "FR":
            #Mainmenu
            self.searchbartxt = "Taper votre recherche ici..."
            self.profile = "Mon profil"
            self.title = "The Kitchen Project"
            self.fav = "Favoris"
            self.back = "Back"
            self.schedule = "Schedule"
            #Schedule
            self.launch = "Lancer la prépartion"
            self.review = "Revoir la prépartion"
                #launch
            self.launch_mode = "Mode de lancement :"
            self.show_list_of_steps = "Afficher les étapes de préparation"
            self.list_mode = "En liste"
            self.step_by_step = "En étape-par-étape"
            self.real_time_mode = "En temps réél"
                #review
            self.view_list_steps = "Afficher les étapes"
            self.edit_list_recipes = "Modifier la liste des recettes"
            self.edit_list_steps = "Modifier les étapes"
            self.specification = "Personnaliser ma cuisine"
        # ==================== English (by default)
        else:
            #Mainmenu
            self.searchbartxt = "Type something here..."
            self.profile = "My profile"
            self.title = "The Kitchen Project"
            self.fav = "Favorites"
            self.back = "Retour"
            self.schedule = "Planning"
            #Schedule
            self.launch = "Launch the preparation"
            self.review = "Review the preparation"
                #launch
            self.launch_mode = "Launch mode :"
            self.show_list_of_steps = "Show the list of steps"
            self.list_mode = "List format"
            self.step_by_step = "Step-by-step"
            self.real_time_mode = "In real time"
                #review
            self.view_list_steps = "View list of steps"
            self.edit_list_recipes = "Edit list of recipes"
            self.edit_list_steps = "Edit list of steps"
            self.specification = "Specify my kitchen"


class Favourites:
    def __init__(self, root, width, height, lang):
        # Initialization of the new canvas
            # basics
        self.root = root
        self.width, self.height = width, height
        self.lang = Language(lang)
        # Canvas
        self.can = tk.Canvas(self.root, bg="white",
                             width=width, height=height)
        self.can.place(x=0, y=0)

        # Buttons
        self.back_mainmenu = tk.Button(self.root, background="orange", text = self.lang.back,
                                        borderwidth=0, highlightthickness=0, command=self.back_mm)
        # Buttons placement
        self.back_mainmenu.pack()
        self.back_mainmenu.place(x=width*0.83, y=height*0.14)
        # Text
        self.can.create_text(width*0.93, height*0.16, text=self.lang.fav,
                             fill="black", font=("Calibri light", 15))
    
    # back to mainmenu
    def back_mm(self):
        self.can.destroy()
        MainMenu(self.root, 1000, 700, 'EN')

# ========================================================== S C H E D U L E =====================================
class Schedule:
    def __init__(self, root, width, height, lang):
        # === Root
        self.root = root
        # === Parameters 
        self.width = width
        self.height = height
        self.lang = Language(lang)
        # === Canvas parameters
        self.can = self.can = tk.Canvas(self.root, bg="white",
                             width=width, height=height)
        self.can.place(x=0, y=0)
        # === Design parameters
        self.can.create_rectangle(0, 0, width, height*0.20, fill='orange', outline='white')
        self.can.create_text(width*0.5, height*0.05, text=self.lang.title, fill="black", font=("Calibri Light", 30))
        # === Image
        self.home_page = tk.PhotoImage(file=r"img/home.png").subsample(20, 20)

        # === Buttons creation
        self.return_home = tk.Button(self.root, font=("Calibri", 10), image=self.home_page, 
            background="white", borderwidth=0, highlightthickness=0, command=self.return_home_f)
            
            # == menu schedule
        self.launch = tk.Button(self.root, font=("Calibri", 10), text=self.lang.launch, 
            background="white", highlightthickness=0, command=self.launch)

        self.review= tk.Button(self.root, font=("Calibri", 10), text=self.lang.review, 
            background="white", highlightthickness=0, command=self.review)
            
            # == sub menu launch
        self.show_list_of_steps = tk.Button(self.root, font=("Calibri", 10), text=self.lang.show_list_of_steps, 
            background="white", highlightthickness=0, command=self.launch)

        self.list_mode = tk.Button(self.root, font=("Calibri", 10), text=self.lang.list_mode, 
            background="white", highlightthickness=0, command=self.launch)

        self.step_by_step_mode = tk.Button(self.root, font=("Calibri", 10), text=self.lang.step_by_step, 
            background="white", highlightthickness=0, command=self.launch)

        self.real_time_mode = tk.Button(self.root, font=("Calibri", 10), text=self.lang.real_time_mode, 
            background="white", highlightthickness=0, command=self.launch)
            
            # == sub menu review
        self.view_list_steps = tk.Button(self.root, font=("Calibri", 10), text=self.lang.view_list_steps, 
            background="white", highlightthickness=0, command=self.launch)

        self.edit_list_recipes = tk.Button(self.root, font=("Calibri", 10), text=self.lang.edit_list_recipes, 
            background="white", highlightthickness=0, command=self.launch)

        self.edit_list_steps = tk.Button(self.root, font=("Calibri", 10), text=self.lang.edit_list_steps, 
            background="white", highlightthickness=0, command=self.launch)

        self.specification = tk.Button(self.root, font=("Calibri", 10), text=self.lang.specification, 
            background="white", highlightthickness=0, command=self.launch)
        
        # === Buttons placement
            #home
        self.return_home.pack()
        self.return_home.place(x= width*0.05, y= height*0.13)
            #menu
        self.launch.pack()
        self.launch.place(x= width*0.5, y= height*0.35, width = 200, height = 50, anchor ="n")
        self.review.pack()
        self.review.place(x= width*0.5, y= height*0.65, width = 200, height = 50, anchor ="n")
        # === Data base analysis

    # === Functions
    def return_home_f (self):
        """Function that allows the user to go on the main page
        """
        self.can.destroy()
        MainMenu(self.root, 1000, 700, self.lang)
    
    # === sub - menu
    def launch(self):
        """Function that launches the sub - menu: Launch
        """
        #Deleting all buttons
        self.hide_buttons(1)
        #Packing
        self.show_list_of_steps.pack()
        self.list_mode.pack()
        self.step_by_step_mode.pack()
        self.real_time_mode.pack()
        #Placing buttons
        self.show_list_of_steps.place(x= self.width*0.5, y= self.height*0.35, width = 200, height = 50, anchor ="n")
        self.list_mode.place(x= self.width*0.5, y= self.height*0.55, width = 200, height = 50, anchor ="n")
        self.step_by_step_mode.place(x= self.width*0.5, y= self.height*0.65, width = 200, height = 50, anchor ="n")
        self.real_time_mode.place(x= self.width*0.5, y= self.height*0.75, width = 200, height = 50, anchor ="n")
        #Text
        self.can.create_text(self.width*0.5, self.height*0.5,font=("Calibri", 15), text =self.lang.launch_mode)

    
    def review(self):
        """Function that launches the sub - menu: Review
        """
        #Deleting allbuttons
        self.hide_buttons(1)
        #Packing
        self.view_list_steps.pack()
        self.edit_list_recipes.pack()
        self.edit_list_steps.pack()
        self.specification.pack()
        #Placing buttons
        self.view_list_steps.place(x= self.width*0.5, y= self.height*0.25, width = 200, height = 50, anchor ="n")
        self.edit_list_recipes.place(x= self.width*0.5, y= self.height*0.45, width = 200, height = 50, anchor ="n")
        self.edit_list_steps.place(x= self.width*0.5, y= self.height*0.55, width = 200, height = 50, anchor ="n")
        self.specification.place(x= self.width*0.5, y= self.height*0.75, width = 200, height = 50, anchor ="n")

    # === Hide buttons function
    def hide_buttons(self, key):
        """Function that hide all the buttons of the Canvas
        """
        if (key == 1):
            # menu schedule
            self.launch.place_forget()
            self.review.place_forget()
        elif (key == 2):
            # sub menu "launch"
            print("1")
        elif (key == 3):
            # sub menu "review"
            print("2")
# ============================================================= MAIN FRAME =================================================
class MainFrame:
    def __init__(self, root, width, height, lang):
        self.root = root
        self.width, self.height = width, height
        self.root.geometry(str(width) + "x" + str(height))
        self.lang = Language(lang)
        self.root.title(self.lang.title)
        self.root.configure(bg='white')
        #self.root.resize()
        # ================= Launching Main
        MainMenu(self.root, width, height, lang)
        # ================= Main Loop =================
        self.root.mainloop()