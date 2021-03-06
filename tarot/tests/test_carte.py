'''
Project : Tarot Web [https://github.com/nfk/tarot-web]
Author  : nfk
Date    : 25 dec. 2010
'''
import unittest
from tarot.carte import Carte


class TestCarte(unittest.TestCase):

    def testCarte(self):
        carte = Carte('quatre', 4, 0.5, 'atout')
        self.assertTrue(str(carte) == 'quatre(4) atout - point = 0.5')

if __name__ == '__main__':
    unittest.main()
