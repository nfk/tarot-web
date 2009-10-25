'''
Project : Tarot Web [https://launchpad.net/tarot]
Author  : nfk
Date    : 25 oct. 2009
'''

from carte import Carte

class Joueur:
    '''
    classdocs
    '''

    def __init__(self, ident):
        '''
        Constructor
        '''
        self.__identifiant = ""
        self.__score = 0
        self.__prise = ""
        self.__cartes = []
 
        
    def setCartes(self, cartes):
        self.__cartes = cartes
        
    def getCartes(self):
        return self.__cartes

    def joueCarte(self, index):
            return self.__cartes[index];
