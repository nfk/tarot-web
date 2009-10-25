'''
Project : Tarot Web [https://launchpad.net/tarot]
Author  : nfk
Date    : 25 oct. 2009
'''

import unittest
import os
import sys

dirname = os.path.dirname(__file__)
if dirname == '':
    dirname = '.'
dirname = os.path.realpath(dirname)

updir = os.path.split(dirname)[0]
if updir not in sys.path:
    sys.path.append(updir)

from constantes import TypeCarte
from cartes import Cartes

class ListeCartesJeuTarot(unittest.TestCase):
    '''
    test le jeu de carte
    '''

    def testCartes(self):
        c = Cartes()
        print ""
        for carte in c.getCartes():
            print carte.info()
            
        self.assertEquals(c.getCartes().__len__(), TypeCarte.NB_CARTES)
        
    
        