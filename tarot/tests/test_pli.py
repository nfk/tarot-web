'''
Project : Tarot Web [https://github.com/nfk/tarot-web]
Author  : nfk
Date    : 17 dec. 2010
'''
import unittest
import erreur
from joueur import Joueur
from pli import Pli
from carte import Carte


class TestPli(unittest.TestCase):

    def testPliAdd(self):
        joueur1 = Joueur('joueur1')
        joueur2 = Joueur('joueur2')
        joueur3 = Joueur('joueur3')
        joueur4 = Joueur('joueur4')
        joueur5 = Joueur('joueur5')
        pli = Pli()

        carte = Carte('quatre', 4, 0.5, 'atout')
        self.assertEquals(pli.add(carte, joueur1), None)
        self.assertRaises(erreur.PliCarteDejaJouee, pli.add, carte, joueur2)
        self.assertEquals(pli.add(Carte('cinq', 5, 0.5, 'atout'), joueur2),
                          None)
        self.assertEquals(pli.add(Carte('quatre', 4, 0.5, 'pique'), joueur3),
                          None)
        self.assertRaises(erreur.PliJoueurADejaJoue, pli.add,
                          Carte('quatre', 4, 0.5, 'pique'), joueur3)
        self.assertEquals(pli.add(Carte('roi', 14, 4.5, 'coeur'), joueur4),
                          None)
        self.assertRaises(erreur.PliComplet, pli.add,
                          Carte('reine', 13, 3.5, 'coeur'), joueur5)

    def testPliControle(self):
        joueur1 = Joueur('joueur1')
        joueur2 = Joueur('joueur2')
        joueur3 = Joueur('joueur3')

        pli = Pli()

        joueur1.addCarte(Carte('quatre', 4, 0.5, 'atout'))
        joueur1.addCarte(Carte('quatorze', 14, 0.5, 'atout'))
        joueur1.addCarte(Carte('quatre', 4, 0.5, 'pique'))
        joueur1.addCarte(Carte('six', 6, 0.5, 'pique'))
        joueur1.addCarte(Carte('roi', 14, 4.5, 'pique'))
        joueur1.addCarte(Carte('roi', 14, 4.5, 'coeur'))
        joueur1.addCarte(Carte('reine', 13, 3.5, 'coeur'))
        joueur1.addCarte(Carte('as', 1, 0.5, 'coeur'))

        # je joue la premiere carte
        carteAjouer = joueur1.cartes[0]
        self.assertEquals(pli.controle(carteAjouer, joueur1), True)

        # je joue comme premiere carte l excuse
        carteAjouer = Carte('excuse', 0, 4.5, 'atout')
        self.assertEquals(pli.controle(carteAjouer, joueur1), True)
        pli.add(carteAjouer, joueur1)

        # La premiere carte est l excuse le second joueur1 joue un AS de trefle
        carteAjouer = Carte('as', 1, 0.5, 'trefle')
        self.assertEquals(pli.controle(carteAjouer, joueur1), True)
        pli.add(carteAjouer, joueur2)

        # Le joueur joue un roi de trefle
        self.assertEquals(pli.controle(Carte('roi', 14, 4.5, 'trefle'),
                                       joueur1), True)

        # Le joueur coupe car il n a pas de trefle
        carteAjouer = joueur1.cartes[0]
        self.assertEquals(pli.controle(carteAjouer, joueur1), True)

        # Le joueur1 fait pipi a l atout
        pli.add(Carte('vingt', 20, 0.5, 'atout'), joueur3)
        self.assertEquals(pli.controle(carteAjouer, joueur1), True)

        # Le joueur1 triche car il a un atout superieur
        joueur1.addCarte(Carte('vingt-et-un', 21, 4.5, 'atout'))
        self.assertEquals(pli.controle(carteAjouer, joueur1), False)

        # Le joueur1 joue autre chose qu atout alors qu il na pas de trefle
        carteAjouer = joueur1.cartes[4]
        self.assertEquals(pli.controle(carteAjouer, joueur1), False)

        # Le joueur n a pas la couleur demandee et pas d atout
        joueur1.joueCarte(0)
        joueur1.joueCarte(0)
        joueur1.joueCarte(6)

        carteAjouer = joueur1.cartes[0]  # quatre de pique
        self.assertEquals(pli.controle(carteAjouer, joueur1), True)

    def testPliResultat(self):
        joueur1 = Joueur('joueur1')
        joueur2 = Joueur('joueur2')
        joueur3 = Joueur('joueur3')
        joueur4 = Joueur('joueur4')

        pli = Pli()
        pli.add(Carte('sept', 7, 0.5, 'coeur'), joueur1)
        pli.add(Carte('roi', 14, 4.5, 'coeur'), joueur2)
        pli.add(Carte('quatorze', 14, 0.5, 'atout'), joueur3)

        self.assertRaises(erreur.PliIncomplet, pli.resultat)

        pli.add(Carte('dame', 13, 3.5, 'coeur'), joueur4)

        pli.resultat()
        self.assertEquals(pli.point, 4.5 + 0.5 + 0.5 + 3.5)
        self.assertEquals(pli.winner, joueur3)

if __name__ == '__main__':
    unittest.main()
