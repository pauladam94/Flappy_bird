# coding: utf8
## programme d'affichage de trajectoire d'une balle

"""
cd Documents\Perso\Python\Flappy_bird
"""

# importation module
import pygame as py
import module_fb as mod
import math
from time import sleep
from random import randint

py.init()

# def de la fenetre :
fenetre = py.display.set_mode((600,500), py.DOUBLEBUF | py.HWSURFACE | py.RESIZABLE)
py.display.set_caption("Snake GAME P.A.")
fenetre.fill((0,0,0))
py.display.flip()

# importation des sons
vent = py.mixer.Sound("vent.ogg")
aile = py.mixer.Sound("aile.ogg")
point = py.mixer.Sound("point.ogg")

# importation des images
oiseau = py.image.load("canard2.png")
oiseau.convert()

nuage = py.image.load("fond.png")
nuage.convert()

tube_haut = py.image.load("tube.png")
tube_haut.convert()

tube_bas = py.transform.rotate(tube_haut,180)
tube_bas.convert()

###  Def Var  :
# position initial de l'objet
# en pixel
Xb = 200
Yb = 200

# tube
Xtu = -100
Max = 100

nb_tube = 6

# les C_tube[i][0] sont les abscisses (en haut à gauche) des tubes
# les c_tube[i][1] sont les ordonnées des coins en haut à gauche des trous
# entre les tubes 
C_tube =[ [Xtu,Max] ]
for i in range(nb_tube) :
    if i ==0 :
        C_tube.append([C_tube[i][0]+mod.distance+200,mod.tirage()]) 
    else :    
        C_tube.append([C_tube[i][0]+mod.distance,mod.tirage()])
# temps initial
t=0

# init t_chute
t_chute = 0

# incrément 
saut = 15
score=0
increment = 0.01
#increment = 0.05
compteur = 0
incr= 2

# position du nuage
Xn,Yn = -70,-70
X_nuage = [Xn,Xn+mod.nuage_es,Xn+1700]

# premier dessin st
fenetre.fill(mod.NOIR)
fenetre.blit(nuage,[-70,-70])
fenetre.blit(oiseau,[Xb,Yb])
C_tube = mod.dessin_tube(fenetre, C_tube, incr,tube_haut,tube_bas)
py.display.flip()
A=True
FIN = True
while A :
    for event in py.event.get() :
        if event.type == py.QUIT :
            A = False
            FIN = False
            break
        if event.type == py.KEYDOWN :
            if event.key == py.K_SPACE :
                A = False 
                break
        elif event.type == py.MOUSEBUTTONDOWN :
            if event.button == 3 :
                A = False
                break

lancement = True
#vent.play(loop = 4)
#vent.play()
while lancement and FIN :
    oiseau_rot = oiseau
    t_chute += 0.03
    #print(t_chute)
    compteur += 1
    for event in py.event.get() :
        if event.type == py.QUIT :
            lancement = False
            break
        elif event.type == py.KEYDOWN :
            if event.key == py.K_SPACE or event.key == py.K_UP :
                aile.play()
                Yb -= saut
                t_chute = 0
        elif event.type == py.MOUSEBUTTONDOWN :
            if event.button == 1 :
                aile.play()
                Yb -= saut
                t_chute = 0
    # faire bouger les nuages
    if compteur*incr % mod.nuage_es == 0 and compteur !=0 :
        del X_nuage[0]
        X_nuage.append(X_nuage[-1]+mod.nuage_es) 
    for i in range(len(X_nuage)):
        X_nuage[i] -= incr
    for i in X_nuage :
        fenetre.blit(nuage,[i,Yn])    
    # faire tomber l'oiseau
    Yb= mod.fy(t_chute,Yb)
    Vy =  6 * t_chute - 4
    #print(Vy)
    #angle= 1-(t_chute * 135)
    oiseau_rot= py.transform.rotate(oiseau_rot,round(- 10.94*Vy+1.24))

    
    fenetre.blit(oiseau_rot,[Xb,Yb])
    C_tube = mod.dessin_tube(fenetre,C_tube,incr,tube_haut,tube_bas)
    t += increment

    # si l'oiseau dépasse les limites 
    if Yb >= 500 or Yb<=0 :
        mod.fin_loose(fenetre, score)
        lancement = False
        break
    # quand on arrive au niveau des tubes 
    for i in range(len(C_tube)):
        if Xb == C_tube[i][0]-28 :
            point.play()
            score+=1
            del C_tube[0]
            C_tube.append([C_tube[-1][0] + mod.distance , mod.tirage()])
        if Xb >= C_tube[i][0]-28  and Xb <= C_tube[i][0]-28+mod.largueur :
            if Yb <= C_tube[i][1] or Yb >= C_tube[i][1]+mod.separt :
                mod.fin_loose(fenetre,score)
                lancement = False
                break

    mod.score_update(fenetre,score)
    py.time.delay(round(increment*1000))
    py.display.flip()

sleep(1)
py.quit()
