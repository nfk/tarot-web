'''
Project : Tarot Web [https://github.com/nfk/tarot-web]
Author  : nfk
Date    : 25 oct. 2009
'''

class MaxJoueursAtteint(Exception):
    pass
class ManqueJoueurs(Exception):
    pass

class PliComplet(Exception):
    pass
class PliIncomplet(Exception):
    pass
class PliJoueurADejaJoue(Exception):
    pass
class PliCarteDejaJouee(Exception):
    pass
