'''
Project : Tarot Live [https://launchpad.net/tarot]
Author  : nfk
Date    : 25 dec. 2010
'''
import unittest
from carte import Carte

class TestCarte(unittest.TestCase):

    def testCarte(self):
        carte = Carte('quatre', 4, 0.5, 'atout')
        self.assertEquals(carte.info(), "quatre(4) atout - point=0.5")

    def testName(self):
        carte = Carte('quatre', 4, 0.5, 'atout')
        self.assertEquals(carte.name(), "quatre_atout")