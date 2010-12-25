'''
Project : Tarot Web [https://launchpad.net/tarot]
Author  : nfk
Date    : 25 oct. 2009
'''

class Joueur:
    '''
    definition d un joueur de tarot
    '''
    
    def __init__(self, ident):
        '''
        Constructor
        '''
        self.identifiant = ident
        self.score = 0
        self.prise = ""
        self.cartes = []

    def joueCarte(self, index):
        carte = self.cartes[index]
        self.cartes.remove(carte)
        return carte;

    def getCartes(self):
        return self.cartes

    def setCarte(self, carte):
        self.cartes.append(carte)

    def hasCouleur(self, couleur):
        for carte in self.cartes:
            if carte.couleur == couleur:
                return True
        return False
    
    def hasAtoutSuperieur(self, valeur):
        for carte in self.cartes:
            if carte.valeur > valeur:
                return True
        return False
