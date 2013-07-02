'''
Project : Tarot Web [https://github.com/nfk/tarot-web]
Author  : nfk
Date    : 28 dec. 2010
'''
import constantes
from copy import deepcopy


class InfoJeu:
    nbRois = 0
    nbOutdlers = 0
    nbAtouts = 0
    nbCouleur = deepcopy(constantes.COULEUR)
    pourcentAtouts = 0
    pourcentCarteNormale = 0
    pourcentPoints = 0


class StatsCartes:
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

    def __razInfo(self):
        ''' mise a zero des stats'''
        self.info.nbRois = 0
        self.info.nbOutdlers = 0
        self.info.nbAtouts = 0
        for color in self.info.nbCouleur.keys():
            self.info.nbCouleur[color] = 0
        self.info.pourcentAtouts = 0
        self.info.pourcentCarteNormale = 0
        self.info.pourcentPoints = 0

    def __countOutdlers(self):
        ''' compte le nombre de bouts dans le jeu '''
        for carte in self.cartes:
            if carte.color is 'atout':
                if constantes.OUTDLERS.values().count(carte.value) > 0:
                    self.info.nbOutdlers += 1

    def __countAtout(self):
        ''' compte le nombre d'atout dans le jeu '''
        for carte in self.cartes:
            if carte.color is 'atout':
                self.info.nbAtouts += 1

    def __countRoi(self):
        ''' compte le nombre de roi dans le jeu '''
        for carte in self.cartes:
            if carte.name is 'roi':
                self.info.nbRois += 1

    def __pourcentAtouts(self):
        ''' valeur moyenne des atouts'''
        atouts = []
        for carte in self.cartes:
            if carte.color is 'atout':
                atouts.append(carte.value)

        self.info.pourcentAtouts = (sum(atouts) * 100 /
                                    sum(constantes.ATOUT.values()))

    def __pourcentCarteFortes(self):
        ''' valeur moyenne des cartes standard '''
        values = []
        for carte in self.cartes:
            if carte.color is not 'atout' and carte.point > 0.5:
                values.append(carte)

        self.info.pourcentCarteNormale = (len(values) * 100 /
                                          constantes.NB_TETES)

    def __pourcentPoint(self):
        ''' valeur en point des cartes '''
        pourcentPoints = []
        for carte in self.cartes:
            pourcentPoints.append(carte.point)

        self.info.pourcentPoints = int(sum(pourcentPoints) * 100 /
                                       constantes.POINT['total'])

    def __countCouleur(self):
        ''' calcul le nombre de cartes dans chaque colors '''
        for carte in self.cartes:
            if carte.color in constantes.COULEUR:
                self.info.nbCouleur[carte.color] += 1
