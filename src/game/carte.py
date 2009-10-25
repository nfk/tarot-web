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
        '''
        Constructor
        '''
        self.__nom      = str(nom)
        self.__valeur   = int(valeur)
        self.__point    = float(point)
        self.__couleur  = str(couleur)
    
    def __str__(self):
        return self.__nom + " " + self.__couleur
    
    def info(self):
        return self.__nom + "\t" + self.__couleur + \
                    "\t" +  str(self.__point) + "\t" + str(self.__valeur)


        