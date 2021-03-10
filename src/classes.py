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
            file=r"img/schedule.png").subsample(20, 20)
        # ================= Menu design =================
        # ========== Up border ==========

        self.can.create_rectangle(
            0, 0, self.width, self.height*0.20, fill='orange', outline='white')

        # ===== Title =====
        self.can.create_text(self.width*0.5, self.height*0.05, text=self.lang.title, fill="black", font=(calibri, 30))

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
        self.button_schedule = tk.Button(self.root ,image = self.schedule_icon, background="orange",
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
    
    # ====== Funcion Schedule
    def schedule(self):
        """Function that lanches the schedule-page // detroy main menu
        """
        self.can.destroy()
        Schedule(self.root, self.width, self.height, self.lang.lang)

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
            #Mainmenu
            self.searchbartxt = "Taper votre recherche ici..."
            self.profile = "Mon profil"
            self.title = "The Kitchen Project"
            self.fav = "Favoris"
            self.back = "Retour"
            self.schedule = "Planning"
            #Schedule
            self.launch = "Lancer la prépartion"
            self.review = "Revoir la prépartion"
                #launch
            self.launch_mode = "Modes de lancement :"
            self.display_mode = "Affichage :"
            self.show_list_of_steps = "Afficher les étapes de préparation"
            self.list_mode = "En liste"
            self.step_by_step = "En étape-par-étape"
            self.real_time_mode = "En temps réél"
                #review
            self.review_mode_1 = "Afficher avant préparation"
            self.review_mode_2 = "Modifier avant préparation"
            self.review_mode_3 = "Spécifier ma cuisine avant de commencer"
            self.view_list_steps = "Afficher les étapes"
            self.edit_list_recipes = "Modifier la liste des recettes"
            self.edit_list_steps = "Modifier les étapes"
            self.specification = "Personnaliser ma cuisine"
        # ==================== English (by default)
        elif self.lang == "EN":
            #Mainmenu
            self.searchbartxt = "Type something here..."
            self.profile = "My profile"
            self.title = "The Kitchen Project"
            self.fav = "Favorites"
            self.back = "Back"
            self.schedule = "Schedule"
            #Schedule
            self.launch = "Launch the preparation"
            self.review = "Review the preparation"
                #launch
            self.launch_mode = "Launch modes :"
            self.display_mode = "Displaying :"
            self.show_list_of_steps = "Show the list of steps"
            self.list_mode = "List format"
            self.step_by_step = "Step-by-step"
            self.real_time_mode = "In real time"
                #review
            self.review_mode_1 = "View before preparation"
            self.review_mode_2 = "Edit before preparation"
            self.review_mode_3 = "Specify your kitchen befor preparation"
            self.view_list_steps = "View list of steps"
            self.edit_list_recipes = "Edit list of recipes"
            self.edit_list_steps = "Edit list of steps"
            self.specification = "Specify my kitchen"
        else:
            # Fatal error
            print("E  R  R  O  R      L A N G")


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
        MainMenu(self.root, 1000, 700, self.lang.lang)

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
        self.can.create_rectangle(0, 0, self.width, self.height*0.20, fill='orange', outline='white')
        self.can.create_text(self.width*0.5, self.height*0.05, text=self.lang.title, fill="black", font=("Calibri Light", 30))
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
            background="white", highlightthickness=0, command=self.launch)

        self.review= tk.Button(self.root, font=("Calibri", 10), text=self.lang.review, 
            background="white", highlightthickness=0, command=self.review)
            
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
            #home
        self.return_home.pack()
        self.return_home.place(x= self.width*0.05, y= height*0.13)
            #menu
        self.launch.pack()
        self.launch.place(x= self.width*0.5, y= self.height*0.35, width = 200, height = 50, anchor ="n")
        self.review.pack()
        self.review.place(x= self.width*0.5, y= self.height*0.65, width = 200, height = 50, anchor ="n")
        # === Data base analysis

    # ========================================================================== Functions
    def return_home_f (self):
        """Function that allows the user to go on the main page
        """
        self.can.destroy()
        MainMenu(self.root, 1000, 700, self.lang.lang)
    
    def back_l_f (self):
        """ Function that allows the user to go back on the main menu schedule
        """
        #Deleting all buttons
        self.hide_buttons(2)
        #Placing the buttons
        self.place_all_buttons(3)

    def back_r_f (self):
        """ Function that allows the user to go back on the main menu schedule
        """
        #Deleting all buttons
        self.hide_buttons(3)
        #Placing the buttons
        self.place_all_buttons(3)
    
    # === sub - menu
    def launch(self):
        """Function that launches the sub - menu: Launch
        """
        #Deleting all buttons
        self.hide_buttons(1)
        self.place_all_buttons(1)
        #Text
        self.text_temp = (self.can.create_text(self.width*0.5, self.height*0.475,font=("Calibri", 15), text =self.lang.launch_mode),
        self.can.create_text(self.width*0.5, self.height*0.275,font=("Calibri", 15), text =self.lang.display_mode))

    
    def review(self):
        """Function that launches the sub - menu: Review
        """
        #Deleting allbuttons
        self.hide_buttons(1)
        self.place_all_buttons(2)
        # Text
        self.text_temp = (self.can.create_text(self.width*0.5, self.height*0.25,font=("Calibri", 15), text =self.lang.review_mode_1),
        self.can.create_text(self.width*0.5, self.height*0.46,font=("Calibri", 15), text =self.lang.review_mode_2),
        self.can.create_text(self.width*0.5, self.height*0.80,font=("Calibri", 15), text =self.lang.review_mode_3))

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
            self.can.delete(self.text_temp[0],self.text_temp[1])
        elif (key == 3):
            # sub menu "review"
            self.view_list_steps.place_forget()
            self.edit_list_recipes.place_forget()
            self.edit_list_steps.place_forget()
            self.specification.place_forget()
            self.back_r.place_forget()
            self.can.delete(self.text_temp[0],self.text_temp[1], self.text_temp[2])

    def place_all_buttons(self, key):
        """Function that places the buttons in function of the key
        """
        if (key==1): #Launch
            #Packing
            self.show_list_of_steps.pack()
            self.list_mode.pack()
            self.step_by_step_mode.pack()
            self.real_time_mode.pack()
            self.back_l.pack()
            #Placing buttons
            self.show_list_of_steps.place(x= self.width*0.5, y= self.height*0.35, width = 250, height = 50, anchor ="n")
            self.list_mode.place(x= self.width*0.5, y= self.height*0.55, width = 250, height = 50, anchor ="n")
            self.step_by_step_mode.place(x= self.width*0.5, y= self.height*0.65, width = 250, height = 50, anchor ="n")
            self.real_time_mode.place(x= self.width*0.5, y= self.height*0.75, width = 250, height = 50, anchor ="n")
            self.back_l.place(x= self.width*0.75, y= self.height*0.90, width = 70, height = 50, anchor ="n")
        elif (key ==2): # Review
            #Packing
            self.view_list_steps.pack()
            self.edit_list_recipes.pack()
            self.edit_list_steps.pack()
            self.specification.pack()
            self.back_r.pack()
            #Placing buttons
            self.view_list_steps.place(x= self.width*0.5, y= self.height*0.30, width = 250, height = 50, anchor ="n")
            self.edit_list_recipes.place(x= self.width*0.5, y= self.height*0.50, width = 250, height = 50, anchor ="n")
            self.edit_list_steps.place(x= self.width*0.5, y= self.height*0.60, width = 250, height = 50, anchor ="n")
            self.specification.place(x= self.width*0.5, y= self.height*0.85, width = 250, height = 50, anchor ="n")
            self.back_r.place(x= self.width*0.75, y= self.height*0.90, width = 70, height = 50, anchor ="n")
        elif (key ==3): # Menu
            #self.launch.pack()
            self.launch.place(x= self.width*0.5, y= self.height*0.35, width = 200, height = 50, anchor ="n")
            self.review.pack()
            self.review.place(x= self.width*0.5, y= self.height*0.65, width = 200, height = 50, anchor ="n")

    # ========================================= R E D I R E C T
        # ================== LAUNCH
    def show_list_of_steps_f(self):
        """ Function that allow the user to view the list of steps that they will follow
        """
        self.hide_buttons(2)
        ScheduleSubMenu(self.root, self.width, self.height, self.lang.lang, 1)

    def list_mode_f(self):
        """ Function that allow the launching of the preparation in list - mode
        """
        self.hide_buttons(2)
        ScheduleSubMenu(self.root, self.width, self.height, self.lang.lang, 2)

    def step_by_step_mode_f(self):
        """ Function that allow the launching of the preparation in a step - by - step mode
        """
        self.hide_buttons(2)
        ScheduleSubMenu(self.root, self.width, self.height, self.lang.lang, 3)

    def real_time_mode_f(self):
        """ Function that allow the launching of the preparation in real - time mode
        """
        self.hide_buttons(2)
        ScheduleSubMenu(self.root, self.width, self.height, self.lang.lang, 4)

        # ================== REVIEW
    def view_list_steps_f (self):
        """ Function that allows the user to visualize the number of steps and possibly edit it
        """
        self.hide_buttons(3)
        ScheduleSubMenu(self.root, self.width, self.height, self.lang.lang, 5)
        
    def edit_list_recipes_f (self):
        """ Function that allows the user to edit their list of recipes
        """
        self.hide_buttons(3)
        ScheduleSubMenu(self.root, self.width, self.height, self.lang.lang, 6)
        
    def edit_list_step_f (self):
        """ Function that allows the user to edit their list of steps
        """
        self.hide_buttons(3)
        ScheduleSubMenu(self.root, self.width, self.height, self.lang.lang, 7)
        
    def specification_f (self):
        """ Function that allows the user to specify what tye of kitchen tools they use and whatever else...
                                O P T I O N (when everything is finished)
        """
        self.hide_buttons(3)
        ScheduleSubMenu(self.root, self.width, self.height, self.lang.lang, 8)

# =================================================== SUB CLASSes of SCHEDULE
class ScheduleSubMenu:
    def __init__(self, root, width, height, lang, key):
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
        #distribution
        if (key == 1):
            ShowListSteps(self.can, self.width, self.height, self.lang.lang)
        elif (key == 2):
            ListMode(self.can, self.width, self.height, self.lang.lang)
        #elif (key == 3):
            StepByStep(self.can, self.width, self.height, self.lang.lang)
        #elif (key == 4):

        #elif (key == 5):

        #elif (key == 6):

class ShowListSteps :  
    def __init__(self, can, width, height, lang):
        # Variables
        self.can, self.width, self.height, self.lang = can, width, height, Language(lang)
            # Index is of the form index = i[3], with i < [0, +inf[
        self.index = 0
        # Image
        self.three_dots = tk.PhotoImage(file=r"img/three_dots.png")
        # Buttons
        self.back =tk.Button(self.can, image=self.three_dots,
            background="white", highlightthickness=0, command = self.back_f)
        self.next =tk.Button(self.can, font=("Calibri", 10), image=self.three_dots,
            background="white", highlightthickness=0, command = self.next_f)
            # pack and place
        self.next.pack()
        self.next.place(x=self.width*0.5, y=self.height*0.9, width = 100, height = 30, anchor = "n")
        
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
        self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h - self.step - self.step_h,
                                  self.middle_w + self.step_w, self.middle_h - self.step + self.step_h, fill='orange', outline='white')
                # middle
        self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h - self.step_h,
                                  self.middle_w + self.step_w, self.middle_h + self.step_h, fill='orange', outline='white')
                # down
        self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h + self.step - self.step_h,
                                  self.middle_w + self.step_w, self.middle_h + self.step + self.step_h, fill='orange', outline='white')
        
        # Functions for the buttons
    def back_f(self):
        """Function that allow the user to get back on the list
        """
        
    def next_f(self):
        """Function that allow the user to get back on the list
        """
        self.back.pack()
        self.back.place(x=self.width*0.5, y=self.height*0.05, width = 100, height = 30, anchor = "n")
        
# ===================================
class ListMode:
    def __init__(self, can, width, height, lang):
        # Variables
        self.can, self.width, self.height, self.lang = can, width, height, Language(lang)
        # Image
        self.arrow_u = tk.PhotoImage(file=r"img/arrow_u.png")
        self.arrow_d = tk.PhotoImage(file=r"img/arrow_d.png")
        # Buttons
        self.back =tk.Button(self.can, image=self.arrow_u,
            background="white", highlightthickness=0, command = self.back_f)
        self.next =tk.Button(self.can, font=("Calibri", 10), image=self.arrow_d,
            background="white", highlightthickness=0, command = self.next_f)
            # pack and place
        self.next.pack()
        self.next.place(x=self.width*0.015, y=self.height*0.84, width = 100, height = 100, anchor = "sw")
        
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
        self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h - self.step - self.step_h,
                                  self.middle_w + self.step_w, self.middle_h - self.step + self.step_h, fill='orange', outline='white')
                # middle
        self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h - self.step_h,
                                  self.middle_w + self.step_w, self.middle_h + self.step_h, fill='orange', outline='white')
                # down
        self.can.create_rectangle(self.middle_w - self.step_w, self.middle_h + self.step - self.step_h,
                                  self.middle_w + self.step_w, self.middle_h + self.step + self.step_h, fill='orange', outline='white')
        
        # Functions for the buttons
    def back_f(self):
        """Function that allow the user to get back on the list
        """
        
    def next_f(self):
        """Function that allow the user to get back on the list
        """
        self.back.pack()
        self.back.place(x=self.width*0.015, y=self.height*0.16, width = 100, height = 100, anchor = "nw")

class StepByStep:
    def __init__(self, can, width, height, lang):
        # Variables
        self.can, self.width, self.height, self.lang = can, width, height, Language(lang)
        # 

# ============================================================= MAIN FRAME =======================================================================

class MainFrame:
    def __init__(self, root, width, height, lang):
        self.root = root
        self.width, self.height = width, height
        self.root.geometry(str(width) + "x" + str(height))
        self.lang = Language(lang)
        self.root.title(self.lang.title)
        self.root.configure(bg='white')
        # ====== Resize
        #self.root.minsize(self.width, self.height)
        #self.root.maxsize(self.width +100, self.height +70)
        self.root.resizable(width=False, height=False)
        # { when we will want to be able to resize the window: how to know the size choosen :::}
        # actualwidth = self.root.winfo_screenwidth()
        # actualheight = self.root.winfo_screenheight()
        # ================= Launching Main
        MainMenu(self.root, self.width, self.height, self.lang.lang)
        # ================= Main Loop =================
        self.root.mainloop()