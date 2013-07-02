'''
Project : Tarot Web [https://github.com/nfk/tarot-web]
Author  : nfk
Date    : 29 avr. 2012
'''


def getCartesCouleur(cartes, color):
    ''' renvoi la liste des cartes corespondant a la couleur '''
    retCartes = []
    for carte in cartes:
        if carte.color == color:
            retCartes.append(carte)
    return retCartes
