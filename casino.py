# coding:utf-8

# Importation du module random.
import random

# Importation du module contenant les variables globales.
from variables_globales import *

# Importation du module contenant les fonctions globales.
from fonction_globales import *


# Définition de la fonction jouer (fonction principale).

def jouer():

    global porte_monaie

    # Affichage du contenu du porte monaie.

    print("Vous avez en votre possesion : {} $.".format(porte_monaie))


    # Le joueur doit miser une somme (int) inférieure ou égale a celle qu'il possède.

    valide = False

    while valide == False:

        try:

            mise = int(input("MISE : "))

            if mise > 0 and mise <= porte_monaie:

                valide = True

            else:

                continue

        except:

            continue

    # On retire la mise au porte monaie

    porte_monaie -= mise

    # On fait tourner la roulette

    roulette = random.randint(mini, maxi)

    # Le joueur choisi un nombre (int) compris entre 0 (mini) et 49 (maxi).

    valide = False

    while valide == False:

        try:

            choix_joueur = int(input("Choisissez un nombre entre {} et {} inclus : ".format(str(mini), str(maxi))))

            if choix_joueur >= mini and choix_joueur <= maxi:

                valide = True

            else:

                    continue

        except:

            continue

    if choix_joueur == roulette:

        print("Vous gagnez 5 fois votre mise")
        porte_monaie += mise * 5

    elif est_pair(choix_joueur) and est_pair(roulette):

        print("Vous gagnez 2 fois votre mise")
        porte_monaie += mise * 2

    elif est_impair(choix_joueur) and est_impair(roulette):

        print("Vous gagnez 2 fois votre mise")
        porte_monaie += mise * 2

    else:

        print("Vous perdez votre mise :(")


if __name__ == "__main__":

    while porte_monaie > 0:

        jouer()

        if porte_monaie > 0:

            if rejouer():

                continue

            else:

                break