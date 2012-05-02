'''
Project : Tarot Live [https://launchpad.net/tarot]
Author  : nfk
Date    : 29 avr. 2012
'''

class Util:
    
    
    def getCartesCouleur(self, cartes, couleur):
        ''' renvoi la liste des cartes corespondant a la couleur '''
        
        retCartes = []
        
        for carte in cartes:
            if carte.couleur == couleur:
                retCartes.append(carte)
                
        return retCartes
    
    
    def hasRoi(self, cartes):
        ''' la series de cartes contient un roi '''
        
        for carte in cartes:
            if carte.nom == 'roi':
                return True
        
        return False