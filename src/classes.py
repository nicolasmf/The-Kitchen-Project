# ========================================== C L A S S E S ==========================================
"""
File that contains all the classes of The_Kitchen_Project.

"""
# === Import
import tkinter as tk
calibri = "Calibri light"


class MainMenu:
    def __init__(self, root, width, height, lang, list):
        # ================= Root =================
        # ================= Root
        self.root = root
        self.lang = Language(lang)
        self.width = width
        self.height = height
        # ================= Window parameters =================
        self.can = tk.Canvas(self.root, bg="white",
                             width=self.width, height=self.height)
        self.can.place(x=0, y=0)

        # ================= Images initialization =================

        self.search_icon = tk.PhotoImage(
            file=r"img/magnifier_icon.png").subsample(20, 20)
        self.favorite_star = tk.PhotoImage(
            file=r"img/star.png").subsample(20, 20)
        self.schedule_icon = tk.PhotoImage(
            file=r"img/schedule.png")
        # ================= Menu design =================
        # ========== Up border ==========

        self.can.create_rectangle(
            0, 0, self.width, self.height*0.20, fill='orange', outline='white')

        # ===== Title =====
        self.can.create_text(self.width*0.5, self.height*0.05,
                             text=self.lang.title, fill="black", font=(calibri, 30))

        # ===== Search Bar =====
        self.search_bar = tk.Entry(
            self.root, width=int(self.width*0.5/8-1), justify="center")
        self.search_bar.pack()
        self.search_bar.place(x=self.width*0.25, y=self.height*0.13,
                              height=40, width=self.height*0.7)
        self.search_bar.insert(0, self.lang.searchbartxt)
        self.search_bar.bind(
            "<FocusIn>", func=lambda e: self.search_bar.delete('0', "end"))
        # ===== Buttons =====
        self.button_search = tk.Button(self.root, image=self.search_icon, background="white",
                                       borderwidth=0, highlightthickness=0, command=self.sb_delete)
        self.button_search.pack()
        # placement
        self.button_search.place(x=self.width*0.71, y=self.height*0.14)
        # =========== Schedule Buttons ====
        self.button_schedule = tk.Button(self.root, image=self.schedule_icon, background="orange",
                                         borderwidth=0, highlightthickness=0, command=self.schedule)
        self.button_schedule.pack()
        self.button_schedule.place(x=self.width*0.83, y=self.height*0.10)
        # Binding return key to sb_delete function
        self.root.bind('<Return>', self.sb_delete)

        # ===== Favorite =====
        self.buttonfavorite = tk.Button(self.root, image=self.favorite_star, background="orange",
                                        borderwidth=0, highlightthickness=0, command=self.favoritewindow)
        self.buttonfavorite.pack()
        self.buttonfavorite.place(x=self.width*0.83, y=self.height*0.14)
        # ======= Text
        self.can.create_text(self.width*0.93, self.height*0.16, text=self.lang.fav,
                             fill="black", font=(calibri, 15))
        self.can.create_text(self.width*0.93, self.height*0.12, text=self.lang.schedule,
                             fill="black", font=(calibri, 15))
        # ===== Language =====

        self.buttonlanguage_en = tk.Button(self.root, text="EN", font=(
            "Calibri", 10), background="white", borderwidth=0, highlightthickness=0, command=self.language_en)
        self.buttonlanguage_fr = tk.Button(self.root, text="FR", font=(
            "Calibri", 10), background="white", borderwidth=0, highlightthickness=0, command=self.language_fr)
        self.buttonlanguage_en.pack()
        self.buttonlanguage_en.place(x=self.width*0.96, y=self.height*0.95)
        self.buttonlanguage_fr.pack()
        self.buttonlanguage_fr.place(x=self.width*0.92, y=self.height*0.95)

        # === LIST OF RECIPIES
        self.list = list
        # === Recipes buttons ===
        self.button_moelleux = tk.Button(self.root, text=self.lang.add_word + self.lang.moelleux + self.lang.add_word2, font=(
            "Calibri", 10), background="white", borderwidth=0, highlightthickness=0, command=self.f_moelleux)

        self.button_pie = tk.Button(self.root, text=self.lang.add_word + self.lang.pie + self.lang.add_word2, font=(
            "Calibri", 10), background="white", borderwidth=0, highlightthickness=0, command=self.f_pie)

        self.button_muffin = tk.Button(self.root, text=self.lang.add_word + self.lang.muffin + self.lang.add_word2, font=(
            "Calibri", 10), background="white", borderwidth=0, highlightthickness=0, command=self.f_muffin)

        self.button_yogurt = tk.Button(self.root, text=self.lang.add_word + self.lang.yogurt + self.lang.add_word2, font=(
            "Calibri", 10), background="white", borderwidth=0, highlightthickness=0, command=self.f_yogurt)

        self.button_far = tk.Button(self.root, text=self.lang.add_word + self.lang.far + self.lang.add_word2, font=(
            "Calibri", 10), background="white", borderwidth=0, highlightthickness=0, command=self.f_far)
        # = pack ===
        self.button_moelleux.pack()
        self.button_pie.pack()
        self.button_muffin.pack()
        self.button_yogurt.pack()
        self.button_far.pack()
        # = Place
        self.button_moelleux.place(
            x=self.width*0.5, y=self.height*0.35, anchor='n')
        self.button_pie.place(x=self.width*0.5, y=self.height*0.45, anchor='n')
        self.button_muffin.place(
            x=self.width*0.5, y=self.height*0.55, anchor='n')
        self.button_yogurt.place(
            x=self.width*0.5, y=self.height*0.65, anchor='n')
        self.button_far.place(x=self.width*0.5, y=self.height*0.75, anchor='n')
        # = Effect (when return home)
        if self.if_exists('Moelleux'):
            self.button_moelleux.config(
                relief="sunken", background='#CFD8DC', borderwidth=2)
        if self.if_exists('Tarte_au_citron'):
            self.button_pie.config(
                relief="sunken", background='#CFD8DC', borderwidth=2)
        if self.if_exists('Muffins'):
            self.button_muffin.config(
                relief="sunken", background='#CFD8DC', borderwidth=2)
        if self.if_exists('Gateau_Yaourt'):
            self.button_yogurt.config(
                relief="sunken", background='#CFD8DC', borderwidth=2)
        if self.if_exists('Far_Breton'):
            self.button_far.config(
                relief="sunken", background='#CFD8DC', borderwidth=2)
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
        Favourites(self.root, 1000, 700, 'EN', self.list)

    def searchbardelete(self):
        """Function to delete what's inside the search bar
        """
        self.search_bar.delete('0', "end")

    def language_fr(self):
        """Function that changes the language to French
        """
        if self.lang.lang == 'FR':  # Check if the language is already English
            return
        else:
            self.root.destroy()
            MainFrame(tk.Tk(), self.width, self.height, 'FR')

    def language_en(self):
        """Function that changes the language to French
        """
        if self.lang.lang == 'EN':  # Check if the language is already English
            return
        else:
            self.root.destroy()
            MainFrame(tk.Tk(), 1000, 700, 'EN')

    # ====== Function recipes
    def f_moelleux(self):
        """ add the moelleux to the list if it ain't already there
        """
        if not self.if_exists('Moelleux'):
            self.list.append('Moelleux')
        self.button_moelleux.config(
            relief="sunken", background='#CFD8DC', borderwidth=2)

    def f_pie(self):
        """ add the pieto the list if it ain't already there
        """
        if not self.if_exists('Tarte_au_citron'):
            self.list.append('Tarte_au_citron')
        self.button_pie.config(
            relief="sunken", background='#CFD8DC', borderwidth=2)

    def f_muffin(self):
        """ add the muffin to the list if it ain't already there
        """
        if not self.if_exists('Muffins'):
            self.list.append('Muffins')
        self.button_muffin.config(
            relief="sunken", background='#CFD8DC', borderwidth=2)

    def f_yogurt(self):
        """ add the yogurt to the list if it ain't already there
        """
        if not self.if_exists('Gateau_Yaourt'):
            self.list.append('Gateau_Yaourt')
        self.button_yogurt.config(
            relief="sunken", background='#CFD8DC', borderwidth=2)

    def f_far(self):
        """ add the far to the list if it ain't already there
        """
        if not self.if_exists('Far_Breton'):
            self.list.append('Far_Breton')
        self.button_far.config(
            relief="sunken", background='#CFD8DC', borderwidth=2)

    # ====== Funcion Schedule
    def schedule(self):
        """Function that lanches the schedule-page // detroy main menu
        """
        self.can.destroy()
        Schedule(self.root, self.width, self.height, self.lang.lang, self.list)

    def if_exists(self, target):
        """ Function that return 1 if 'it' exists in the list, 0 if not
        """
        end = 0
        while end < len(self.list):
            if self.list[end] == target:
                return 1
            else:
                end += 1
        return 0

# ===================================================================== L A N G U A G E ===============================


class Language():
    """Class that allow the user to change language
    """

    def __init__(self, lang):
        """Initialisation of the class language
        """
        self.lang = lang
        # French
        if self.lang == "FR":
            # Mainmenu
            self.searchbartxt = "Taper votre recherche ici..."
            self.profile = "Mon profil"
            self.title = "The Kitchen Project"
            self.fav = "Favoris"
            self.back = "Retour"
            self.next = "Prochain"
            self.back_menu = "Retour au menu"
            self.schedule = "Planning"
            # Schedule
            self.launch = "Lancer la prépartion"
            self.review = "Revoir la prépartion"
            # Recipes
            self.add_word = "Ajouter "
            self.add_word2 = " à la liste"
            self.moelleux = "Moelleux"
            self.pie = "Tarte au citron"
            self.muffin = "Muffin"
            self.yogurt = "Gateau au yahourt"
            self.far = "Far Breton"
            # launch
            self.launch_mode = "Modes de lancement :"
            self.display_mode = "Affichage :"
            self.show_list_of_steps = "Afficher les étapes de préparation"
            self.list_mode = "En liste"
            self.step_by_step = "En étape-par-étape"
            self.real_time_mode = "En temps réél"
            # review
            self.review_mode_1 = "Afficher avant préparation"
            self.review_mode_2 = "Modifier avant préparation"
            self.review_mode_3 = "Spécifier ma cuisine avant de commencer"
            self.view_list_steps = "Afficher les étapes"
            self.edit_list_recipes = "Modifier la liste des recettes"
            self.edit_list_steps = "Modifier les étapes"
            self.specification = "Personnaliser ma cuisine"
            # vocab
            self.step = "étape"
            self.previous = "Etape précédente"
            self.finish = "Finis!"
        # English (by default)
        elif self.lang == "EN":
            # Mainmenu
            self.searchbartxt = "Type something here..."
            self.profile = "My profile"
            self.title = "The Kitchen Project"
            self.fav = "Favorites"
            self.back = "Back"
            self.next = "Next"
            self.back_menu = "Back to menu"
            self.schedule = "Schedule"
            # Schedule
            self.launch = "Launch the preparation"
            self.review = "Review the preparation"
            # Recipes
            self.add_word = "Add "
            self.add_word2 = " to the list"
            self.moelleux = "Fondant"
            self.pie = "Lemon pie"
            self.muffin = "Muffin"
            self.yogurt = "Yogurt cake"
            self.far = "Far Breton"
            # launch
            self.launch_mode = "Launch modes :"
            self.display_mode = "Displaying :"
            self.show_list_of_steps = "Show the list of steps"
            self.list_mode = "List format"
            self.step_by_step = "Step-by-step"
            self.real_time_mode = "In real time"
            # review
            self.review_mode_1 = "View before preparation"
            self.review_mode_2 = "Edit before preparation"
            self.review_mode_3 = "Specify your kitchen before preparation"
            self.view_list_steps = "View list of steps"
            self.edit_list_recipes = "Edit list of recipes"
            self.edit_list_steps = "Edit list of steps"
            self.specification = "Specify my kitchen"
            # vocab
            self.step = "step"
            self.previous = "Previous step"
            self.finish = "Finished !"
        else:
            # Fatal error
            print("E  R  R  O  R      L A N G")


class Favourites:
    def __init__(self, root, width, height, lang, list):
        # Initialization of the new canvas
        # basics
        self.root = root
        self.width, self.height = width, height
        self.lang = Language(lang)
        self.list = list
        # Canvas
        self.can = tk.Canvas(self.root, bg="white",
                             width=width, height=height)
        self.can.place(x=0, y=0)

        # Buttons
        self.back_mainmenu = tk.Button(self.root, background="orange", text=self.lang.back,
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
        MainMenu(self.root, 1000, 700, self.lang.lang, self.list)

# ========================================================== S C H E D U L E =====================================


class Schedule:
    """ Class Schedule (that'll redirect to another sub-class in function of the mode chosen)
    """

    def __init__(self, root, width, height, lang, list):
        # === Root
        self.root = root
        # === Parameters
        self.width = width
        self.height = height
        self.lang = Language(lang)
        # list
        self.list = list
        # === Canvas parameters
        self.can = self.can = tk.Canvas(self.root, bg="white",
                                        width=width, height=height)
        self.can.place(x=0, y=0)
        # === Design parameters
        self.can.create_rectangle(
            0, 0, self.width, self.height*0.20, fill='orange', outline='white')
        self.can.create_text(self.width*0.5, self.height*0.05,
                             text=self.lang.title, fill="black", font=("Calibri Light", 30))
        # === Image
        self.home_page = tk.PhotoImage(file=r"img/home.png").subsample(20, 20)

        # === Buttons creation
        self.return_home = tk.Button(self.root, font=("Calibri", 10), image=self.home_page,
                                     background="white", borderwidth=0, highlightthickness=0, command=self.return_home_f)

        self.back_r = tk.Button(self.root, font=("Calibri", 10), text=self.lang.back,
                                background="white", borderwidth=0, highlightthickness=0, command=self.back_r_f)

        self.back_l = tk.Button(self.root, font=("Calibri", 10), text=self.lang.back,
                                background="white", borderwidth=0, highlightthickness=0, command=self.back_l_f)

        # == menu schedule
        self.launch = tk.Button(self.root, font=("Calibri", 10), text=self.lang.launch,
                                background="white", highlightthickness=0, command=self.launch_f)

        self.review = tk.Button(self.root, font=("Calibri", 10), text=self.lang.review,
                                background="white", highlightthickness=0, command=self.review_f)

        # == sub menu launch
        self.show_list_of_steps = tk.Button(self.root, font=("Calibri", 10), text=self.lang.show_list_of_steps,
                                            background="white", highlightthickness=0, command=self.show_list_of_steps_f)

        self.list_mode = tk.Button(self.root, font=("Calibri", 10), text=self.lang.list_mode,
                                   background="white", highlightthickness=0, command=self.list_mode_f)

        self.step_by_step_mode = tk.Button(self.root, font=("Calibri", 10), text=self.lang.step_by_step,
                                           background="white", highlightthickness=0, command=self.step_by_step_mode_f)

        self.real_time_mode = tk.Button(self.root, font=("Calibri", 10), text=self.lang.real_time_mode,
                                        background="white", highlightthickness=0, command=self.real_time_mode_f)

        self.text_temp = 0
        # == sub menu review
        self.view_list_steps = tk.Button(self.root, font=("Calibri", 10), text=self.lang.view_list_steps,
                                         background="white", highlightthickness=0, command=self.view_list_steps_f)

        self.edit_list_recipes = tk.Button(self.root, font=("Calibri", 10), text=self.lang.edit_list_recipes,
                                           background="white", highlightthickness=0, command=self.edit_list_recipes_f)

        self.edit_list_steps = tk.Button(self.root, font=("Calibri", 10), text=self.lang.edit_list_steps,
                                         background="white", highlightthickness=0, command=self.edit_list_step_f)

        self.specification = tk.Button(self.root, font=("Calibri", 10), text=self.lang.specification,
                                       background="white", highlightthickness=0, command=self.specification_f)

        # === Buttons placement
        # home
        self.return_home.pack()
        self.return_home.place(x=self.width*0.05, y=height*0.13)
        # menu
        self.launch.pack()
        self.launch.place(x=self.width*0.5, y=self.height *
                          0.35, width=200, height=50, anchor="n")
        self.review.pack()
        self.review.place(x=self.width*0.5, y=self.height *
                          0.65, width=200, height=50, anchor="n")
        # === Data base analysis

    # ========================================================================== Functions
    def return_home_f(self):
        """Function that allows the user to go on the main page
        """
        self.can.destroy()
        MainMenu(self.root, 1000, 700, self.lang.lang, self.list)

    def back_l_f(self):
        """ Function that allows the user to go back on the main menu schedule
        """
        # Deleting all buttons
        self.hide_buttons(2)
        # Placing the buttons
        self.place_all_buttons(3)

    def back_r_f(self):
        """ Function that allows the user to go back on the main menu schedule
        """
        # Deleting all buttons
        self.hide_buttons(3)
        # Placing the buttons
        self.place_all_buttons(3)

    # === sub - menu
    def launch_f(self):
        """Function that launches the sub - menu: Launch
        """
        # Deleting all buttons
        self.hide_buttons(1)
        self.place_all_buttons(1)
        # Text
        self.text_temp = (self.can.create_text(self.width*0.5, self.height*0.475, font=("Calibri", 15), text=self.lang.launch_mode),
                          self.can.create_text(self.width*0.5, self.height*0.275, font=("Calibri", 15), text=self.lang.display_mode))

    def review_f(self):
        """Function that launches the sub - menu: Review
        """
        # Deleting allbuttons
        self.hide_buttons(1)
        self.place_all_buttons(2)
        # Text
        self.text_temp = (self.can.create_text(self.width*0.5, self.height*0.25, font=("Calibri", 15), text=self.lang.review_mode_1),
                          self.can.create_text(
                              self.width*0.5, self.height*0.46, font=("Calibri", 15), text=self.lang.review_mode_2),
                          self.can.create_text(self.width*0.5, self.height*0.80, font=("Calibri", 15), text=self.lang.review_mode_3))

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
            self.show_list_of_steps.place_forget()
            self.list_mode.place_forget()
            self.step_by_step_mode.place_forget()
            self.real_time_mode.place_forget()
            self.back_l.place_forget()
            self.can.delete(self.text_temp[0], self.text_temp[1])
        elif (key == 3):
            # sub menu "review"
            self.view_list_steps.place_forget()
            self.edit_list_recipes.place_forget()
            self.edit_list_steps.place_forget()
            self.specification.place_forget()
            self.back_r.place_forget()
            self.can.delete(self.text_temp[0],
                            self.text_temp[1], self.text_temp[2])

    def place_all_buttons(self, key):
        """Function that places the buttons in function of the key
        """
        if (key == 1):  # Launch
            # Packing
            self.show_list_of_steps.pack()
            self.list_mode.pack()
            self.step_by_step_mode.pack()
            self.real_time_mode.pack()
            self.back_l.pack()
            # Placing buttons
            self.show_list_of_steps.place(
                x=self.width*0.5, y=self.height*0.35, width=250, height=50, anchor="n")
            self.list_mode.place(
                x=self.width*0.5, y=self.height*0.55, width=250, height=50, anchor="n")
            self.step_by_step_mode.place(
                x=self.width*0.5, y=self.height*0.65, width=250, height=50, anchor="n")
            self.real_time_mode.place(
                x=self.width*0.5, y=self.height*0.75, width=250, height=50, anchor="n")
            self.back_l.place(x=self.width*0.75, y=self.height *
                              0.90, width=70, height=50, anchor="n")
        elif (key == 2):  # Review
            # Packing
            self.view_list_steps.pack()
            self.edit_list_recipes.pack()
            self.edit_list_steps.pack()
            self.specification.pack()
            self.back_r.pack()
            # Placing buttons
            self.view_list_steps.place(
                x=self.width*0.5, y=self.height*0.30, width=250, height=50, anchor="n")
            self.edit_list_recipes.place(
                x=self.width*0.5, y=self.height*0.50, width=250, height=50, anchor="n")
            self.edit_list_steps.place(
                x=self.width*0.5, y=self.height*0.60, width=250, height=50, anchor="n")
            self.specification.place(
                x=self.width*0.5, y=self.height*0.85, width=250, height=50, anchor="n")
            self.back_r.place(x=self.width*0.75, y=self.height *
                              0.90, width=70, height=50, anchor="n")
        elif (key == 3):  # Menu
            # self.launch.pack()
            self.launch.place(x=self.width*0.5, y=self.height *
                              0.35, width=200, height=50, anchor="n")
            self.review.pack()
            self.review.place(x=self.width*0.5, y=self.height *
                              0.65, width=200, height=50, anchor="n")

    # ========================================= R E D I R E C T
        # ================== LAUNCH
    def show_list_of_steps_f(self):
        """ Function that allow the user to view the list of steps that they will follow
        """
        self.hide_buttons(2)
        ScheduleSubMenu(self.root, self.width, self.height,
                        self.lang.lang, 1, self.list)

    def list_mode_f(self):
        """ Function that allow the launching of the preparation in list - mode
        """
        self.hide_buttons(2)
        ScheduleSubMenu(self.root, self.width, self.height,
                        self.lang.lang, 2, self.list)

    def step_by_step_mode_f(self):
        """ Function that allow the launching of the preparation in a step - by - step mode
        """
        self.hide_buttons(2)
        ScheduleSubMenu(self.root, self.width, self.height,
                        self.lang.lang, 3, self.list)

    def real_time_mode_f(self):
        """ Function that allow the launching of the preparation in real - time mode
        """
        self.hide_buttons(2)
        ScheduleSubMenu(self.root, self.width, self.height,
                        self.lang.lang, 4, self.list)

        # ================== REVIEW
    def view_list_steps_f(self):
        """ Function that allows the user to visualize the number of steps and possibly edit it
        """
        self.hide_buttons(3)
        ScheduleSubMenu(self.root, self.width, self.height,
                        self.lang.lang, 5, self.list)

    def edit_list_recipes_f(self):
        """ Function that allows the user to edit their list of recipes
        """
        self.hide_buttons(3)
        ScheduleSubMenu(self.root, self.width, self.height,
                        self.lang.lang, 6, self.list)

    def edit_list_step_f(self):
        """ Function that allows the user to edit their list of steps
        """
        self.hide_buttons(3)
        ScheduleSubMenu(self.root, self.width, self.height,
                        self.lang.lang, 7, self.list)

    def specification_f(self):
        """ Function that allows the user to specify what tye of kitchen tools they use and whatever else...
                                O P T I O N (when everything is finished)
        """
        self.hide_buttons(3)
        ScheduleSubMenu(self.root, self.width, self.height,
                        self.lang.lang, 8, self.list)

# =================================================== SUB CLASSes of SCHEDULE


class ScheduleSubMenu:
    """ Sub class of schedule that redirect the user to the correct sub - class
    """

    def __init__(self, root, width, height, lang, key, list):
        # Initialization root
        self.root = root
        # Dimension
        self.width, self.height = width, height
        # Definition of the Canvas
        self.can = tk.Canvas(self.root, bg="white",
                             width=self.width, height=self.height*0.8)
        self.can.place(x=0, y=self.height*0.20)
        self.height = self.height*0.8
        # Language
        self.lang = Language(lang)
        # distribution
        self.list = list
        self.list_of_steps = self.steps(self.list)
        #print("Printing line 605:", self.list_of_steps)
        if (key == 1):
            # ================== Launch PART
            ShowListSteps(self.can, self.root, self.width,
                          self.height, self.lang.lang, self.list, self.list_of_steps)
        elif (key == 2):
            ListMode(self.can, self.root, self.width,
                     self.height, self.lang.lang, self.list, self.list_of_steps)
        elif (key == 3):
            StepByStep(self.can, self.root, self.width,
                       self.height, self.lang.lang, self.list, self.list_of_steps)
        elif (key == 4):
            RealTimeMode(self.can, self.root, self.width,
                         self.height, self.lang.lang, self.list, self.list_of_steps)
            # ================== REVIEW PART
        elif (key == 5):
            ViewListSteps(self.can, self.root, self.width,
                          self.height, self.lang.lang, self.list, self.list_of_steps)
        elif (key == 6):
            EditListRecipes(self.can, self.root, self.width,
                            self.height, self.lang.lang, self.list, self.list_of_steps)
        elif (key == 7):
            EditListSteps(self.can, self.root, self.width,
                          self.height, self.lang.lang, self.list, self.list_of_steps)
        elif (key == 8):
            Specification(self.can, self.root, self.width,
                          self.height, self.lang.lang, self.list, self.list_of_steps)
        else:
            # =================== ELSE
            print("FATAL ERROR")

    def steps(self, list_input):
        """ Function that creates steps out of the list of recipes
        """
        list_of_steps = []
        for recipe in list_input:
            name = 'recipes/.recipes/t' + recipe + '.txt'
            file_name = open(name, 'r')
            file_content = file_name.readlines()
            for i in range(int(file_content[0][0]) - 1):
                list_of_steps = self.sort(
                    file_content[i+1], list_of_steps, recipe)

        # inverting the inverted list
        for i in range(len(list_of_steps)//2):
            list_of_steps[i], list_of_steps[len(
                list_of_steps)-1-i] = list_of_steps[len(list_of_steps)-1-i], list_of_steps[i]
        return list_of_steps

    def sort(self, string, list_input, name_file):
        """ Function that put a sting in a sorted list
        """
        # if empty list
        if list_input == []:
            modified_string = string[:5] + ' [' + name_file + '] -' + (
                ((string[5:].replace("\n", "")).replace("Â", "")).replace("Ã©", "é")).replace("Ã¢", "â")
            return [modified_string]
        # variables
        indicator = int(string[0])*10 + int(string[1]) + \
            int(string[3])*0.1 + int(string[4])*0.01
        length = len(list_input)
        # loop to sort
        loop, end_loop = 0, 0
        while end_loop == 0 and (loop < length):
            ind_list = int(list_input[loop][0])*10 + int(list_input[loop][1]) + int(
                list_input[loop][3])*0.1 + int(list_input[loop][4])*0.01
            if indicator >= ind_list:
                modified_string = string[:5] + ' [' + name_file + '] -' + (
                    ((string[5:].replace("\n", "")).replace("Â", "")).replace("Ã©", "é")).replace("Ã¢", "â")
                list_input.insert(loop, modified_string)
                end_loop += 1
            loop += 1
        # return
        return list_input

# ===================================


class ShowListSteps:
    """ Sub class of schedule that display the steps of the list
    """

    def __init__(self, can, root, width, height, lang, list, list_of_steps):
        # Variables
        self.can, self.width, self.height, self.lang = can, width, height, Language(
            lang)
        # Index is of the form index = i[3], with i < [0, +inf[
        self.index = 0
        self.root = root
        self.list = list
        self.list_of_steps = list_of_steps
        self.index = 0
        # Image
        self.three_dots = tk.PhotoImage(file=r"img/three_dots.png")
        # Buttons
        self.back = tk.Button(self.can, image=self.three_dots,
                              background="white", highlightthickness=0, command=self.back_f)

        self.next = tk.Button(self.can, image=self.three_dots,
                              background="white", highlightthickness=0, command=self.next_f)

        self.back_menu = tk.Button(self.can, text=self.lang.back_menu,
                                   background="white", borderwidth=0, highlightthickness=0, command=self.back_menu_f)

        # pack and place
        self.back_menu.pack()

        self.back_menu.place(x=self.width*0.1, y=self.height *
                             0.05, width=100, height=30, anchor="n")

        # Orange RECTANGLES
        # var middle point
        self.middle_w = self.width*0.5
        self.middle_h = self.height*0.5
        # var distance between middle and up/down
        self.step = self.height*0.25
        # var distance between middle and extremities
        self.step_w = self.width*0.35
        self.step_h = self.height*0.1
        # Rectangle
        # up
        self.rect0 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h - self.step - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h - self.step + self.step_h, fill='orange', outline='white')
        # middle
        self.rect1 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h + self.step_h, fill='orange', outline='white')
        # down
        self.rect2 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h + self.step - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h + self.step + self.step_h, fill='orange', outline='white')

        # placing text into rectangels
        if len(self.list_of_steps) >= 1:
            # First
            self.text0 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h - self.step,
                                              text=self.list_of_steps[self.index], width=550, anchor='w')
            if len(self.list_of_steps) >= 2:
                # Second
                self.text1 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h,
                                                  text=self.list_of_steps[self.index+1], width=550, anchor='w')
                if len(self.list_of_steps) >= 3:
                    # Third
                    self.text2 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h + self.step,
                                                      text=self.list_of_steps[self.index+2], width=550, anchor='w')
                    # place button
                    self.next.place(x=self.width*0.75, y=self.height*0.75,
                                    width=95, height=30, anchor="w")
                else:
                    # deleting rectangles and texts that have no use
                    self.can.delete(self.rect2)
            else:
                # deleting rectangles and texts that have no use
                self.can.delete(self.rect1), self.can.delete(self.rect2)
        else:
            # deleting rectangles and texts that have no use
            self.can.delete(self.rect0), self.can.delete(
                self.rect1), self.can.delete(self.rect2)

        # Functions for the buttons
    def back_f(self):
        """Function that allow the user to get back on the list
        """
        # Moving to the previous recipes
        self.index -= 3
        # placing text
        # Rectangles
        self.can.delete(self.rect0), self.can.delete(
            self.rect1), self.can.delete(self.rect2)
        # up
        self.rect0 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h - self.step - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h - self.step + self.step_h, fill='orange', outline='white')
        # middle
        self.rect1 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h + self.step_h, fill='orange', outline='white')
        # down
        self.rect2 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h + self.step - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h + self.step + self.step_h, fill='orange', outline='white')
        # placing text
        # deleting previous steps
        self.can.delete(self.text0), self.can.delete(
            self.text1), self.can.delete(self.text2)
        # creating the previous steps
        self.text0 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h - self.step,
                                          text=self.list_of_steps[self.index], width=550, anchor='w')
        self.text1 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h,
                                          text=self.list_of_steps[self.index+1], width=550, anchor='w')
        self.text2 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h + self.step,
                                          text=self.list_of_steps[self.index+2], width=550, anchor='w')
        # forgetting button
        if self.index == 0:
            self.back.place_forget()
        # placing buttons
        self.next.place(x=self.width*0.75, y=self.height*0.75,
                        width=95, height=30, anchor="w")

    def next_f(self):
        """Function that allow the user to go next on the list
        """
        # place preview
        self.back.place(x=self.width*0.75, y=self.height*0.25,
                        width=95, height=30, anchor="w")
        # erasing text
        self.can.delete(self.text0), self.can.delete(
            self.text1), self.can.delete(self.text2)
        # Moving to the next recipes
        self.index += 3
        # changing text
        if (len(self.list_of_steps) - self.index) >= 1:
            # First
            self.text0 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h - self.step,
                                              text=self.list_of_steps[self.index], width=550, anchor='w')
            if (len(self.list_of_steps) - self.index) >= 2:
                # Second
                self.text1 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h,
                                                  text=self.list_of_steps[self.index+1], width=550, anchor='w')
                if (len(self.list_of_steps) - self.index) >= 3:
                    # Third
                    self.text2 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h + self.step,
                                                      text=self.list_of_steps[self.index+2], width=550, anchor='w')
                else:
                    # deleting rectangles that have no use
                    self.can.delete(self.rect2)
                    # forgetting button
                    self.next.place_forget()
            else:
                # deleting rectangles that have no use
                self.can.delete(self.rect1), self.can.delete(self.rect2)
                # forgetting button
                self.next.place_forget()
        else:
            # deleting rectangles that have no use
            self.can.delete(self.rect0), self.can.delete(
                self.rect1), self.can.delete(self.rect2)
            # forgetting button
            self.next.place_forget()

    def back_menu_f(self):
        """ Function that allow the user to get back to the mainmenu(schedule - launch)
        """
        self.can.destroy()
        Schedule(self.root, self.width, self.height /
                 0.8, self.lang.lang, self.list).launch_f()


# ===================================
class ListMode:
    """ Sub class of schedule that display the list mode
    """

    def __init__(self, can, root, width, height, lang, list, list_of_steps):
        # Variables
        self.can, self.width, self.height, self.lang = can, width, height, Language(
            lang)
        self.root = root
        self.list = list
        self.list_of_steps = list_of_steps
        self.index = -1
        # Image
        self.arrow_u = tk.PhotoImage(file=r"img/arrow_u.png")
        self.arrow_d = tk.PhotoImage(file=r"img/arrow_d.png")

        # Buttons
        self.back = tk.Button(self.can, image=self.arrow_u,
                              background="white", highlightthickness=0, command=self.back_f)

        self.next = tk.Button(self.can, image=self.arrow_d,
                              background="white", highlightthickness=0, command=self.next_f)

        self.back_menu = tk.Button(self.can, text=self.lang.back_menu,
                                   background="white", borderwidth=0, highlightthickness=0, command=self.back_menu_f)

        # pack and place
        self.back_menu.pack()

        self.back_menu.place(x=self.width*0.1, y=self.height *
                             0.05, width=100, height=30, anchor="n")

        # Orange RECTANGLES
        # var middle point
        self.middle_w = self.width*0.5
        self.middle_h = self.height*0.5
        # var distance between middle and up/down
        self.step = self.height*0.25
        # var distance between middle and extremities
        self.step_w = self.width*0.35
        self.step_h = self.height*0.1
        # Rectangle
        # up
        self.rect0 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h - self.step - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h - self.step + self.step_h, fill='#ffcc99', outline='white')
        # middle
        self.rect1 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h + self.step_h, fill='orange', outline='white')
        # down
        self.rect2 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h + self.step - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h + self.step + self.step_h, fill='#ffcc99', outline='white')

        # placing text into rectangels
        if len(self.list_of_steps) >= 1:
            # First
            self.text0 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h - self.step,
                                              text="", width=550, anchor='w')
            if len(self.list_of_steps) >= 2:
                # Second
                self.text1 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h,
                                                  text=self.list_of_steps[self.index+1], width=550, anchor='w')
                if len(self.list_of_steps) >= 3:
                    # Third
                    self.text2 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h + self.step,
                                                      text=self.list_of_steps[self.index+2], width=550, anchor='w')
                    # place button
                    self.next.place(x=self.width*0.875, y=self.height*0.75,
                                    width=90, height=90, anchor="w")
                else:
                    # deleting rectangles and texts that have no use
                    self.can.delete(self.rect2)
            else:
                # deleting rectangles and texts that have no use
                self.can.delete(self.rect1), self.can.delete(self.rect2)
        else:
            # deleting rectangles and texts that have no use
            self.can.delete(self.rect0), self.can.delete(
                self.rect1), self.can.delete(self.rect2)

        # Functions for the buttons
    def back_f(self):
        """Function that allow the user to get back on the list
        """
        # Moving to the previous recipes
        self.index -= 1
        # placing text
        # Rectangles
        self.can.delete(self.rect0), self.can.delete(
            self.rect1), self.can.delete(self.rect2)
        # up
        self.rect0 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h - self.step - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h - self.step + self.step_h, fill='#ffcc99', outline='white')
        # middle
        self.rect1 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h + self.step_h, fill='orange', outline='white')
        # down
        self.rect2 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h + self.step - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h + self.step + self.step_h, fill='#ffcc99', outline='white')
        # placing text
        # deleting previous steps
        self.can.delete(self.text0), self.can.delete(
            self.text1), self.can.delete(self.text2)
        # creating the previous steps
        if (self.index == -1):
            self.text0 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h - self.step,
                                              text="", width=550, anchor='w')
        else:
            self.text0 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h - self.step,
                                              text=self.list_of_steps[self.index], width=550, anchor='w')
        self.text1 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h,
                                          text=self.list_of_steps[self.index+1], width=550, anchor='w')
        self.text2 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h + self.step,
                                          text=self.list_of_steps[self.index+2], width=550, anchor='w')
        # forgetting button
        if self.index == -1:
            self.back.place_forget()
        # placing buttons
        self.next.place(x=self.width*0.875, y=self.height*0.75,
                        width=90, height=90, anchor="w")

    def next_f(self):
        """Function that allow the user to go next on the list
        """
        # place preview
        self.back.place(x=self.width*0.875, y=self.height*0.25,
                        width=90, height=90, anchor="w")
        # erasing text
        self.can.delete(self.text0), self.can.delete(
            self.text1), self.can.delete(self.text2)
        # Moving to the next recipes
        self.index += 1
        # changing text
        if (len(self.list_of_steps) - self.index) >= 1:
            # First
            self.text0 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h - self.step,
                                              text=self.list_of_steps[self.index], width=550, anchor='w')
            if (len(self.list_of_steps) - self.index) >= 2:
                # Second
                self.text1 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h,
                                                  text=self.list_of_steps[self.index+1], width=550, anchor='w')
                if (len(self.list_of_steps) - self.index) >= 3:
                    # Third
                    self.text2 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h + self.step,
                                                      text=self.list_of_steps[self.index+2], width=550, anchor='w')
                else:
                    # deleting rectangles that have no use
                    self.can.delete(self.rect2)
                    # forgetting button
                    self.next.place_forget()
            else:
                # deleting rectangles that have no use
                self.can.delete(self.rect1), self.can.delete(self.rect2)
                # forgetting button
                self.next.place_forget()
        else:
            # deleting rectangles that have no use
            self.can.delete(self.rect0), self.can.delete(
                self.rect1), self.can.delete(self.rect2)
            # forgetting button
            self.next.place_forget()

    def back_menu_f(self):
        """ Function that allow the user to get back to the mainmenu(schedule - launch)
        """
        self.can.destroy()
        Schedule(self.root, self.width, self.height /
                 0.8, self.lang.lang, self.list).launch_f()


# ===================================
class StepByStep:
    def __init__(self, can, root, width, height, lang, list, list_of_steps):
        # Variables
        self.can, self.width, self.height, self.lang = can, width, height, Language(
            lang)
        self.root = root
        self.list = list
        self.list_of_steps = list_of_steps
        self.index = -1
        self.color_set = ['green', '#90ee90', 'orange', '#ffcc99']
        self.marqued_index = -1
        # Buttons
        self.back = tk.Button(self.can, text=self.lang.previous,
                              background="white", highlightthickness=0, command=self.back_f)

        self.done = tk.Button(self.can, text=self.lang.finish,
                              background="white", highlightthickness=0, command=self.done_f)

        self.next = tk.Button(self.can, text=self.lang.next + " "+self.lang.step,
                              background="white", highlightthickness=0, command=self.next_f)

        self.back_menu = tk.Button(self.can, text=self.lang.back_menu,
                                   background="white", borderwidth=0, highlightthickness=0, command=self.back_menu_f)
        # pack and place
        self.back_menu.pack()
        self.back_menu.place(x=self.width*0.1, y=self.height *
                             0.05, width=100, height=30, anchor="n")

        # Orange RECTANGLES
        # var middle point
        self.middle_w = self.width*0.5
        self.middle_h = self.height*0.5
        # var distance between middle and up/down
        self.step = self.height*0.25
        # var distance between middle and extremities
        self.step_w = self.width*0.35
        self.step_h = self.height*0.1
        # Rectangle
        # up
        self.rect0 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h - self.step - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h - self.step + self.step_h, fill='#ffcc99', outline='white')
        # middle
        self.rect1 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h + self.step_h, fill='orange', outline='white')
        # down
        self.rect2 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h + self.step - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h + self.step + self.step_h, fill='#ffcc99', outline='white')

        # placing text into rectangels
        if len(self.list_of_steps) >= 1:
            # First
            self.done.place(x=self.width*0.875, y=self.height*0.5,
                            width=90, height=90, anchor="w")
            self.text0 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h - self.step,
                                              text="", width=550, anchor='w')
            if len(self.list_of_steps) >= 2:
                # Second
                self.text1 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h,
                                                  text=self.list_of_steps[self.index+1], width=550, anchor='w')
                if len(self.list_of_steps) >= 3:
                    # Third
                    self.text2 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h + self.step,
                                                      text=self.list_of_steps[self.index+2], width=550, anchor='w')
                    # place button
                    self.next.place(x=self.width*0.875, y=self.height*0.75,
                                    width=90, height=90, anchor="w")
                else:
                    # deleting rectangles and texts that have no use
                    self.can.delete(self.rect2)
            else:
                # deleting rectangles and texts that have no use
                self.can.delete(self.rect1), self.can.delete(self.rect2)
        else:
            # deleting rectangles and texts that have no use
            self.can.delete(self.rect0), self.can.delete(
                self.rect1), self.can.delete(self.rect2)

        # Functions for the buttons
    def back_f(self):
        """Function that allow the user to get back on the list
        """
        # Moving to the previous recipes
        self.index -= 1
        # placing text
        # Rectangles
        self.can.delete(self.rect0), self.can.delete(
            self.rect1), self.can.delete(self.rect2)
        # up
        self.rect0 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h - self.step - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h - self.step + self.step_h,
                                               fill=self.color_set[self.change_color(self.index)+1], outline='white')
        # middle
        self.rect1 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h + self.step_h,
                                               fill=self.color_set[self.change_color(self.index+1)], outline='white')
        # down
        self.rect2 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h + self.step - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h + self.step + self.step_h,
                                               fill=self.color_set[self.change_color(self.index+2)+1], outline='white')
        # placing text
        # deleting previous steps
        self.can.delete(self.text0), self.can.delete(
            self.text1), self.can.delete(self.text2)
        # creating the previous steps
        if (self.index == -1):
            self.text0 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h - self.step,
                                              text="", width=550, anchor='w')
            self.can.delete(self.rect0)
        else:
            self.text0 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h - self.step,
                                              text=self.list_of_steps[self.index], width=550, anchor='w')
        self.text1 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h,
                                          text=self.list_of_steps[self.index+1], width=550, anchor='w')
        self.text2 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h + self.step,
                                          text=self.list_of_steps[self.index+2], width=550, anchor='w')
        # forgetting button
        if self.index == -1:
            self.back.place_forget()
        # print(self.index, self.marqued_index-1)
        if self.index == self.marqued_index:
            self.done.place(x=self.width*0.875, y=self.height*0.5,
                            width=90, height=90, anchor="w")
        else:
            self.done.place_forget()
        # placing buttons
        self.next.place(x=self.width*0.875, y=self.height*0.75,
                        width=90, height=90, anchor="w")

    def next_f(self):
        """Function that allow the user to go next on the list
        """
        # place preview
        if self.index+1 == self.marqued_index-1:
            self.done.place(x=self.width*0.875, y=self.height*0.5,
                            width=90, height=90, anchor="w")
        else:
            self.done.place_forget()
        self.back.place(x=self.width*0.875, y=self.height*0.25,
                        width=90, height=90, anchor="w")
        # erasing text and rectangles
        self.can.delete(self.text0), self.can.delete(
            self.text1), self.can.delete(self.text2)
        self.can.delete(self.rect0), self.can.delete(
            self.rect1), self.can.delete(self.rect2)
        # Moving to the next recipes
        self.index += 1
        # changing text
        if (len(self.list_of_steps) - self.index) >= 1:
            # First
            self.rect0 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h - self.step - self.step_h,
                                                   self.middle_w + self.step_w, self.middle_h - self.step + self.step_h,
                                                   fill=self.color_set[self.change_color(self.index)+1], outline='white')
            self.text0 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h - self.step,
                                              text=self.list_of_steps[self.index], width=550, anchor='w')
            if (len(self.list_of_steps) - self.index) >= 2:
                # Second
                self.rect1 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h - self.step_h,
                                                       self.middle_w + self.step_w, self.middle_h + self.step_h,
                                                       fill=self.color_set[self.change_color(self.index+1)], outline='white')
                self.text1 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h,
                                                  text=self.list_of_steps[self.index+1], width=550, anchor='w')
                if (len(self.list_of_steps) - self.index) >= 3:
                    # Third
                    # down
                    self.rect2 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h + self.step - self.step_h,
                                                           self.middle_w + self.step_w, self.middle_h + self.step + self.step_h,
                                                           fill=self.color_set[self.change_color(self.index+2)+1], outline='white')
                    self.text2 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h + self.step,
                                                      text=self.list_of_steps[self.index+2], width=550, anchor='w')
                else:
                    # deleting rectangles that have no use
                    self.can.delete(self.rect2)
                    # forgetting button
                    self.next.place_forget()
            else:
                # deleting rectangles that have no use
                self.can.delete(self.rect1), self.can.delete(self.rect2)
                # forgetting button
                self.next.place_forget()
        else:
            # deleting rectangles that have no use
            self.can.delete(self.rect0), self.can.delete(
                self.rect1), self.can.delete(self.rect2)
            # forgetting button
            self.next.place_forget()

    def done_f(self):
        """ Function that chnage the previous rectangle in green
        """
        # Marquing the done index
        self.marqued_index = self.index+1
        if self.index+1 >= len(self.list_of_steps)-1:
            self.done.place_forget()
            return
        # changing the previous rectangle
        self.can.delete(self.rect0)
        self.rect0 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h - self.step - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h - self.step + self.step_h,
                                               fill="light green", outline='white')
        self.next_f()

    def change_color(self, index):
        """ Function that changes the color in function of the index
        """
        # test
        if index <= self.marqued_index:
            return 0
        else:
            return 2

    def back_menu_f(self):
        """ Function that allow the user to get back to the mainmenu(schedule - launch)
        """
        self.can.destroy()
        Schedule(self.root, self.width, self.height /
                 0.8, self.lang.lang, self.list).launch_f()


# ===================================
class RealTimeMode:
    """ Class that will allow the user to prepare their meal in real time with the application telling them what to do when and how
    [Maybe most important work to do]

    _idea_ (to continue time without enter a infinit loop):
    while (...):
        wait (1 (second))
        if (no _new_ action)
            t++ (time continue)
        else:
            execute new action (like skip step, done step or previous or even exit)
    """

    def __init__(self, can, root, width, height, lang, list, list_of_steps):
        # Variables
        self.can, self.width, self.height, self.lang = can, width, height, Language(
            lang)
        self.root = root
        self.list = list
        self.list_of_steps = list_of_steps
        # Initializing time
        # self.time
        # Buttons
        self.back_menu = tk.Button(self.can, text=self.lang.back_menu,
                                   background="white", borderwidth=0, highlightthickness=0, command=self.back_menu_f)
        # Images
        self.clock = tk.PhotoImage(file=r"img/clock.png")
        self.clock_placed = self.can.create_image(
            self.width*0.85, self.height*0.2, image=self.clock)
        self.clock_center = (self.width*0.85, self.height*0.2)

        # Pack and place
        self.back_menu.pack()

        self.back_menu.place(x=self.width*0.1, y=self.height *
                             0.05, width=100, height=30, anchor="n")

    # Functions

    def needles_placing(self, hours, minutes, seconds):
        """ Function that places the needles on the clock
        """
        # Angles definition

        # theta0  hours * (360/12)
        # theta1  minutes * (360/60)
        # theta2  seconds * (360/60)

    def back_menu_f(self):
        """ Function that allow the user to get back to the mainmenu(schedule - launch)
        """
        self.can.destroy()
        Schedule(self.root, self.width, self.height /
                 0.8, self.lang.lang, self.list).launch_f()

# ===================================


class ViewListSteps:
    """ Class that allow the user to view the list of steps, in which they cannot edit the list (but can access the page that can)
    """

    def __init__(self, can, root, width, height, lang, list, list_of_steps):
        # Variables
        self.can, self.width, self.height, self.lang = can, width, height, Language(
            lang)
        self.root = root
        self.list = list
        self.list_of_steps = list_of_steps
        self.index = 0
        # Image
        self.arrow_u = tk.PhotoImage(file=r"img/arrow_u.png")
        self.arrow_d = tk.PhotoImage(file=r"img/arrow_d.png")

        # Buttons
        self.back = tk.Button(self.can, image=self.arrow_u,
                              background="white", highlightthickness=0, command=self.back_f)

        self.next = tk.Button(self.can, image=self.arrow_d,
                              background="white", highlightthickness=0, command=self.next_f)

        self.back_menu = tk.Button(self.can, text=self.lang.back_menu,
                                   background="white", borderwidth=0, highlightthickness=0, command=self.back_menu_f)

        # pack and place
        self.back_menu.pack()

        self.back_menu.place(x=self.width*0.1, y=self.height *
                             0.05, width=100, height=30, anchor="n")

        # Orange RECTANGLES
        # var middle point
        self.middle_w = self.width*0.5
        self.middle_h = self.height*0.5
        # var distance between middle and up/down
        self.step = self.height*0.25
        # var distance between middle and extremities
        self.step_w = self.width*0.35
        self.step_h = self.height*0.1
        # Rectangle
        # up
        self.rect0 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h - self.step - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h - self.step + self.step_h, fill='orange', outline='white')
        # middle
        self.rect1 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h + self.step_h, fill='orange', outline='white')
        # down
        self.rect2 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h + self.step - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h + self.step + self.step_h, fill='orange', outline='white')

        # placing text into rectangels
        if len(self.list_of_steps) >= 1:
            # First
            self.text0 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h - self.step,
                                              text=self.list_of_steps[self.index], width=550, anchor='w')
            if len(self.list_of_steps) >= 2:
                # Second
                self.text1 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h,
                                                  text=self.list_of_steps[self.index+1], width=550, anchor='w')
                if len(self.list_of_steps) >= 3:
                    # Third
                    self.text2 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h + self.step,
                                                      text=self.list_of_steps[self.index+2], width=550, anchor='w')
                    # place button
                    self.next.place(x=self.width*0.875, y=self.height*0.75,
                                    width=90, height=90, anchor="w")
                else:
                    # deleting rectangles and texts that have no use
                    self.can.delete(self.rect2)
            else:
                # deleting rectangles and texts that have no use
                self.can.delete(self.rect1), self.can.delete(self.rect2)
        else:
            # deleting rectangles and texts that have no use
            self.can.delete(self.rect0), self.can.delete(
                self.rect1), self.can.delete(self.rect2)

        # Functions for the buttons
    def back_f(self):
        """Function that allow the user to get back on the list
        """
        # Moving to the previous recipes
        self.index -= 3
        # placing text
        # Rectangles
        self.can.delete(self.rect0), self.can.delete(
            self.rect1), self.can.delete(self.rect2)
        # up
        self.rect0 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h - self.step - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h - self.step + self.step_h, fill='orange', outline='white')
        # middle
        self.rect1 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h + self.step_h, fill='orange', outline='white')
        # down
        self.rect2 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h + self.step - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h + self.step + self.step_h, fill='orange', outline='white')
        # placing text
        # deleting previous steps
        self.can.delete(self.text0), self.can.delete(
            self.text1), self.can.delete(self.text2)
        # creating the previous steps
        self.text0 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h - self.step,
                                          text=self.list_of_steps[self.index], width=550, anchor='w')
        self.text1 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h,
                                          text=self.list_of_steps[self.index+1], width=550, anchor='w')
        self.text2 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h + self.step,
                                          text=self.list_of_steps[self.index+2], width=550, anchor='w')
        # forgetting button
        if self.index == 0:
            self.back.place_forget()
        # placing buttons
        self.next.place(x=self.width*0.875, y=self.height*0.75,
                        width=90, height=90, anchor="w")

    def next_f(self):
        """Function that allow the user to go next on the list
        """
        # place preview
        self.back.place(x=self.width*0.875, y=self.height*0.25,
                        width=90, height=90, anchor="w")
        # erasing text
        self.can.delete(self.text0), self.can.delete(
            self.text1), self.can.delete(self.text2)
        # Moving to the next recipes
        self.index += 3
        # changing text
        if (len(self.list_of_steps) - self.index) >= 1:
            # First
            self.text0 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h - self.step,
                                              text=self.list_of_steps[self.index], width=550, anchor='w')
            if (len(self.list_of_steps) - self.index) >= 2:
                # Second
                self.text1 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h,
                                                  text=self.list_of_steps[self.index+1], width=550, anchor='w')
                if (len(self.list_of_steps) - self.index) >= 3:
                    # Third
                    self.text2 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h + self.step,
                                                      text=self.list_of_steps[self.index+2], width=550, anchor='w')
                else:
                    # deleting rectangles that have no use
                    self.can.delete(self.rect2)
                    # forgetting button
                    self.next.place_forget()
            else:
                # deleting rectangles that have no use
                self.can.delete(self.rect1), self.can.delete(self.rect2)
                # forgetting button
                self.next.place_forget()
        else:
            # deleting rectangles that have no use
            self.can.delete(self.rect0), self.can.delete(
                self.rect1), self.can.delete(self.rect2)
            # forgetting button
            self.next.place_forget()

    def back_menu_f(self):
        """ Function that allow the user to get back to the mainmenu(schedule - launch)
        """
        self.can.destroy()
        Schedule(self.root, self.width, self.height /
                 0.8, self.lang.lang, self.list).review_f()

# ===================================


class EditListRecipes:
    """ Class that will allow the user to edit their list of steps (not advised but still)
    """

    def __init__(self, can, root, width, height, lang, list, list_of_steps):
        # Variables
        self.can, self.width, self.height, self.lang = can, width, height, Language(
            lang)
        self.root = root
        self.list = list
        self.index = 0
        # img
        self.bin = tk.PhotoImage(file=r"img/Bin.png").subsample(10, 10)
        # Buttons
        self.back_menu = tk.Button(self.can, text=self.lang.back_menu,
                                   background="white", borderwidth=0, highlightthickness=0, command=self.back_menu_f)
        self.next_step = tk.Button(self.can, text=self.lang.next,
                                   background="white", borderwidth=0, highlightthickness=0, command=self.next_step_f)

        self.previous_step = tk.Button(self.can, text=self.lang.back,
                                       background="white", borderwidth=0, highlightthickness=0, command=self.previous_step_f)
        # delete buttons
        self.delete0 = tk.Button(self.can, image=self.bin,
                                 background="white", borderwidth=0, highlightthickness=0, command=self.delete_recipe0)
        self.delete1 = tk.Button(self.can, image=self.bin,
                                 background="white", borderwidth=0, highlightthickness=0, command=self.delete_recipe1)
        self.delete2 = tk.Button(self.can, image=self.bin,
                                 background="white", borderwidth=0, highlightthickness=0, command=self.delete_recipe2)

        # TEMP RECTANGLE
        # var middle point
        self.middle_w = self.width*0.5
        self.middle_h = self.height*0.5
        # var distance between middle and up/down
        self.step = self.height*0.25
        # var distance between middle and extremities
        self.step_w = self.width*0.35
        self.step_h = self.height*0.1
        # Rectangle
        # up
        self.rect0 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h - self.step - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h - self.step + self.step_h, fill='orange', outline='white')
        # middle
        self.rect1 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h + self.step_h, fill='orange', outline='white')
        # down
        self.rect2 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h + self.step - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h + self.step + self.step_h, fill='orange', outline='white')
        # text
        if len(self.list) >= 1:
            # First
            self.text0 = self.can.create_text(self.middle_w, self.middle_h - self.step,
                                              text=self.list[self.index], width=550, anchor='w')
            self.delete0.place(x=self.width*0.75, y=self.height*0.25,
                               width=50, height=50, anchor="w")
            if len(self.list) >= 2:
                # Second
                self.text1 = self.can.create_text(self.middle_w, self.middle_h,
                                                  text=self.list[self.index+1], width=550, anchor='w')
                self.delete1.place(x=self.width*0.75, y=self.height*0.5,
                                   width=50, height=50, anchor="w")
                if len(self.list) >= 3:
                    # Third
                    self.text2 = self.can.create_text(self.middle_w, self.middle_h + self.step,
                                                      text=self.list[self.index+2], width=550, anchor='w')
                    self.delete2.place(x=self.width*0.75, y=self.height*0.75,
                                       width=50, height=50, anchor="w")
                    # place button
                    self.next_step.place(x=self.width*0.75, y=self.height*0.25,
                                         width=100, height=30, anchor="n")
                else:
                    # deleting rectangles and texts that have no use
                    self.can.delete(self.rect2)
            else:
                # deleting rectangles and texts that have no use
                self.can.delete(self.rect1), self.can.delete(self.rect2)
        else:
            # deleting rectangles and texts that have no use
            self.can.delete(self.rect0), self.can.delete(
                self.rect1), self.can.delete(self.rect2)
        # Pack and place
        self.back_menu.place(x=self.width*0.1, y=self.height *
                             0.05, width=100, height=30, anchor="n")

    # Functions

    def next_step_f(self):
        """ Function that will display the next step (the actual -> previous ; next -> actual)
        """
        # erasing text
        if (len(self.list) == 0):
            return self.back_menu_f()
        elif self.index >= 3:
            # place preview
            self.previous_step.place(x=self.width*0.75, y=self.height*0.75,
                                     width=100, height=30, anchor="n")
        # Moving to the next recipes
        self.index += 3
        # changing text
        if (len(self.list) - self.index) >= 1:
            # First
            self.can.delete(self.text0)
            self.text0 = self.can.create_text(self.middle_w, self.middle_h - self.step,
                                              text=self.list[self.index], width=550, anchor='w')
            if (len(self.list) - self.index) >= 2:
                # Second
                self.can.delete(self.text1)
                self.text1 = self.can.create_text(self.middle_w, self.middle_h,
                                                  text=self.list[self.index+1], width=550, anchor='w')
                if (len(self.list) - self.index) >= 3:
                    # Third
                    self.can.delete(self.text2)
                    self.text2 = self.can.create_text(self.middle_w, self.middle_h + self.step,
                                                      text=self.list[self.index+2], width=550, anchor='w')
                    self.next_step.place(x=self.width*0.75, y=self.height*0.25,
                                         width=100, height=30, anchor="n")
                else:
                    # deleting rectangles that have no use
                    self.can.delete(self.rect2)
                    # forgetting button
                    self.next_step.place_forget()
                    self.delete2.place_forget()
            else:
                # deleting rectangles that have no use
                self.can.delete(self.rect1), self.can.delete(self.rect2)
                self.delete1.place_forget(), self.delete2.place_forget()
                # forgetting button
                self.next_step.place_forget()
        else:
            # deleting rectangles that have no use
            self.can.delete(self.rect0), self.can.delete(
                self.rect1), self.can.delete(self.rect2)
            self.delete0.place_forget(), self.delete1.place_forget(), self.delete2.place_forget()
            # forgetting button
            self.next_step.place_forget()

    def previous_step_f(self):
        """ Function that will display the next step (previous -> actual ; actual -> next)
        """
        # Moving to the previous recipes
        self.index -= 3
        # placing text
        # Rectangles
        # up
        self.rect0 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h - self.step - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h - self.step + self.step_h, fill='orange', outline='white')
        # middle
        self.rect1 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h + self.step_h, fill='orange', outline='white')
        # down
        self.rect2 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h + self.step - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h + self.step + self.step_h, fill='orange', outline='white')
        # placing text
        # deleting previous steps
        self.can.delete(self.text0), self.can.delete(
            self.text1), self.can.delete(self.text2)
        # creating the previous steps
        self.text0 = self.can.create_text(self.middle_w, self.middle_h - self.step,
                                          text=self.list[self.index], width=550, anchor='w')
        self.text1 = self.can.create_text(self.middle_w, self.middle_h,
                                          text=self.list[self.index+1], width=550, anchor='w')
        self.text2 = self.can.create_text(self.middle_w, self.middle_h + self.step,
                                          text=self.list[self.index+2], width=550, anchor='w')
        # forgetting button
        if self.index == 0:
            self.previous_step.place_forget()
        # placing buttons
        self.next_step.place(x=self.width*0.75, y=self.height*0.25,
                             width=100, height=30, anchor="n")
        # placing buttons
        self.next_step.place(x=self.width*0.91, y=self.height*0.75,
                             width=100, height=30, anchor="n")
        self.delete0.place(x=self.width*0.75, y=self.height*0.25,
                           width=50, height=50, anchor="w")
        self.delete1.place(x=self.width*0.75, y=self.height*0.5,
                           width=50, height=50, anchor="w")
        self.delete2.place(x=self.width*0.75, y=self.height*0.75,
                           width=50, height=50, anchor="w")

    def delete_recipe0(self):
        """ Deleting the recipe at placement 0
        """
        del self.list[self.index]
        self.index -= 3
        self.can.delete(self.text0)
        self.next_step_f()

    def delete_recipe1(self):
        """ Deleting the recipe at placement 1
        """
        del self.list[self.index+1]
        self.index -= 3
        self.can.delete(self.text1)
        self.next_step_f()

    def delete_recipe2(self):
        """ Deleting the recipe at placement 2
        """
        del self.list[self.index+2]
        self.index -= 3
        self.can.delete(self.text2)
        self.next_step_f()

    def back_menu_f(self):
        """ Function that allow the user to get back to the mainmenu(schedule - review)
        """
        self.can.destroy()
        Schedule(self.root, self.width, self.height /
                 0.8, self.lang.lang, self.list).review_f()

# ===================================


class EditListSteps:
    """ Class (option) that will allow the user to specify what is their kitchen, with what specification (microwave - 750W for instance; ...)
    """

    def __init__(self, can, root, width, height, lang, list, list_of_steps):
        # Variables
        self.can, self.width, self.height, self.lang = can, width, height, Language(
            lang)
        self.root = root
        self.list = list
        self.list_of_steps = list_of_steps
        self.index = 0
        # img
        self.bin = tk.PhotoImage(file=r"img/Bin.png").subsample(10, 10)
        # Buttons
        self.back_menu = tk.Button(self.can, text=self.lang.back_menu,
                                   background="white", borderwidth=0, highlightthickness=0, command=self.back_menu_f)
        self.next_step = tk.Button(self.can, text=self.lang.next,
                                   background="white", borderwidth=1, highlightthickness=0, command=self.next_step_f)

        self.previous_step = tk.Button(self.can, text=self.lang.back,
                                       background="white", borderwidth=1, highlightthickness=0, command=self.previous_step_f)
        # delete buttons
        self.delete0 = tk.Button(self.can, image=self.bin,
                                 background="white", borderwidth=0, highlightthickness=0, command=self.delete_recipe0)
        self.delete1 = tk.Button(self.can, image=self.bin,
                                 background="white", borderwidth=0, highlightthickness=0, command=self.delete_recipe1)
        self.delete2 = tk.Button(self.can, image=self.bin,
                                 background="white", borderwidth=0, highlightthickness=0, command=self.delete_recipe2)

        # TEMP RECTANGLE
        # var middle point
        self.middle_w = self.width*0.5
        self.middle_h = self.height*0.5
        # var distance between middle and up/down
        self.step = self.height*0.25
        # var distance between middle and extremities
        self.step_w = self.width*0.35
        self.step_h = self.height*0.1
        # Rectangle
        # up
        self.rect0 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h - self.step - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h - self.step + self.step_h, fill='orange', outline='white')
        # middle
        self.rect1 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h + self.step_h, fill='orange', outline='white')
        # down
        self.rect2 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h + self.step - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h + self.step + self.step_h, fill='orange', outline='white')
        # text
        if len(self.list_of_steps) >= 1:
            # First
            self.text0 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h - self.step,
                                              text=self.list_of_steps[self.index], width=550, anchor='w')
            self.delete0.place(x=self.width*0.75, y=self.height*0.25,
                               width=50, height=50, anchor="w")
            if len(self.list_of_steps) >= 2:
                # Second
                self.text1 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h,
                                                  text=self.list_of_steps[self.index+1], width=550, anchor='w')
                self.delete1.place(x=self.width*0.75, y=self.height*0.5,
                                   width=50, height=50, anchor="w")
                if len(self.list_of_steps) >= 3:
                    # Third
                    self.text2 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h + self.step,
                                                      text=self.list_of_steps[self.index+2], width=550, anchor='w')
                    self.delete2.place(x=self.width*0.75, y=self.height*0.75,
                                       width=50, height=50, anchor="w")
                    # place button
                    self.next_step.place(x=self.width*0.91, y=self.height*0.75,
                                         width=100, height=30, anchor="n")
                else:
                    # deleting rectangles and texts that have no use
                    self.can.delete(self.rect2)
            else:
                # deleting rectangles and texts that have no use
                self.can.delete(self.rect1), self.can.delete(self.rect2)
        else:
            # deleting rectangles and texts that have no use
            self.can.delete(self.rect0), self.can.delete(
                self.rect1), self.can.delete(self.rect2)

        # Pack and place
        self.back_menu.place(x=self.width*0.1, y=self.height *
                             0.05, width=100, height=30, anchor="n")

    # Functions

    def next_step_f(self):
        """ Function that will display the next step (the actual -> previous ; next -> actual)
        """
        # Moving to the next recipes
        self.index += 3
        # erasing text
        if (len(self.list_of_steps) == 0):
            return self.back_menu_f()
        elif self.index >= 3:
            # place preview
            self.previous_step.place(x=self.width*0.91, y=self.height*0.25,
                                     width=100, height=30, anchor="n")
        # Moving to the next recipes
        self.can.delete(self.text0), self.can.delete(
            self.text1), self.can.delete(self.text2)
        # changing text
        if (len(self.list_of_steps) - self.index) >= 1:
            # First
            self.text0 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h - self.step,
                                              text=self.list_of_steps[self.index], width=550, anchor='w')
            if (len(self.list_of_steps) - self.index) >= 2:
                # Second
                self.text1 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h,
                                                  text=self.list_of_steps[self.index+1], width=550, anchor='w')
                if (len(self.list_of_steps) - self.index) >= 3:
                    # Third
                    self.text2 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h + self.step,
                                                      text=self.list_of_steps[self.index+2], width=550, anchor='w')
                    self.next_step.place(x=self.width*0.91, y=self.height*0.75,
                                         width=100, height=30, anchor="n")
                else:
                    # deleting rectangles that have no use
                    self.can.delete(self.rect2)
                    # forgetting button
                    self.next_step.place_forget()
                    self.delete2.place_forget()
            else:
                # deleting rectangles that have no use
                self.can.delete(self.rect1), self.can.delete(self.rect2)
                # forgetting button
                self.next_step.place_forget()
                self.delete1.place_forget(), self.delete2.place_forget()
        else:
            # deleting rectangles that have no use
            self.can.delete(self.rect0), self.can.delete(
                self.rect1), self.can.delete(self.rect2)
            # forgetting button
            self.next_step.place_forget()
            self.delete0.place_forget(), self.delete1.place_forget(), self.delete2.place_forget()

    def previous_step_f(self):
        """ Function that will display the next step (previous -> actual ; actual -> next)
        """
        # Moving to the previous recipes
        self.index -= 3
        # placing text
        # Rectangles
        # up
        self.rect0 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h - self.step - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h - self.step + self.step_h, fill='orange', outline='white')
        # middle
        self.rect1 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h + self.step_h, fill='orange', outline='white')
        # down
        self.rect2 = self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h + self.step - self.step_h,
                                               self.middle_w + self.step_w, self.middle_h + self.step + self.step_h, fill='orange', outline='white')
        # placing text
        # deleting previous steps
        self.can.delete(self.text0), self.can.delete(
            self.text1), self.can.delete(self.text2)
        # creating the previous steps
        self.text0 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h - self.step,
                                          text=self.list_of_steps[self.index], width=550, anchor='w')
        self.text1 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h,
                                          text=self.list_of_steps[self.index+1], width=550, anchor='w')
        self.text2 = self.can.create_text(self.middle_w - self.width*0.3, self.middle_h + self.step,
                                          text=self.list_of_steps[self.index+2], width=550, anchor='w')
        # forgetting button
        if self.index == 0:
            self.previous_step.place_forget()
        # placing buttons
        self.next_step.place(x=self.width*0.91, y=self.height*0.75,
                             width=100, height=30, anchor="n")
        self.delete0.place(x=self.width*0.75, y=self.height*0.25,
                           width=50, height=50, anchor="w")
        self.delete1.place(x=self.width*0.75, y=self.height*0.5,
                           width=50, height=50, anchor="w")
        self.delete2.place(x=self.width*0.75, y=self.height*0.75,
                           width=50, height=50, anchor="w")

    def delete_recipe0(self):
        """ Deleting the recipe at placement 0
        """
        del self.list_of_steps[self.index]
        self.index -= 3
        self.can.delete(self.text0)
        self.next_step_f()

    def delete_recipe1(self):
        """ Deleting the recipe at placement 1
        """
        del self.list_of_steps[self.index+1]
        self.index -= 3
        self.can.delete(self.text1)
        self.next_step_f()

    def delete_recipe2(self):
        """ Deleting the recipe at placement 2
        """
        del self.list_of_steps[self.index+2]
        self.index -= 3
        self.can.delete(self.text2)
        self.next_step_f()

    def back_menu_f(self):
        """ Function that allow the user to get back to the mainmenu(schedule - review)
        """
        self.can.destroy()
        Schedule(self.root, self.width, self.height /
                 0.8, self.lang.lang, self.list).review_f()

# ===================================


class Specification:
    def __init__(self, can, root, width, height, lang, list, list_of_steps):
        # Variables
        self.can, self.width, self.height, self.lang = can, width, height, Language(
            lang)
        self.root = root
        self.list = list
        # Buttons
        self.back_menu = tk.Button(self.can, text=self.lang.back_menu,
                                   background="white", borderwidth=0, highlightthickness=0, command=self.back_menu_f)

        # Pack and place
        self.back_menu.pack()

        self.back_menu.place(x=self.width*0.1, y=self.height *
                             0.05, width=100, height=30, anchor="n")

    # Functions
    def back_menu_f(self):
        """ Function that allow the user to get back to the mainmenu(schedule - review)
        """
        self.can.destroy()
        Schedule(self.root, self.width, self.height /
                 0.8, self.lang.lang, self.list).review_f()


# ================================================================================================================================================
# ============================================================= MAIN FRAME =======================================================================
# ================================================================================================================================================
class MainFrame:
    def __init__(self, root, width, height, lang):
        self.root = root
        self.width, self.height = width, height
        self.root.geometry(str(width) + "x" + str(height))
        self.lang = Language(lang)
        self.root.title(self.lang.title)
        self.root.configure(bg='white')
        self.list = []
        # ====== Resize
        #self.root.minsize(self.width, self.height)
        #self.root.maxsize(self.width +100, self.height +70)
        self.root.resizable(width=False, height=False)
        # { when we will want to be able to resize the window: how to know the size choosen :::}
        # actualwidth = self.root.winfo_screenwidth()
        # actualheight = self.root.winfo_screenheight()
        # ================= Launching Main
        MainMenu(self.root, self.width, self.height, self.lang.lang, self.list)
        # ================= Main Loop =================
        self.root.mainloop()
