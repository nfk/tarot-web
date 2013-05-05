'''
Project : Tarot Web [https://github.com/nfk/tarot-web]
Author  : nfk
Date    : 25 oct. 2009
'''


class Carte:
    '''
    carte de tarot
    '''

    def __init__(self, nom, valeur, point, couleur):
        ''' Constructeur '''
        self.nom = str(nom)
        self.valeur = int(valeur)
        self.point = float(point)
        self.couleur = str(couleur)

    def name(self):
        ''' renvoi le nom de la carte'''
        return '%s_%s' % (self.nom, self.couleur)

    def info(self):
        ''' renvoi une chaine d'info sur la carte '''
        return "%s(%d) %s - point = %.1f" % (self.nom, self.valeur,
                                             self.couleur, self.point)
