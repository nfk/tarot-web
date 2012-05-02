'''
Project : Tarot Live [https://launchpad.net/tarot]
Author  : nfk
Date    : 25 oct. 2009
'''

class Carte:
    '''
    carte de tarot
    '''
  
    def __init__(self, nom, valeur, point, couleur):
        ''' Constructeur '''
        self.nom      = str(nom)
        self.valeur   = int(valeur)
        self.point    = float(point)
        self.couleur  = str(couleur)
    
    def name(self):
        ''' renvoi le nom de la carte'''
        return self.nom + '_' + self.couleur
    
    def info(self):
        ''' renvoi une chaine d'info sur la carte '''
        return self.nom + "(" + str(self.valeur) + ") " + self.couleur + \
                    " - point=" +  str(self.point)


        