'''
Project : Tarot Web [https://launchpad.net/tarot]
Author  : nfk
Date    : 28 dec. 2010
'''
from constantes import TypeCarte

class InfoJeu:
    nbRois = 0
    nbOutdlers = 0
    nbAtouts = 0
    moyAtouts = 0
    moyCarteNormale = 0
    points = 0.0

class StatsMainJoueur:
    '''
    information sur le jeu du joueur
    '''

    def __init__(self):
        ''' Constructeur '''
        self.info = InfoJeu()
    
    def calcul(self, cartes):
        ''' calcul les stats sur le jeu de cartes '''
        self.__countAtout()
        self.__countOutdlers()
        self.__countRoi()
        self.__moyAtouts(cartes)
        self.__moyCarteNormale(cartes)


    def __countOutdlers(self):
        ''' compte le nombre de bouts dans le jeu '''
        for carte in self.cartes:
            if carte.couleur is 'atout':
                if TypeCarte.OUTDLERS.values().count(carte.valeur) > 0:
                    self.info.nbOutdlers += 1               
    
    def __countAtout(self):
        ''' compte le nombre d'atout dans le jeu '''
        for carte in self.cartes:
            if carte.couleur is 'atout':
                self.info.nbAtouts += 1               
                
    def __countRoi(self):
        ''' compte le nombre de roi dans le jeu '''
        for carte in self.cartes:
            if carte.nom is 'roi':
                self.info.nbRois += 1          
        
    def __moyAtouts(self, cartes):
        ''' valeur moyenne des atouts'''
        # TODO pourcentage des atouts
        atouts = []
        for carte in cartes:
            if carte.couleur is 'atout':
                atouts.append(carte.valeur)
                
        self.info.moyAtouts = sum(atouts)*100 / sum(TypeCarte.ATOUT.values()) 
        
    def __moyCarteNormale(self, cartes):
        ''' valeur moyenne des cartes standard '''
        values = []
        for carte in cartes:
            if carte.couleur is not 'atout':
                values.append(carte.valeur)
        
        self.info.moyCarteNormale = sum(values)/len(values)
                 
    def __point(self, cartes):
        ''' valeur en point des cartes '''
        points = []
        for carte in cartes:
            points.append(carte.point)
        
        self.info.points = sum(points)
        