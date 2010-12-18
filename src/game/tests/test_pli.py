'''
Project : Tarot Web [https://launchpad.net/tarot]
Author  : nfk
Date    : 17 dec. 2010
'''
import unittest
from joueur import Joueur
from pli import Pli
from carte import Carte

class Test(unittest.TestCase):

    def testPliControle(self):
        joueur = Joueur('joueur1')
        pli = Pli()
        
        joueur.setCarte(Carte('quatre', 4, 0.5, 'atout'))
        joueur.setCarte(Carte('quatorze', 14, 0.5, 'atout'))
        joueur.setCarte(Carte('quatre', 4, 0.5, 'pique'))
        joueur.setCarte(Carte('six', 6, 0.5, 'pique'))
        joueur.setCarte(Carte('roi', 14, 4.5, 'pique'))
        joueur.setCarte(Carte('roi', 14, 4.5, 'coeur'))
        joueur.setCarte(Carte('reine', 13, 3.5, 'coeur'))
        joueur.setCarte(Carte('as', 1, 0.5, 'coeur'))

        # je joue la premiere carte
        carteAjouer = joueur.getCartes()[0]
        self.assertEquals(pli.controle(joueur, carteAjouer), True)
        
        # je joue comme premiere carte l excuse
        carteAjouer = Carte('excuse', 0, 4.5, 'atout')
        self.assertEquals(pli.controle(joueur, carteAjouer), True)
        pli.add(carteAjouer)

        # La premiere carte est l excuse le second joueur joue un AS de trefle
        carteAjouer = Carte('as', 1, 0.5, 'trefle')
        self.assertEquals(pli.controle(joueur, carteAjouer), True)
        pli.add(carteAjouer)

        # Le joueur coupe car il n a pas de trefle
        carteAjouer = joueur.getCartes()[0]
        self.assertEquals(pli.controle(joueur, carteAjouer), True)
        
        # Le joueur fait pipi a l atout
        pli.add(Carte('vingt', 20, 0.5, 'atout'))
        self.assertEquals(pli.controle(joueur, carteAjouer), True)
        
        # Le joueur triche car il a un atout superieur
        joueur.setCarte(Carte('vingt-et-un', 21, 4.5, 'atout'))
        self.assertEquals(pli.controle(joueur, carteAjouer), False)
        
        # Le joueur joue autre chose qu atout alors qu il na pas de trefle
        carteAjouer = joueur.getCartes()[4]
        self.assertEquals(pli.controle(joueur, carteAjouer), False)
        
        
        

if __name__ == "__main__":
    unittest.main()
    