'''
Project : Tarot Web [https://launchpad.net/tarot]
Author  : nfk
Date    : 25 oct. 2009
'''

class Carte:
    '''
    carte de tarot
    '''
  
    def __init__(self, nom, valeur, point, couleur):
        self.nom      = str(nom)
        self.valeur   = int(valeur)
        self.point    = float(point)
        self.couleur  = str(couleur)
    
    def info(self):
        ''' renvoi une chaine d'info sur la carte'''
        return self.nom + "(" + str(self.valeur) + ") " + self.couleur + \
                    " - valeur=" +  str(self.point)


        