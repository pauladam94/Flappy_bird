
# coding: utf8

"""
cd Documents\Perso\Python\Flappy_bird
fonction pour le programme
flappy bird
"""

import pygame as py
import math
from random import randint

py.init()

# initialisation des abscisses et ordonnées
#def des couleurs
NOIR      = (0,0,0)
BLANC     = (255,255,255)
ROUGE     = (255,0,0)
ROSE      = (255, 20, 147)
ORANGE    = (255, 69, 0)
JAUNE     = (255,255,0)
VIOLET    = (128, 0, 128)
VERT      = (84,173,65)
VERT_FLASHI = (0, 255, 255) 
NAVY      = (0, 0, 128)
MARRON    = (165, 42, 42)
BLEU      = (0,0,255)
GRIS      = (122, 145, 145)
TURQUOISE = (50, 255, 255)


# separation en ordonnée entre les tubes haut et bas
separt = 150

# largueur des tubes ( en abscisse )
largueur = 76 

#distance en abscisse entre les tubes 
distance = 300

# espacement entre les nuages
nuage_es = 820

arial_30 = py.font.SysFont("arial", 30)

### def de fonction
#   Vy = 6 * t - 4
def fy(t,Y0) :
    return(round(6*t**2-4*t+Y0))

def tirage():
    return(randint(4,24)*13)

def fin_loose(window, score):
    dimension_text = arial_30.render("{}".format(" Vous avez perdu !! ; - ) "), True, NOIR)
    window.blit(dimension_text, [150,200] )
    py.display.flip()
    py.time.delay(2000)

def score_update(window,score):
    score = arial_30.render("Score : " + str(score), False, BLEU)
    window.blit(score, [400, 100])

def dessin_tube(window,list,incr,image1,image2):
    for i in range(len(list)):
        list[i][0] -= incr
        window.blit(image1, [list[i][0], list[i][1]-300] )
        window.blit(image2, [list[i][0], list[i][1]+separt] )
    return(list)