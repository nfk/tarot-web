'''
Project : Tarot Web [https://github.com/nfk/tarot-web]
Author  : nfk
Date    : 25 oct. 2009
'''


class Carte:
    ''' card of tarot '''

    def __init__(self, nom, valeur, point, couleur):
        self.nom = nom
        self.valeur = int(valeur)
        self.point = float(point)
        self.couleur = couleur

    def name(self):
        ''' return name of card '''
        return '%s_%s' % (self.nom, self.couleur)

    def __str__(self):
        ''' return string with card attributes'''
        return '%s(%d) %s - point = %.1f' % (self.nom, self.valeur,
                                             self.couleur, self.point)
