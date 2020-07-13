# coding:utf-8

import pygame

from fonction_globales import *

from variables_globales import *

from couleurs import *

# Initialisation du module pygame.

pygame.init()

# Création de la fenetre

screen = pygame.display.set_mode((SIZE))

# Changement de la couleur de fond de la fenetre.

screen.fill(darkgreen)

# Création / placement du bouton jouer.

rect = [WIDTH//2-(WIDTH_BOUTON_JOUER//2), HEIGHT//2-(HEIGHT_BOUTON_JOUER//2), WIDTH_BOUTON_JOUER, HEIGHT_BOUTON_JOUER]
pygame.draw.rect(screen, black, rect, 1)

# Texte bouton jouer

affiche_texte(screen, "Jouer", rect, black, 15)

# gestion du clic sur le bouton.

while continuer:

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                if event.pos[0] > WIDTH // 2 - WIDTH_BOUTON_JOUER // 2 and event.pos[0] < WIDTH // 2 + WIDTH_BOUTON_JOUER // 2:

                    if event.pos[1] > HEIGHT // 2 - HEIGHT_BOUTON_JOUER // 2 and event.pos[1] < HEIGHT // 2 + HEIGHT_BOUTON_JOUER // 2:

                        screen.fill(darkgreen)

                        continuer = False

# Affichage choix joueur.



i = 0
y = 0

while y != 5 and i != 10:

    if (i * CASE % 100 == 0 and y * CASE % 100 == 0) or ((i * CASE % 100 != 0 and y * CASE % 100 != 0)):

        rect = [i * CASE, y * CASE, CASE, CASE]
        pygame.draw.rect(screen, black, rect)

        texte = y * 10 + i
        affiche_texte(screen, str(texte), rect, red, 15)

    if (i * CASE % 100 != 0 and y * CASE % 100 == 0) or (i * CASE % 100 == 0 and y * CASE % 100 != 0):

        rect = [i * CASE, y * CASE, CASE, CASE]
        pygame.draw.rect(screen, red, rect)

        texte = y * 10 + i
        affiche_texte(screen, str(texte), rect, black, 15)

    i += 1

    if i * CASE == WIDTH:

        y += 1
        i = 0

continuer = True

while continuer:

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                x = event.pos[0] // 50
                y = event.pos[1] // 50

                choixjoueur = y * 10 + x

                screen.fill(darkgreen)

                continuer = False

# Affichage du choix du joueur.

rect = [WIDTH // 4 - WIDTH_BOUTON_JOUER // 2, HEIGHT // 4 - HEIGHT_BOUTON_JOUER // 2, WIDTH_BOUTON_JOUER, HEIGHT_BOUTON_JOUER]
pygame.draw.rect(screen, black, rect, 1)

if est_pair(choixjoueur):

    pygame.draw.rect(screen, black, rect)
    affiche_texte(screen, str(choixjoueur), rect, red, 15)

else:

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
        