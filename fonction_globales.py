# coding:utf-8

import random

import pygame


def est_pair(nb):

    if nb % 2 == 0:

        return True

    else:

        return False

def est_impair(nb):

    if nb % 2 != 0:

        return True

    else:

        return False

def rejouer():

    valide = False

    while valide == False:

        rejouer = input("Voulez vous continuer à jouer ? (Y/N) : ")

        if rejouer.upper() == "Y":

            valide = True
            continuer = True

        elif rejouer.upper() == "N":

            valide = True
            continuer = False

        else:

            continue

    return continuer

def wait_escape():
    encore = 1
    while encore == 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    encore = 0
            if event.type == pygame.QUIT:
                encore = 0

def affiche_texte(screen, texte, rect, couleur_texte, size):   
  
    # Initialisation de la fonte
    pygame.font.init()
    font = pygame.font.SysFont("verdana", size, bold=False, italic=False)
  
    # Coordonnées du centre    
    centre = [rect[0]+rect[2]//2, rect[1]+rect[3]//2]
  
    # création de la surface contenant le texte
    text_area = font.render(texte, 1, couleur_texte)
  
    # taille de la surface contenant le texte
    text_size = font.size(texte)
    
    # position d'ancrage du coin en haut à gauche de la surface contenant le texte
    text_pos = [centre[0]-text_size[0]//2, centre[1]-text_size[1]//2]
   
    # ancrage de la surface contenant le texte dans la fenêtre
    screen.blit(text_area, text_pos)
    pygame.display.flip()  
   
    # desinitialisation de la fonte
    pygame.font.quit()