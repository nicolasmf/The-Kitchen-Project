## ========================================== C L A S S E S ====================================
"""
File that contains all the classes of The_Kitchen_Project.

"""
class language(object):
    """Class that allow the user to change language
    """
    def __init__(self, choice):
        """Initialisation of the class language
        """
        # French
        if choice=="FR":
            self.searchbartxt = "Taper votre recherche ici"
            self.profile = "Mon profil"
        # English (by default)
        else :
            self.searchbartxt = "Type something here"
            self.profile = "My profile"

