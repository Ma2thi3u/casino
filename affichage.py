# coding:utf-8

import pygame

from fonction_globales import *

from variables_globales import *

from couleurs import *

# Initialisation du module pygame.

pygame.init()

# Création de la fenetre.

screen = pygame.display.set_mode((SIZE))

# Titre de la fenetre.

pygame.display.set_caption("Casino")

# Changement de la couleur de fond de la fenetre.

screen.fill(darkgreen)

# Création / placement du bouton jouer.

x_bouton_jouer = WIDTH // 2
y_bouton_jouer = HEIGHT // 4

creer_bouton(screen, x_bouton_jouer, y_bouton_jouer, WIDTH_BOUTON, HEIGHT_BOUTON, black, black, "Jouer")

# Création / placement porte monnaie

x_bouton_porte_monnaie = x_bouton_jouer
y_bouton_porte_monnaie = HEIGHT * 3 / 5

texte = "Porte monnaie : {} €".format(str(porte_monaie))

creer_bouton(screen, x_bouton_porte_monnaie, y_bouton_porte_monnaie, WIDTH_BOUTON * 2, HEIGHT_BOUTON, black, black, texte)

# Gestion porte monnaie (add / remove).

# Bouton ajouer

x_bouton_add = 4 * WIDTH // 5
y_bouton_add = y_bouton_porte_monnaie

creer_bouton(screen, x_bouton_add, y_bouton_add, WIDTH_BOUTON // 2, HEIGHT_BOUTON, black, black, "+")

# Bouton remove

x_bouton_remove = WIDTH // 5
y_bouton_remove = y_bouton_porte_monnaie

creer_bouton(screen, x_bouton_remove, y_bouton_remove, WIDTH_BOUTON // 2, HEIGHT_BOUTON, black, black, "-")

# Gestion du clic sur les boutons (porte monnaie).

continuer = True

while continuer:

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                if event.pos[0] >= x_bouton_remove - WIDTH_BOUTON // 4 and event.pos[0] <= x_bouton_remove + WIDTH_BOUTON // 4:

                    if event.pos[1] >= y_bouton_remove - HEIGHT_BOUTON // 2 and event.pos[1] <= y_bouton_remove + HEIGHT_BOUTON // 2:

                        if porte_monaie <= 0:

                            pass

                        else:

                            porte_monaie -= 10

                        texte = "Porte monnaie : {} €".format(str(porte_monaie))
                        creer_bouton(screen, x_bouton_porte_monnaie, y_bouton_porte_monnaie, WIDTH_BOUTON * 2, HEIGHT_BOUTON, black, black, texte)

                elif event.pos[0] >= x_bouton_add - WIDTH_BOUTON // 4 and event.pos[0] <= x_bouton_add + WIDTH_BOUTON // 4:

                        if event.pos[1] >= y_bouton_add - HEIGHT_BOUTON // 2 and event.pos[1] <= y_bouton_add + HEIGHT_BOUTON // 2:

                            porte_monaie += 10

                            texte = "Porte monnaie : {} €".format(str(porte_monaie))
                            creer_bouton(screen, x_bouton_porte_monnaie, y_bouton_porte_monnaie, WIDTH_BOUTON * 2, HEIGHT_BOUTON, black, black, texte)

                elif event.pos[0] > x_bouton_jouer - WIDTH_BOUTON // 2 and event.pos[0] < x_bouton_jouer + WIDTH_BOUTON // 2:

                    if event.pos[1] > y_bouton_jouer - HEIGHT_BOUTON // 2 and event.pos[1] < y_bouton_jouer + HEIGHT_BOUTON // 2:

                        if porte_monaie > 0:

                            screen.fill(darkgreen)

                            continuer = False

# Affichage choix joueur (nombres).

i = 0
j = 0

while j != 5 and i != 10:

    if (i * CASE % 100 == 0 and j * CASE % 100 == 0) or ((i * CASE % 100 != 0 and j * CASE % 100 != 0)):

        rect = [i * CASE, j * CASE, CASE, CASE]
        pygame.draw.rect(screen, black, rect)

        texte = j * 10 + i
        affiche_texte(screen, str(texte), rect, red, 15)

    if (i * CASE % 100 != 0 and j * CASE % 100 == 0) or (i * CASE % 100 == 0 and j * CASE % 100 != 0):

        rect = [i * CASE, j * CASE, CASE, CASE]
        pygame.draw.rect(screen, red, rect)

        texte = j * 10 + i
        affiche_texte(screen, str(texte), rect, black, 15)

    i += 1

    if i * CASE == WIDTH:

        j += 1
        i = 0

# Affichage choix joueur (pair / impair).

# Pair

rect = [0, HEIGHT // 2, WIDTH // 2, CASE]
pygame.draw.rect(screen, black, rect)

affiche_texte(screen, "Pair", rect, red, 15)

# Impair

rect = [WIDTH // 2, HEIGHT // 2, WIDTH // 2, CASE]
pygame.draw.rect(screen, red, rect)

affiche_texte(screen, "Impair", rect, black, 15)

pygame.display.flip()

# Gestion de la mise

mise = porte_monaie

# Création / placement porte monnaie

x_bouton_mise = WIDTH // 2
y_bouton_mise = HEIGHT * 4 / 5

creer_bouton(screen, x_bouton_mise, y_bouton_mise, WIDTH_BOUTON * 2, HEIGHT_BOUTON, black, black, str(mise))

# Gestion porte monnaie (add / remove).

# Bouton ajouer

x_bouton_add = 4 * WIDTH // 5
y_bouton_add = y_bouton_mise

creer_bouton(screen, x_bouton_add, y_bouton_add, WIDTH_BOUTON // 2, HEIGHT_BOUTON, black, black, "+")

# Bouton remove

x_bouton_remove = WIDTH // 5
y_bouton_remove = y_bouton_mise

creer_bouton(screen, x_bouton_remove, y_bouton_remove, WIDTH_BOUTON // 2, HEIGHT_BOUTON, black, black, "-")

pygame.display.flip()

continuer = True

while continuer:

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                if event.pos[0] >= x_bouton_remove - WIDTH_BOUTON // 4 and event.pos[0] <= x_bouton_remove + WIDTH_BOUTON // 4:

                    if event.pos[1] >= y_bouton_remove - HEIGHT_BOUTON // 2 and event.pos[1] <= y_bouton_remove + HEIGHT_BOUTON // 2:

                        if mise <= 0:

                            pass

                        else:

                            mise -= 10

                        creer_bouton(screen, x_bouton_mise, y_bouton_mise, WIDTH_BOUTON * 2, HEIGHT_BOUTON, black, black, str(mise))

                elif event.pos[0] >= x_bouton_add - WIDTH_BOUTON // 4 and event.pos[0] <= x_bouton_add + WIDTH_BOUTON // 4:

                    if event.pos[1] >= y_bouton_add - HEIGHT_BOUTON // 2 and event.pos[1] <= y_bouton_add + HEIGHT_BOUTON // 2:

                        if mise >= porte_monaie:

                            pass

                        else:

                            mise += 10

                        creer_bouton(screen, x_bouton_mise, y_bouton_mise, WIDTH_BOUTON * 2, HEIGHT_BOUTON, black, black, str(mise))

                x = event.pos[0] // 50
                y = event.pos[1] // 50

                choixjoueur = y * 10 + x

                if choixjoueur >= 60:

                    continue

                if choixjoueur >= 50 and choixjoueur <= 54:

                    choixjoueur = "Pair"

                elif choixjoueur >= 55 and choixjoueur <= 59:

                    choixjoueur = "Impair"

                screen.fill(darkgreen)

                continuer = False

# Affichage du choix du joueur.

x_choix_joueur = WIDTH // 4
y_choix_joueur = HEIGHT // 4

if choixjoueur == "Pair":

    choixjoueur = 50

elif choixjoueur == "Impair":

    choixjoueur = 51


if est_pair(choixjoueur) and choixjoueur < 50:

    creer_bouton(screen, x_choix_joueur, y_choix_joueur, WIDTH_BOUTON, HEIGHT_BOUTON, red, black, str(choixjoueur), 0)

elif est_impair(choixjoueur) and choixjoueur < 50:

    creer_bouton(screen, x_choix_joueur, y_choix_joueur, WIDTH_BOUTON, HEIGHT_BOUTON, black, red, str(choixjoueur), 0)

elif choixjoueur == 50:

    creer_bouton(screen, x_choix_joueur, y_choix_joueur, WIDTH_BOUTON, HEIGHT_BOUTON, red, black, "Pair", 0)

elif choixjoueur == 51:

    creer_bouton(screen, x_choix_joueur, y_choix_joueur, WIDTH_BOUTON, HEIGHT_BOUTON, black, red, "Impair", 0)



# Affichage du choix aleatoire.

rect = [WIDTH * 3 // 4 - WIDTH_BOUTON // 2, HEIGHT // 4 - HEIGHT_BOUTON // 2, WIDTH_BOUTON, HEIGHT_BOUTON]
pygame.draw.rect(screen, black, rect, 1)

choix_aleatoire = int(choix_aleatoire())

if est_pair(choix_aleatoire):

    pygame.draw.rect(screen, black, rect)       
    affiche_texte(screen, str(choix_aleatoire), rect, red, 15)

else:

    pygame.draw.rect(screen, red, rect)       
    affiche_texte(screen, str(choix_aleatoire), rect, black, 15)

# Actualisation de la fenetre.

pygame.display.flip()

# Attente de la fermeture de la fenetre

wait_escape()
        