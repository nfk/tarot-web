'''
Project : Tarot Web [https://github.com/nfk/tarot-web]
Author  : nfk
Date    : 28 dec. 2010
'''
import unittest
from tarot.joueur import Joueur
from tarot.carte import Carte


class TestJoueur(unittest.TestCase):

    def testJoueur(self):
        cards = [
            Carte('quatre', 4, 0.5, 'atout'),
            Carte('quatorze', 14, 0.5, 'atout'),
            Carte('quatre', 4, 0.5, 'pique'),
            Carte('six', 6, 0.5, 'pique'),
            Carte('roi', 14, 4.5, 'pique'),
            Carte('roi', 14, 4.5, 'coeur'),
            Carte('reine', 13, 3.5, 'coeur'),
            Carte('as', 1, 0.5, 'coeur')
        ]

        j = Joueur('test')
        strGame = ''
        for c in cards:
            j.addCarte(c)
            strGame = '%s\n%s' % (strGame, str(c))

        self.assertFalse(j.hasAtoutSuperieur(15))
        self.assertFalse(j.hasAtoutSuperieur(14))
        self.assertTrue(j.hasAtoutSuperieur(13))

        self.assertTrue(j.hasCouleur('atout'))
        self.assertFalse(j.hasCouleur('trefle'))

        self.assertTrue(str(j) == strGame)

if __name__ == '__main__':
        unittest.main()
