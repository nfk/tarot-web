'''
Project : Tarot Live [https://launchpad.net/tarot]
Author  : nfk
Date    : 25 oct. 2009
'''

from partie import Partie

class Partie4Joueurs(Partie):
    '''
    Partie de tarot pour 4 joueurs
    '''

    def __init__(self):
        ''' Constructeur '''
        Partie.__init__(self, nbJoueurs=4, nbCarteAuChien=6)
        
        