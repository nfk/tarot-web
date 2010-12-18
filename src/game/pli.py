'''
Project : Tarot Web [https://launchpad.net/tarot]
Author  : nfk
Date    : 17 dec. 2010
'''

class Pli:
    '''
    gestion des plis
    '''
    def __init__(self):
        self.cartes = [] 
    
    def add(self, carte):
        self.cartes.append(carte)
    
    def controle(self, joueur, carte):
        ''' controle la carte a jouer par le joueur '''
        
        #TODO test excuse sur la premiere carte
        if len(self.cartes) == 0:
            return True
        
        # La reference du controle c est la premiere carte
        first = self.cartes[0]
        
        # La carte est de la meme couleur
        if carte.couleur == first.couleur and carte.couleur != 'atout':
            return True

        # Le joueur joue un atout et n a pas la couleur demandee
        if carte.couleur is 'atout' and joueur.hasCouleur(first.couleur) == False:
            # L atout est superieur
            max = self.__valeurMaxAtouts()
            if carte.valeur > max:
                return True   
            # Le joueur fait pipi
            if carte.valeur < max and joueur.hasAtoutSuperieur(max) == False:
                return True
        
        # Le joueur n a pas la couleur demandee et pas d atout
        if joueur.hasCouleur(first.couleur) == False and joueur.hasCouleur('atout') == False :
            return True
        
        return False
            
    def __valeurMaxAtouts(self):
        ''' recherche la valeur max des atouts presents dans le pli '''
        valeurMax = 0
        for carte in self.cartes:
            if carte.couleur is 'atout' and carte.valeur > valeurMax:
                valeurMax = carte.valeur
        return valeurMax
         
    
    def resultat(self):
        pass