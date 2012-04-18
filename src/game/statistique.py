'''
Project : Tarot Web [https://launchpad.net/tarot]
Author  : nfk
Date    : 28 dec. 2010
'''
from constantes import TypeCarte
from constantes import ReglePartie
from copy import deepcopy

class InfoJeu:
    nbRois = 0
    nbOutdlers = 0
    nbAtouts = 0
    nbCouleur = deepcopy(TypeCarte.COULEUR)
    moyAtouts = 0
    moyCarteNormale = 0
    points = 0

class StatsMainJoueur:
    '''
    information sur le jeu du joueur
    '''

    def __init__(self):
        ''' Constructeur '''
        self.info = InfoJeu()
        self.cartes = []
    
    def calcul(self, cartes):
        ''' calcul les stats sur le jeu de cartes '''
        self.cartes = cartes
        self.__razInfo()
        self.__countAtout()
        self.__countOutdlers()
        self.__countRoi()
        self.__countCouleur()
        self.__pourcentAtouts()
        self.__pourcentCarteFortes()
        self.__pourcentPoint()

    def printStats(self):
        ''' affiche les stats du jeu '''
        print '\n ___________________________________'
        print 'Nombre atouts = ' + str(self.info.nbAtouts)
        print 'Nombre outdlers = ' + str(self.info.nbOutdlers)
        print 'Nombre rois = ' + str(self.info.nbRois)
        for couleur, valeur in self.info.nbCouleur.items():
            print 'Nombre ' + couleur + ' = ' + str(valeur)
        print 'Atouts = ' + str(self.info.moyAtouts) + '%'
        print 'Cartes fortes = ' + str(self.info.moyCarteNormale) + '%'
        print 'Point du jeu = ' + str(self.info.points) + '%'

    def __razInfo(self):
        ''' mise a zero des stats'''
        self.info.nbRois = 0
        self.info.nbOutdlers = 0
        self.info.nbAtouts = 0
        for couleur in self.info.nbCouleur.keys():
            self.info.nbCouleur[couleur] = 0
        self.info.moyAtouts = 0
        self.info.moyCarteNormale = 0
        self.info.points = 0

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
        
    def __pourcentAtouts(self):
        ''' valeur moyenne des atouts'''
        atouts = []
        for carte in self.cartes:
            if carte.couleur is 'atout':
                atouts.append(carte.valeur)
                
        self.info.moyAtouts = sum(atouts)*100 / sum(TypeCarte.ATOUT.values()) 
        
    def __pourcentCarteFortes(self):
        ''' valeur moyenne des cartes standard '''
        values = []
        for carte in self.cartes:
            if carte.couleur is not 'atout' and carte.point > 0.5:
                values.append(carte)
              
        self.info.moyCarteNormale = len(values)*100 / TypeCarte.NB_TETES
                 
    def __pourcentPoint(self):
        ''' valeur en point des cartes '''
        points = []
        for carte in self.cartes:
            points.append(carte.point)
        
        self.info.points = int(sum(points)*100 / ReglePartie.POINT['total'])
        
    def __countCouleur(self):
        ''' calcul le nombre de cartes dans chaque couleurs '''
        for carte in self.cartes:
            if TypeCarte.COULEUR.has_key(carte.couleur):
                self.info.nbCouleur[carte.couleur] += 1
        
        