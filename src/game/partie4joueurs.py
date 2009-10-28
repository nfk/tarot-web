'''
Project : Tarot Web [https://launchpad.net/tarot]
Author  : nfk
Date    : 25 oct. 2009
'''

from partie import Partie

class Partie4Joueurs(Partie):
    '''
    Partie de tarot pour 4 joueurs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        JOUEURS = 4
        CARTES_AU_CHIEN = 6
        
        Partie.__init__(self, JOUEURS, CARTES_AU_CHIEN)
        
        