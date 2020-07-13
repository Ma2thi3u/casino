# coding:utf-8

import pygame

from fonction_globales import *

from variables_globales import *

from casino import *

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

rect = [WIDTH // 4 - (WIDTH_BOUTON_JOUER//2), HEIGHT // 4 - (HEIGHT_BOUTON_JOUER//2), WIDTH_BOUTON_JOUER, HEIGHT_BOUTON_JOUER]
pygame.draw.rect(screen, black, rect, 1)

# Affichage choix aleatoire.

rect = [WIDTH * 3 // 4 - (WIDTH_BOUTON_JOUER//2), HEIGHT // 4 - (HEIGHT_BOUTON_JOUER//2), WIDTH_BOUTON_JOUER, HEIGHT_BOUTON_JOUER]
pygame.draw.rect(screen, black, rect, 1)

affiche_texte(screen, choix_aleatoire(), rect, black, 15)

# Actualisation de la fenetre.

pygame.display.flip()

# Attente de la fermeture de la fenetre

wait_escape()
            