'''
Project : Tarot Web [https://launchpad.net/tarot]
Author  : nfk
Date    : 25 oct. 2009
'''

class Joueur:
    '''
    classdocs
    '''
    
    def __init__(self, ident):
        '''
        Constructor
        '''
        self.__identifiant = ident
        self.__score = 0
        self.__prise = ""
        self.__cartes = []


    def __str__(self):
        return str(self.__identifiant)

    def joueCarte(self, index):
        carte = self.__cartes[index]
        self.__cartes.remove(carte)
        return carte;

    def getCartes(self):
        return self.__cartes

    def setCarte(self, carte):
        self.__cartes.append(carte)
        
    def getIdentifiant(self):
        return self.__identifiant

    def hasCouleur(self, couleur):
        for carte in self.__cartes:
            if carte.couleur == couleur:
                return True
        return False
    
    def hasAtoutSuperieur(self, valeur):
        for carte in self.__cartes:
            if carte.valeur > valeur:
                return True
        return False
        

    cartes = property(getCartes, None, None, None)

    identifiant = property(getIdentifiant, None, None, None)



