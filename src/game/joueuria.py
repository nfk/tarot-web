'''
Project : Tarot Web [https://launchpad.net/tarot]
Author  : nfk
Date    : 28 dec. 2010
'''

from statistique import StatsMainJoueur

class JoueurIA:
    '''
    Inteligence artificielle d'un joueur fait pour une partie a 4
    '''

    def __init__(self, joueur):
        ''' Constructeur '''
        self.joueur = joueur
        
    def appel(self):
        ''' analyse du jeu et determine le type d'appel '''
        
        s = StatsMainJoueur
        s.calcul(self.joueur.cartes)
        
        s.info.pourcentPoints
        
        
 
        
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
    