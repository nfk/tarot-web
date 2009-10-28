'''
Project : Tarot Web [https://launchpad.net/tarot]
Author  : nfk
Date    : 25 oct. 2009
'''

import unittest

from constantes import TypeCarte
from partie4joueurs import Partie4Joueurs
from joueur import Joueur
import erreurs 

class ListeCartesJeuTarot(unittest.TestCase):
    '''
    test le jeu de carte
    '''

    def testCartes(self):
        partie = Partie4Joueurs()
#        print ""
#        for carte in c.getCartes():
#            print carte.info()
        self.assertEquals(partie.cartes.__len__(), TypeCarte.NB_CARTES)
        
    
    def testAddJoueurs(self):
        partie = Partie4Joueurs()
        for i in range(4):
            j = Joueur("joueur" + str(i+1))
            partie.addJoueur(j)
        
        self.assertEquals(partie.joueurs.__len__(), 4)
        
        j =  Joueur("newJoueur")
        self.assertRaises(erreurs.MaxJoueursAtteint, partie.addJoueur, j)
        
    def testDistribution(self):
        partie = Partie4Joueurs()
        
        # distrib sans add joueur
        self.assertRaises(erreurs.ManqueJoueurs, partie.distribution)
        
        # add des 4 joueurs
        for i in range(4):
            j = Joueur("joueur" + str(i+1))
            partie.addJoueur(j)
        
        self.assertEquals(partie.joueurs.__len__(), 4)
        
        #distrib des cartes
        partie.distribution()
        self.assertEquals(partie.cartesAuChien.__len__(), 6)
        
        # chaque joueur a le bon nombre de cartes
        for joueur in partie.joueurs:
            print joueur.identifiant
            print joueur.cartes
            self.assertEquals(joueur.cartes.__len__(), 18)
        

