'''
Project : Tarot Web [https://launchpad.net/tarot]
Author  : nfk
Date    : 24 oct. 2009
'''

from constantes import TypeCarte
from constantes import ReglePartie
from carte import Carte
from joueur import Joueur

from erreurs import MaxJoueursAtteint

class Partie:
    '''
    ensemble des cartes du jeu de tarot
    '''

    def __init__(self, nb_joueurs):
        '''
        Constructor
        '''
        # variables
        self.__nbJoueurs = nb_joueurs
        self._cartes = []
        self._joueurs = []
        
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
                
    def getCartes(self):
        return self._cartes
    
    def getJoueurs(self):
        return self._joueurs
    
    
    def addJoueur(self, joueur):
        '''
        ajout d un joueur a la partie
        '''
        if self._joueurs.__len__() == self.__nbJoueurs:
            raise MaxJoueursAtteint()
            
        self._joueurs.append(joueur)
        
    
    def distribution(self, joueurs):
        pass

            