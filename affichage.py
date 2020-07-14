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

x_jouer = WIDTH // 2
y_jouer = HEIGHT // 4

rect = [x_jouer - WIDTH_BOUTON_JOUER // 2, y_jouer - HEIGHT_BOUTON_JOUER // 2, WIDTH_BOUTON_JOUER, HEIGHT_BOUTON_JOUER]
pygame.draw.rect(screen, black, rect, 2)

# Texte bouton jouer

affiche_texte(screen, "Jouer", rect, black, 15)

# Création / placement porte monnaie

x_porte_monnaie = x_jouer
y_porte_monnaie = HEIGHT * 3 / 5

rect_porte_monnaie = [x_porte_monnaie - WIDTH_BOUTON_JOUER, y_porte_monnaie - HEIGHT_BOUTON_JOUER // 2, 2 * WIDTH_BOUTON_JOUER, HEIGHT_BOUTON_JOUER]
pygame.draw.rect(screen, black, rect_porte_monnaie, 2)

texte = "Porte monnaie : {} €".format(str(porte_monaie))
affiche_texte(screen, texte, rect_porte_monnaie, black, 15)

# Gestion porte monnaie (add / remove).

# Bouton ajouer

x_add = 4 * WIDTH // 5
y_add = y_porte_monnaie

rect = [x_add - WIDTH_BOUTON_JOUER // 4, y_add - HEIGHT_BOUTON_JOUER // 2, WIDTH_BOUTON_JOUER // 2, HEIGHT_BOUTON_JOUER]
pygame.draw.rect(screen, black, rect, 2)

affiche_texte(screen, "+", rect, black, 15)

# Bouton remove

x_remove = WIDTH // 5
y_remove = y_porte_monnaie

rect = [x_remove - WIDTH_BOUTON_JOUER // 4, y_remove - HEIGHT_BOUTON_JOUER // 2, WIDTH_BOUTON_JOUER // 2, HEIGHT_BOUTON_JOUER]
pygame.draw.rect(screen, black, rect, 2)

affiche_texte(screen, "-", rect, black, 15)

pygame.display.flip()

# Gestion du clic sur les boutons (porte monnaie).

continuer = True

while continuer:

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                if event.pos[0] >= x_remove - WIDTH_BOUTON_JOUER // 4 and event.pos[0] <= x_remove + WIDTH_BOUTON_JOUER // 4:

                    if event.pos[1] >= y_remove - HEIGHT_BOUTON_JOUER // 2 and event.pos[1] <= y_remove + HEIGHT_BOUTON_JOUER // 2:

                        porte_monaie -= 10

                        pygame.draw.rect(screen, darkgreen, rect_porte_monnaie)
                        pygame.draw.rect(screen, black, rect_porte_monnaie, 2)


                        texte = "Porte monnaie : {} €".format(str(porte_monaie))
                        affiche_texte(screen, texte, rect_porte_monnaie, black, 15)

                elif event.pos[0] >= x_add - WIDTH_BOUTON_JOUER // 4 and event.pos[0] <= x_add + WIDTH_BOUTON_JOUER // 4:

                        if event.pos[1] >= y_add - HEIGHT_BOUTON_JOUER // 2 and event.pos[1] <= y_add + HEIGHT_BOUTON_JOUER // 2:

                            porte_monaie += 10

                            pygame.draw.rect(screen, darkgreen, rect_porte_monnaie)
                            pygame.draw.rect(screen, black, rect_porte_monnaie, 2)


                            texte = "Porte monnaie : {} €".format(str(porte_monaie))
                            affiche_texte(screen, texte, rect_porte_monnaie, black, 15)

                elif event.pos[0] > x_jouer - WIDTH_BOUTON_JOUER // 2 and event.pos[0] < x_jouer + WIDTH_BOUTON_JOUER // 2:

                    if event.pos[1] > y_jouer - HEIGHT_BOUTON_JOUER // 2 and event.pos[1] < y_jouer + HEIGHT_BOUTON_JOUER // 2:

                        screen.fill(darkgreen)

                        continuer = False


# Affichage choix joueur (nombres).

i = 0
y = 0

while y != 5 and i != 10:

    if (i * CASE % 100 == 0 and y * CASE % 100 == 0) or ((i * CASE % 100 != 0 and y * CASE % 100 != 0)):

        rect = [i * CASE, y * CASE, CASE, CASE]
        pygame.draw.rect(screen, red, rect)

        texte = y * 10 + i
        affiche_texte(screen, str(texte), rect, black, 15)

    if (i * CASE % 100 != 0 and y * CASE % 100 == 0) or (i * CASE % 100 == 0 and y * CASE % 100 != 0):

        rect = [i * CASE, y * CASE, CASE, CASE]
        pygame.draw.rect(screen, black, rect)

        texte = y * 10 + i
        affiche_texte(screen, str(texte), rect, red, 15)

    i += 1

    if i * CASE == WIDTH:

        y += 1
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

# Création / placement porte monnaie

x_porte_monnaie = WIDTH // 2
y_porte_monnaie = HEIGHT * 4 / 5

rect_porte_monnaie = [x_porte_monnaie - WIDTH_BOUTON_JOUER, y_porte_monnaie - HEIGHT_BOUTON_JOUER // 2, 2 * WIDTH_BOUTON_JOUER, HEIGHT_BOUTON_JOUER]
pygame.draw.rect(screen, black, rect_porte_monnaie, 2)

affiche_texte(screen, str(porte_monaie), rect_porte_monnaie, black, 15)

# Gestion porte monnaie (add / remove).

# Bouton ajouer

x_add = 4 * WIDTH // 5
y_add = y_porte_monnaie

rect = [x_add - WIDTH_BOUTON_JOUER // 4, y_add - HEIGHT_BOUTON_JOUER // 2, WIDTH_BOUTON_JOUER // 2, HEIGHT_BOUTON_JOUER]
pygame.draw.rect(screen, black, rect, 2)

affiche_texte(screen, "+", rect, black, 15)

# Bouton remove

x_remove = WIDTH // 5
y_remove = y_porte_monnaie

rect = [x_remove - WIDTH_BOUTON_JOUER // 4, y_remove - HEIGHT_BOUTON_JOUER // 2, WIDTH_BOUTON_JOUER // 2, HEIGHT_BOUTON_JOUER]
pygame.draw.rect(screen, black, rect, 2)

affiche_texte(screen, "-", rect, black, 15)

pygame.display.flip()

# Gestion clic.

continuer = True

while continuer:

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

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

rect = [WIDTH // 4 - WIDTH_BOUTON_JOUER // 2, HEIGHT // 4 - HEIGHT_BOUTON_JOUER // 2, WIDTH_BOUTON_JOUER, HEIGHT_BOUTON_JOUER]
pygame.draw.rect(screen, black, rect, 1)

if choixjoueur == "Pair" or est_pair(choixjoueur):

    pygame.draw.rect(screen, black, rect)
    affiche_texte(screen, str(choixjoueur), rect, red, 15)

elif choixjoueur == "Impair" or est_impair(choixjoueur):

    pygame.draw.rect(screen, red, rect)
    affiche_texte(screen, str(choixjoueur), rect, black, 15)

# Affichage du choix aleatoire.

rect = [WIDTH * 3 // 4 - WIDTH_BOUTON_JOUER // 2, HEIGHT // 4 - HEIGHT_BOUTON_JOUER // 2, WIDTH_BOUTON_JOUER, HEIGHT_BOUTON_JOUER]
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
        