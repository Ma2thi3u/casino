# coding:utf-8

import pygame

from variables_globales import *

from couleurs import *

from fonction_globales import *

# Initialisation du module pygame.

pygame.init()

# Création de la fenetre.

screen = pygame.display.set_mode((HEIGHT, WIDTH))

# Changement de la couleur de fond de la fenetre.

screen.fill(darkgreen)

# Actualisation de la fenetre.

pygame.display.flip()

# Attente de la fermeture de la fenetre.

wait_escape()