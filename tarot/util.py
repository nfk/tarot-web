'''
Project : Tarot Web [https://github.com/nfk/tarot-web]
Author  : nfk
Date    : 29 avr. 2012
'''


def getCartesCouleur(cartes, couleur):
    ''' renvoi la liste des cartes corespondant a la couleur '''
    retCartes = []
    for carte in cartes:
        if carte.couleur == couleur:
            retCartes.append(carte)
    return retCartes
