'''
Project : Tarot Web [https://github.com/nfk/tarot-web]
Author  : nfk
Date    : 17 dec. 2010
'''
from collections import namedtuple


class Pli:
    '''
    gestion des plis pour 4 joueurs
    '''

    def __init__(self):
        self.pli = []
        self.Couple = namedtuple('Couple', 'carte joueur')
        self.nb_joueurs = 4

        self.point = 0
        self.winner = None

    def add(self, carte, joueur):
        ''' ajout d une carte au pli '''

        if len(self.pli) == self.nb_joueurs:
            raise Exception('Pli Complet')

        if len(self.pli) > 0:
            for p in self.pli:
                if p.carte == carte:
                    raise Exception('Pli Carte Deja Jouee')
                if p.joueur == joueur:
                    raise Exception('Pli Joueur A Deja Joue')

        self.pli.append(self.Couple(carte, joueur))

    def controle(self, carte, joueur):
        ''' controle la carte a jouer par le joueur '''

        first = self.__firstCarte()

        # la premiere carte on joue ce qu on veux
        if first is None:
            return True

        # La carte est de la meme color
        if carte.color == first.color and carte.color != 'atout':
            return True

        # Le joueur joue un atout et n a pas la color demandee
        if (carte.color is 'atout' and
                joueur.hasCouleur(first.color) is False):
            # L atout est superieur
            valeurMax = self.__valeurMaxAtouts()
            if carte.value > valeurMax:
                return True
            # Le joueur fait pipi
            if (carte.value < valeurMax and
                    joueur.hasAtoutSuperieur(valeurMax) is False):
                return True

        # Le joueur n a pas la color demandee et pas d atout
        if (joueur.hasCouleur(first.color) is False and
                joueur.hasCouleur('atout') is False):
            return True

        return False

    def __firstCarte(self):
        ''' retourne la carte d ouverture du pli'''

        if len(self.pli) == 0:
            return None

        # La reference du controle c est la premiere carte
        # sauf si c est l excuse
        if self.pli[0].carte.name == 'excuse':
            if len(self.pli) >= 2:
                return self.pli[1].carte
        else:
            if len(self.pli) >= 1:
                return self.pli[0].carte

        return None

    def __valeurMaxAtouts(self):
        ''' recherche la valeur max des atouts presents dans le pli '''
        valeurMax = 0
        for p in self.pli:
            if p.carte.color is 'atout' and p.carte.value > valeurMax:
                valeurMax = p.carte.value

        return valeurMax

    def resultat(self):
        ''' recherche le vainqueur du pli et calcul le nombre de points '''
        if len(self.pli) < self.nb_joueurs:
            raise Exception('Pli Incomplet')

        current = self.__firstCarte()

        # recherche la carte gagnante
        for p in self.pli[1:self.nb_joueurs]:
            # carte joue ne correspond a rien
            if (p.carte.color != current.color and
                    p.carte.color != 'atout'):
                continue

            # la carte a ete coupee
            if p.carte.color != current.color:
                current = p.carte
                continue

            # la carte est de la meme color on compare la valeur
            if p.carte.value > current.value:
                current = p.carte
                continue

        # recherhe le joueur gagnant et calcul du score
        for p in self.pli:
            if p.carte == current:
                self.winner = p.joueur

            self.point = self.point + p.carte.point
