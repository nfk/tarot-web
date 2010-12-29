'''
Project : Tarot Web [https://launchpad.net/tarot]
Author  : nfk
Date    : 29 dec. 2010
'''
import unittest
from partie4joueurs import Partie4Joueurs
from joueur import Joueur
from statistique import StatsMainJoueur

class Test(unittest.TestCase):

    def testStats(self):
        stats = StatsMainJoueur()
        partie = Partie4Joueurs()
        joueur1 = Joueur('joueur1')
        joueur2 = Joueur('joueur2')
        joueur3 = Joueur('joueur3')
        joueur4 = Joueur('joueur4')
        
        partie.addJoueur(joueur1)
        partie.addJoueur(joueur2)
        partie.addJoueur(joueur3)
        partie.addJoueur(joueur4)
        
        stats.calcul(partie.cartes)
        stats.printStats()
        
        partie.distribution()
        #joueur1.printCartes()
        stats.calcul(joueur1.cartes)
        stats.printStats()
        
