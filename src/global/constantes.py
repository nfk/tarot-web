'''
Project : Tarot Live [https://launchpad.net/tarot]
Author  : nfk
Date    : 24 oct. 2009
'''

class TypeCarte:
    '''
    definition des types de cartes compose par le jeu de tarot
    '''
    
    # BASIC : dict {nom : indice carte}
    BASIC = {   'as': 1,        'deux': 2,      'trois': 3,
                'quatre': 4,    'cinq': 5,      'six': 6,
                'sept': 7,      'huit': 8,      'neuf': 9,
                'dix': 10,      'valet': 11,    'cavalier': 12,
                'reine': 13,    'roi': 14}
    
    # OUTDLERS : dict {nom : indice carte}
    OUTDLERS = {'petit': 1,   'vingt-et-un': 21, 'excuse':0}
    
    # ATOUT : dict {nom : indice carte}
    ATOUT = {   'deux': 2,      'trois': 3,     'quatre': 4,    'cinq': 5,
                'six': 6,       'sept': 7,      'huit': 8,      'neuf': 9,
                'dix': 10,      'onze': 11,     'douze': 12,    'treize': 13,
                'quatorze': 14, 'quinze': 15,   'seize': 16,    'dix-sept': 17, 
                'dix-huit': 18, 'dix-neuf': 19, 'vingt': 20 }
    for key, value in OUTDLERS.items():
        ATOUT[key] = value

    # COULEUR : dict {nom : indice}
    COULEUR =  {'pique': 0, 'coeur': 1, 'carreau': 2, 'trefle':3}

    # COULEUR + ATOUT : dict {nom : indice}
    COULEUR_ET_ATOUT = COULEUR.copy()
    COULEUR_ET_ATOUT['atout'] = 4

    # NB_CARTES : nombre de carte dans un jeu de tarot
    NB_CARTES = len(BASIC) * len(COULEUR) + len(ATOUT)
    
    # NB_TETES : nombre de tetes du jeu (valet, cavalier, reine, roi)
    NB_TETES = 4 * len(COULEUR)


class ReglePartie:
    '''
    definition des types liees au regles du jeu de tarot
    '''
    
    # ENCHERE : dict {nom : coef}
    ENCHERE = {'passe':0, 'petite': 1, 'garde': 2, 'garde_sans': 4, 
               'garde_contre': 8}

    # POINT_CONTRAT : dict {nb : point a atteindre}
    POINT_CONTRAT = {0:56, 1:51, 2:41, 3:36}
    
    # POIGNEE : dict {nom : nombre d atouts}
    POIGNEE = {'simple': 10, 'double': 13, 'triple': 15}
    
    POINT_POIGNEE = {'simple': 20, 'double': 30, 'triple': 40}
    
    # POINT : dict {nom : valeur des cartes}
    POINT   = {'base': 0.5, 'valet': 1.5, 'cavalier': 2.5, 'reine': 3.5,
               'roi': 4.5, 'outdler': 4.5, 'total': 91}

    # POINT_BONUS :dict {nom : valeur des points en bonus}
    POINT_BONUS = {'petit_au_bout': 10}
    
        