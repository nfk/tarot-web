'''
Project : Tarot Web [https://launchpad.net/tarot]
Author  : nfk
Date    : 25 oct. 2009
'''

import unittest

from constantes import TypeCarte
from partie4joueurs import Partie4Joueurs
from joueur import Joueur
from erreurs import MaxJoueursAtteint

class ListeCartesJeuTarot(unittest.TestCase):
    '''
    test le jeu de carte
    '''

    def testCartes(self):
        partie = Partie4Joueurs()
#        print ""
#        for carte in c.getCartes():
#            print carte.info()
        self.assertEquals(partie.getCartes().__len__(), TypeCarte.NB_CARTES)
        
    
    def testAddJoueurs(self):
        partie = Partie4Joueurs()
        ident = "joueur"
        for i in range(4):
            j = Joueur(ident + str(i))
            partie.addJoueur(j)
        
        self.assertEquals(partie.getJoueurs().__len__(), 4)
        
        j =  Joueur("newJoueur")
        self.assertRaises(MaxJoueursAtteint, partie.addJoueur, j)

