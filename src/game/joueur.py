'''
Project : Tarot Web [https://launchpad.net/tarot]
Author  : nfk
Date    : 25 oct. 2009
'''
from constantes import TypeCarte

class Joueur:
    '''
    definition d un joueur de tarot
    '''
    
    def __init__(self, ident):
        ''' Constructeur '''
        self.identifiant = ident
        self.score = 0
        self.prise = 'passe'
        self.cartes = []


    def joueCarte(self, index):
        ''' renvoi une carte et supprime la carte du joueur '''
        carte = self.cartes[index]
        self.cartes.remove(carte)
        return carte

    def addCarte(self, carte):
        ''' ajoute une carte au joueur '''
        self.cartes.append(carte)

    def hasCouleur(self, couleur):
        ''' le joueur a la couleur dans son jeu '''
        for carte in self.cartes:
            if carte.couleur == couleur:
                return True
        return False
    
    def hasAtoutSuperieur(self, valeur):
        ''' le joueur a un atout superieur'''
        for carte in self.cartes:
            if carte.valeur > valeur:
                return True
        return False
    
    def printCartes(self):
        ''' affiche les cartes du joueur '''
        print '\n'
        for carte in self.cartes:
            print carte.info()
            
    def countAtout(self):
        ''' compte le nombre d atouts '''
        nb = 0
        for carte in self.cartes:
            if carte.couleur == 'atout':
                nb = nb + 1
        return nb
    
    def countOutdlers(self):
        ''' compte le nombre d outdlers '''
        nb = 0
        for carte in self.cartes:
            if TypeCarte.OUTDLERS.get(carte.nom) is not None:
                nb = nb + 1
        return nb
          
    def countRoi(self):
        ''' compte le nombre de rois '''
        nb = 0
        for carte in self.cartes:
            if carte.nom == 'roi':
                nb = nb + 1
        return nb
