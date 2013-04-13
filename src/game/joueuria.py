'''
Project : Tarot Web [https://github.com/nfk/tarot-web]
Author  : nfk
Date    : 28 dec. 2010
'''
from constantes import ReglePartie, TypeCarte
from util import Util
from statistique import StatsCartes
from joueur import Joueur

class JoueurIA(Joueur):
    '''
    Inteligence artificielle d'un joueur fait pour une partie a 4
    '''

    def __init__(self, ident):
        ''' Constructeur '''
             
        Joueur.__init__(self, ident)
        self.algo = { 'petite'      : 0.4, 
                      'garde'       : 0.65, 
                      'garde_sans'  : 0.85, 
                      'garde_contre': 1 }

        
    def appel(self):
        ''' analyse du jeu et determine le type d'appel '''
            
        s = StatsCartes()
        s.calcul(self.cartes)
        
        points = s.info.pourcentPoints
        objPoints = ReglePartie.POINT_CONTRAT[s.info.nbOutdlers]
        
        limit = (objPoints * 100) / ReglePartie.POINT['total']
         
        # passe
        if points <  limit*self.algo['petite']:
            return 'passe'
        
        # contrat petite
        if points >=  limit*self.algo['petite'] \
            and points < limit*self.algo['garde']:
            return 'petite'
        
        # contrat garde
        if points >=  limit*self.algo['garde'] \
            and points < limit*self.algo['garde_sans']:
            return 'garde'
        
        # contrat garde_sans
        if points >=  limit*self.algo['garde_sans'] \
            and points < limit*self.algo['garde_contre']:
            return 'garde_sans'
        
        # contrat garde_contre
        return 'garde_contre'
 
        
    def chien(self):
        ''' analyse le jeu et joue n cartes au chien '''
        
        # recherche d'une coupe
        
        s = StatsCartes()
        s.calcul(self.cartes)
        
        util = Util()
        
        cartes = {}
        
        for couleur in TypeCarte.COULEUR.iterkeys():
            cartes[couleur] = util.getCartesCouleur(self.cartes, couleur)
            
            
        #for carte in cartes[couleur]:
        #    print carte.info()
        
        
    def annonce(self):
        ''' le joueur peut faire des annonces '''
        s = StatsCartes()
        s.calcul(self.cartes)
        
        if s.info.nbAtouts < ReglePartie.POIGNEE['simple']:
            return None       
        
        if s.info.nbAtouts >= ReglePartie.POIGNEE['simple'] \
            and s.info.nbAtouts < ReglePartie.POIGNEE['double']:
            return 'simple'
       
        if s.info.nbAtouts >= ReglePartie.POIGNEE['double'] \
            and s.info.nbAtouts < ReglePartie.POIGNEE['triple']:
            return 'double'
       
        return 'triple'
    
    def joue(self): 
        pass
    
