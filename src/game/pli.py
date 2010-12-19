'''
Project : Tarot Web [https://launchpad.net/tarot]
Author  : nfk
Date    : 17 dec. 2010
'''
import erreur
from collections import namedtuple

class Pli:
    '''
    gestion des plis pour 4 joueurs
    '''
    def __init__(self):
        self.pli = []
        self.Couple = namedtuple('Couple', 'carte joueur')
        self.nb_joueurs = 4
        
        self.point = 0
        self.winner = None
    
    def add(self, carte, joueur):
        ''' ajout d une carte au pli '''
        
        if len(self.pli) == self.nb_joueurs:
            raise erreur.PliComplet()
        
        if len(self.pli) > 0:
            for p in self.pli:
                if p.carte == carte:
                    raise erreur.PliCarteDejaJouee
                if p.joueur == joueur:
                    raise erreur.PliJoueurADejaJoue 

        self.pli.append(self.Couple(carte, joueur))
    
    def controle(self, carte, joueur):
        ''' controle la carte a jouer par le joueur '''

        first = self.__firstCarte()
        
        # la premiere carte on joue ce qu on veux
        if first is None:
            return True
        
        # La carte est de la meme couleur
        if carte.couleur == first.couleur and carte.couleur != 'atout':
            return True

        # Le joueur joue un atout et n a pas la couleur demandee
        if carte.couleur is 'atout'\
                                and joueur.hasCouleur(first.couleur) == False:
            # L atout est superieur
            max = self.__valeurMaxAtouts()
            if carte.valeur > max:
                return True   
            # Le joueur fait pipi
            if carte.valeur < max and joueur.hasAtoutSuperieur(max) == False:
                return True
        
        # Le joueur n a pas la couleur demandee et pas d atout
        if joueur.hasCouleur(first.couleur) == False\
                                    and joueur.hasCouleur('atout') == False :
            return True
        
        return False
            
    def __firstCarte(self):
        ''' retourne la carte d ouverture du pli'''
        
        if len(self.pli) == 0:
            return None
        
        # La reference du controle c est la premiere carte 
        # sauf si c est l excuse
        if self.pli[0].carte.nom == 'excuse':
            if len(self.pli) >= 2:
                return self.pli[1].carte
        else:
            if len(self.pli) >= 1:
                return self.pli[0].carte
            
        return None
    
    def __valeurMaxAtouts(self):
        ''' recherche la valeur max des atouts presents dans le pli '''
        valeurMax = 0
        for p in self.pli:
            if p.carte.couleur is 'atout' and p.carte.valeur > valeurMax:
                valeurMax = p.carte.valeur
                
        return valeurMax
         
    
    def resultat(self):
        ''' recherche le vainqueur du pli et calcul le nombre de points '''
        if len(self.pli) < self.nb_joueurs:
            raise erreur.PliIncomplet()
        
        current = self.__firstCarte()
        
        # recherche la carte gagnante
        for p in self.pli[1:self.nb_joueurs]:
            # carte joue ne correspond a rien
            if p.carte.couleur != current.couleur and p.carte.couleur !='atout':
                continue
            
            # la carte a ete coupee
            if p.carte.couleur != current.couleur:
                current = p.carte
                continue
            
            # la carte est de la meme couleur on compare la valeur
            if p.carte.valeur > current.valeur:
                current = p.carte
                continue
        
        # recherhe le joueur gagnant et calcul du score
        for p in self.pli:
            if p.carte == current:
                self.winner = p.joueur
                
            self.point = self.point + p.carte.point
        
        