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