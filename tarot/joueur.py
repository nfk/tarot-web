'''
Project : Tarot Web [https://github.com/nfk/tarot-web]
Author  : nfk
Date    : 25 oct. 2009
'''


class Joueur(object):
    '''
    This class defined all action of player
    '''

    def __init__(self, ident):
        self.identifiant = ident
        self.score = 0
        self.prise = 'passe'
        self.cartes = []

    def joueCarte(self, index):
        ''' remove card and return it '''
        carte = self.cartes[index]
        self.cartes.remove(carte)
        return carte

    def addCarte(self, carte):
        ''' add card to player '''
        self.cartes.append(carte)

    def hasCouleur(self, couleur):
        ''' check if the player has a card in his game '''
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

    def __str__(self):
        ''' return string of player's cards'''
        s = ''
        for carte in self.cartes:
            s = '%s\n%s' % (s, str(carte))
        return s
