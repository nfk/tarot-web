'''
Project : Tarot Web [https://launchpad.net/tarot]
Author  : nfk
Date    : 24 oct. 2009
'''

from constantes import TypeCarte
from constantes import ReglePartie

class Carte:
    '''
    objet carte
    '''
  
    def __init__(self, nom, valeur, point, couleur):
        '''
        Constructor
        '''
        self.__nom      = str(nom)
        self.__valeur   = int(valeur)
        self.__point    = float(point)
        self.__couleur  = str(couleur)
    
    def __str__(self):
        return self.__nom + " " + self.__couleur
    
    def info(self):
        return self.__nom + "\t" + self.__couleur + \
                    "\t" +  str(self.__point) + "\t" + str(self.__valeur)


class Cartes:
    '''
    ensemble des cartes du jeu de tarot
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.__cartes = []
        self.__creationJeu()
        
    def __creationJeu(self):
        '''
        creation du jeu de tarot
        '''
        for couleur in TypeCarte.COULEUR.iterkeys():
            iterCartes = TypeCarte.BASIC.items()
            if couleur == 'atout':
                iterCartes = TypeCarte.ATOUT.items()

            for nom, valeur in iterCartes:
                point = ReglePartie.POINT.get(nom)
                if TypeCarte.OUTDLERS.get(nom) is not None:
                    point = ReglePartie.POINT['outdler']
                if point is None:
                    point = ReglePartie.POINT['base']
                self.__cartes.append(Carte(nom, valeur, point, couleur))
                
    def getCartes(self):
        '''
        accesseurs sur le jeu de tarot
        '''
        return self.__cartes


        