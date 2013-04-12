'''
Project : Tarot Web [https://github.com/nfk/tarot-web]
Author  : nfk
Date    : 28 dec. 2010
'''
import unittest
from joueur import Joueur
from carte import Carte


class TestJoueur(unittest.TestCase):

    def testJoueur(self):  
        j = Joueur('test')
        j.addCarte(Carte('quatre', 4, 0.5, 'atout'))
        j.addCarte(Carte('quatorze', 14, 0.5, 'atout'))
        j.addCarte(Carte('quatre', 4, 0.5, 'pique'))
        j.addCarte(Carte('six', 6, 0.5, 'pique'))
        j.addCarte(Carte('roi', 14, 4.5, 'pique'))
        j.addCarte(Carte('roi', 14, 4.5, 'coeur'))
        j.addCarte(Carte('reine', 13, 3.5, 'coeur'))
        j.addCarte(Carte('as', 1, 0.5, 'coeur'))
        
        self.assertEquals(j.hasAtoutSuperieur(15), False)
        self.assertEquals(j.hasAtoutSuperieur(14), False)
        self.assertEquals(j.hasAtoutSuperieur(13), True)
        
        self.assertEquals(j.hasCouleur('atout'), True)
        self.assertEquals(j.hasCouleur('trefle'), False)
