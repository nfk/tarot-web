'''
Project : Tarot Web [https://github.com/nfk/tarot-web]
Author  : nfk
Date    : 2 mai 2012
'''
import unittest
from joueuria import JoueurIA
from carte import Carte
from constantes import ReglePartie


class TestJoueurIA(unittest.TestCase):

    def testAppel(self):

        j = JoueurIA('IA player')

        self.assertEquals(j.appel(), 'passe')

        j.addCarte(Carte('quatre', 4, 0.5, 'atout'))
        j.addCarte(Carte('roi', 14, 4.5, 'trefle'))
        j.addCarte(Carte('roi', 14, 4.5, 'coeur'))
        j.addCarte(Carte('petit', 1, 4.5, 'atout'))
        j.addCarte(Carte('valet', 11, 1.5, 'trefle'))
        j.addCarte(Carte('reine', 13, 3.5, 'trefle'))
        j.addCarte(Carte('reine', 13, 3.5, 'coeur'))
        j.addCarte(Carte('quatre', 4, 0.5, 'trefle'))
        j.addCarte(Carte('quatre', 4, 0.5, 'coeur'))

        self.assertEquals(j.appel(), 'petite')

        j.addCarte(Carte('valet', 11, 1.5, 'coeur'))
        j.addCarte(Carte('valet', 11, 1.5, 'pique'))
        j.addCarte(Carte('excuse', 0, 4.5, 'atout'))

        self.assertEquals(j.appel(), 'garde')

        j.addCarte(Carte('cavalier', 12, 2.5, 'pique'))
        j.addCarte(Carte('cavalier', 12, 2.5, 'trefle'))

        self.assertEquals(j.appel(), 'garde_sans')

        j.addCarte(Carte('vingt-et-un', 0, 4.5, 'atout'))

        self.assertEquals(j.appel(), 'garde_contre')

    def testAnnonce(self):
        j = JoueurIA('IA player')

        self.assertEquals(j.annonce(), None)

        for i in range(ReglePartie.POIGNEE['simple']):
            j.addCarte(Carte("unknown", i, 0.5, 'atout'))

        self.assertEquals(j.annonce(), 'simple')

        for i in range(
                ReglePartie.POIGNEE['simple'], ReglePartie.POIGNEE['double']):
            j.addCarte(Carte("unknown", i, 0.5, 'atout'))

        self.assertEquals(j.annonce(), 'double')

        for i in range(
                ReglePartie.POIGNEE['double'], ReglePartie.POIGNEE['triple']):
            j.addCarte(Carte("unknown", i, 0.5, 'atout'))

        self.assertEquals(j.annonce(), 'triple')

    def testChien(self):

        j = JoueurIA('IA player')

        j.addCarte(Carte('quatre', 4, 0.5, 'atout'))
        j.addCarte(Carte('roi', 14, 4.5, 'trefle'))
        j.addCarte(Carte('roi', 14, 4.5, 'coeur'))
        j.addCarte(Carte('petit', 1, 4.5, 'atout'))
        j.addCarte(Carte('valet', 11, 1.5, 'trefle'))
        j.addCarte(Carte('reine', 13, 3.5, 'trefle'))
        j.addCarte(Carte('reine', 13, 3.5, 'coeur'))
        j.addCarte(Carte('quatre', 4, 0.5, 'trefle'))
        j.addCarte(Carte('quatre', 4, 0.5, 'coeur'))

        self.assertEquals(j.chien(), None)
