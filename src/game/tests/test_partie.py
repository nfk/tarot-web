'''
Project : Tarot Web [https://launchpad.net/tarot]
Author  : nfk
Date    : 25 oct. 2009
'''

import unittest

from constantes import TypeCarte
from partie4joueurs import Partie4Joueurs
from joueur import Joueur
import erreur 

class TestPartie(unittest.TestCase):

    def testCartes(self):
        partie = Partie4Joueurs()
        self.assertEquals(len(partie.cartes), TypeCarte.NB_CARTES)
        
    
    def testAddJoueurs(self):
        partie = Partie4Joueurs()
        for i in range(4):
            j = Joueur("joueur" + str(i+1))
            partie.addJoueur(j)
        
        self.assertEquals(len(partie.joueurs), 4)
        
        j =  Joueur("newJoueur")
        self.assertRaises(erreur.MaxJoueursAtteint, partie.addJoueur, j)
        
    def testDistribution(self):
        partie = Partie4Joueurs()
        
        # distrib sans add joueur
        self.assertRaises(erreur.ManqueJoueurs, partie.distribution)
        
        # add des 4 joueurs
        for i in range(4):
            j = Joueur("joueur" + str(i+1))
            partie.addJoueur(j)
        
        self.assertEquals(len(partie.joueurs), 4)
        
        #distrib des cartes
        partie.distribution()
        self.assertEquals(len(partie.cartesAuChien), 6)
        
        # chaque joueur a le bon nombre de cartes
        for joueur in partie.joueurs:
            self.assertEquals(len(joueur.cartes), 18)
        