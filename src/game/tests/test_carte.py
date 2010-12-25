'''
Project : Tarot Web [https://launchpad.net/tarot]
Author  : nfk
Date    : 25 dec. 2010
'''
import unittest
from carte import Carte

class Test(unittest.TestCase):

    def testCarte(self):
        carte = Carte('quatre', 4, 0.5, 'atout')
        self.assertEquals(carte.info(), "quatre(4) atout - valeur=0.5")