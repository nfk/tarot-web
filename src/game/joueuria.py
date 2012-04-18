'''
Project : Tarot Web [https://launchpad.net/tarot]
Author  : nfk
Date    : 28 dec. 2010
'''

class JoueurIA:
    '''
    Inteligence artificielle d'un joueur fait pour une partie a 4
    '''

    def __init__(self, joueur):
        ''' Constructeur '''
        self.joueur = joueur
        
    def appel(self):
        ''' analyse du jeu et determine le type d'appel '''
        #Todo joueur ponderer moyenne atout et moyenne tete du jeu du joueur
        
        j = self.joueur
        
        # Si on a pas plus de 4 atouts, 1 roi et 1 bout au minimum, on passe
        if j.countAtout() < 4 and j.countRoi() < 2 and j.countOutdlers() < 2:
            return 'passe'
        
        # Si on a 2 rois peu d'atout et un bout
        if j.countAtout() < 6  and j.countRoi() == 2 and j.countOutdlers() == 1:
            return 'petite'
        
        # Si on a 1 roi, des atouts et un bout
        if j.countAtout() > 6 and j.countAtout() < 9 and j.countRoi() == 1 and\
            j.countOutdlers() == 1:
            return 'petite' 
        
        # Si on a 2 bouts et un petit jeu
        if j.countAtout() < 6 and j.countRoi() == 1 and j.countOutdlers() == 2:
            return 'petite' 
        
        # Si on a 2 rois 2 bouts et 4 ou plus d'atouts
        if j.countAtout() >= 4  and j.countRoi() == 2 and\
            j.countOutdlers() == 1:
            return 'garde'
        
        # Si on a 2 rois 2 bouts et 4 ou plus d'atouts
        if j.countAtout() >= 4  and j.countRoi() == 2 and\
            j.countOutdlers() == 1:
            return 'garde'
        
        # cas oublie...
        return 'petite'  
        
    def chien(self):
        ''' analyse le jeu et joue n cartes au chien '''
        # obtenir coupe possible ?
         
        
        #self.joueur.joueCarte()
        pass
        
    def annonce(self):
        ''' le joueur peut faire des annonces '''
        pass
    
    def joue(self): 
        pass
    