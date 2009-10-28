'''
Project : Tarot Web [https://launchpad.net/tarot]
Author  : nfk
Date    : 24 oct. 2009
'''

import random


from constantes import TypeCarte
from constantes import ReglePartie
from carte import Carte
from joueur import Joueur

import erreurs

class Partie:
    '''
    ensemble des cartes du jeu de tarot
    '''

    def __init__(self, nbJoueurs, nbCarteAuChien):
        '''
        Constructor
        '''
        # constante
        self.__NB_CARTES_AU_CHIEN = nbCarteAuChien
        self.__NB_JOUEURS = nbJoueurs
        
        # variables
        self._cartes    = []
        self._cartesAuChien     = []
        self._joueurs   = []
        
        # initialisation
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
                self._cartes.append(Carte(nom, valeur, point, couleur))


    def addJoueur(self, joueur):
        '''
        ajout d un joueur a la partie
        '''
        if self._joueurs.__len__() == self.__NB_JOUEURS:
            raise erreurs.MaxJoueursAtteint()
            
        self._joueurs.append(joueur)
        
    
    def distribution(self):
        
        # variables
        carte = None
        cartesTmp = self._cartes
        
        # la partie a tous ces joueurs
        if self._joueurs.__len__() != self.__NB_JOUEURS:
            raise erreurs.ManqueJoueurs()
        
        # au fait d abord le chien
        for i in range(self.__NB_CARTES_AU_CHIEN):
            carte = random.choice(cartesTmp)
            self._cartesAuChien.append(carte)
            cartesTmp.remove(carte)
        
        # distribution du restant des cartes aux joueurs   
        while cartesTmp.__len__() > 0:
            for joueur in self._joueurs:
                carte = random.choice(cartesTmp)
                joueur.setCarte(carte)
                cartesTmp.remove(carte)


    def getCartes(self):
        return self._cartes


    def getCartesAuChien(self):
        return self._cartesAuChien


    def getJoueurs(self):
        return self._joueurs
    
    cartes = property(getCartes, None, None, None)

    cartesAuChien = property(getCartesAuChien, None, None, None)

    joueurs = property(getJoueurs, None, None, None)

            