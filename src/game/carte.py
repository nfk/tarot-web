'''
Project : Tarot Web [https://launchpad.net/tarot]
Author  : nfk
Date    : 25 oct. 2009
'''

class Carte:
    '''
    objet carte
    '''
  
    def __init__(self, nom, valeur, point, couleur):
        ''' Constructor '''
        self.nom      = str(nom)
        self.valeur   = int(valeur)
        self.point    = float(point)
        self.couleur  = str(couleur)
    
    def __str__(self):
        return str(self.couleur)
    
    def __repr__(self):
        return repr(self.nom + " " + self.couleur)
    
    def info(self):
        return self.nom + "\t" + self.couleur + \
                    "\t" +  str(self.point) + "\t" + str(self.valeur)


        