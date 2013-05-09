'''
Project : Tarot Web [https://github.com/nfk/tarot-web]
Author  : nfk
Date    : 29 dec. 2010
'''
import unittest
from tarot.partie4joueurs import Partie4Joueurs
from tarot.joueur import Joueur
from tarot.statistique import StatsCartes
import tarot.constantes as constantes


class Test(unittest.TestCase):

    def testStats(self):
        stats = StatsCartes()
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
        self.assertEquals(stats.info.nbAtouts, len(constantes.ATOUT))
        self.assertEquals(stats.info.nbOutdlers, len(constantes.OUTDLERS))
        self.assertEquals(stats.info.nbRois, len(constantes.COULEUR))
        for c in constantes.COULEUR.keys():
            self.assertEquals(stats.info.nbCouleur[c], len(constantes.BASIC))
        self.assertEquals(stats.info.pourcentAtouts, 100)
        self.assertEquals(stats.info.pourcentCarteNormale, 100)
        self.assertEquals(stats.info.pourcentPoints, 100)
        #stats.printStats()

        partie.distribution()
        #joueur1.printCartes()
        stats.calcul(joueur1.cartes)
        #stats.printStats()

if __name__ == '__main__':
    unittest.main()
