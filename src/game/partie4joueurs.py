'''
Project : Tarot Web [https://github.com/nfk/tarot-web]
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
        
        
