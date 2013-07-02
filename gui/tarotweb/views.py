from django.shortcuts import render
from tarot.partie import Partie4Joueurs
from tarot.joueuria import JoueurIA
from tarot.joueur import Joueur


def party(request):
    party = Partie4Joueurs()

    for i in range(3):
        party.addJoueur(JoueurIA("ia-" + str(i + 1)))

    player = Joueur('player one')
    party.addJoueur(player)
    party.distribution()

    return render(request, 'game.html', {'party': party, 'player': player})
