'''
Project : Tarot Web [https://launchpad.net/tarot]
Author  : nfk
Date    : 24 oct. 2009
'''

import random

from constantes import TypeCarte
from constantes import ReglePartie
from carte import Carte

import erreur

class Partie:
    '''
    ensemble des cartes du jeu de tarot
    '''

    def __init__(self, nbJoueurs, nbCarteAuChien):
        ''' Constructor '''
        # constante
        self.__NB_CARTES_AU_CHIEN = nbCarteAuChien
        self.__NB_JOUEURS = nbJoueurs
        
        # variables
        self.cartes = []
        self.cartesAuChien = []
        self.joueurs = []
        
        # initialisation
        self.__creationJeu()
        
    def __creationJeu(self):
        ''' creation du jeu de tarot '''
        for couleur in TypeCarte.COULEUR_ET_ATOUT.iterkeys():
            iterCartes = TypeCarte.BASIC.items()
            if couleur == 'atout':
                iterCartes = TypeCarte.ATOUT.items()

            for nom, valeur in iterCartes:
                point = ReglePartie.POINT.get(nom)
                if TypeCarte.OUTDLERS.get(nom) is not None:
                    point = ReglePartie.POINT['outdler']
                if point is None:
                    point = ReglePartie.POINT['base']
                self.cartes.append(Carte(nom, valeur, point, couleur))


    def addJoueur(self, joueur):
        '''ajout d un joueur a la partie'''
        
        if len(self.joueurs) == self.__NB_JOUEURS:
            raise erreur.MaxJoueursAtteint()
            
        self.joueurs.append(joueur)
        
    
    def distribution(self):
        ''' distrubutions des cartes au joueur et creation du chien '''
        # variables
        carte = None
        cartesTmp = self.cartes
        self.cartesAuChien = []
        
        # la partie a tous ces joueurs
        if len(self.joueurs) != self.__NB_JOUEURS:
            raise erreur.ManqueJoueurs()
        
        # on fait d abord le chien
        while len(self.cartesAuChien) < self.__NB_CARTES_AU_CHIEN:
            carte = random.choice(cartesTmp)
            self.cartesAuChien.append(carte)
            cartesTmp.remove(carte)
        
        # distribution du restant des cartes aux joueurs   
        while len(cartesTmp) > 0:
            for joueur in self.joueurs:
                carte = random.choice(cartesTmp)
                joueur.addCarte(carte)
                cartesTmp.remove(carte)

            