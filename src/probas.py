#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 19:09:07 2018

@author: quentin
"""

from random import shuffle
from IA_0 import IA_0
from IA_1 import IA_1
from IA_2 import IA_2
from IA_3 import IA_3
from ecossais import Jeu
from joueur import Joueur
from carte import Carte
from plateau import Plateau
from groupeCartes import GroupeCartes
from borne import Borne
import numpy.random as rnd  
import numpy as np 
from time import sleep
import matplotlib.pyplot as plt
import time
import datetime
import pickle


#########################       Calcul des probas/test      ##################################
#global T1, T2
#    T1, T2, = 0, 0
#    #for k in range(5):
#        game=Jeu()
#        game.start(True)
#
#    print("Victoires J1 :", 100*T1/(T1+T2), '%')
#    global  t, p11, p22
#    t=0
#    p11 = [0]*21
#    p22 = [0]*21
#    print(len(p11), len(p22))
#    print(p11,'\n', p22)
#    plt.plot(p11, label='J1 proba1')
#    plt.plot(p22, label='J2 proba2')
#    plt.legend()        
#p1 = [0.4375, 0.43478261, 0.43181818, 0.42857143, 0.425, 0.42105263, 0.41666667, 0.41176471, 0.40625, 0.4, 0.39285714, 0.38461538, 0.375, 0.36363636, 0.35, 0.33333333, 0.3125, 0.28571429, 0.25, 0.2, 0.125]
#
#p2 = [0.44680851, 0.44444444, 0.44186047, 0.43902439, 0.43589744, 0.43243243, 0.42857143, 0.42424242, 0.41935484, 0.4137931, 0.40740741, 0.4, 0.39130435, 0.38095238, 0.36842105, 0.35294118, 0.33333333, 0.30769231, 0.27272727, 0.22222222, 0.14285714, ]
#        
#plt.plot(p1, label='J1 proba1')
#plt.plot(p2, label='J2 proba2')
#plt.legend()





####################  Exemple de plateau de jeu (pas viable)  #######################
g = Jeu()
g.plateau.tapis[2][0] = Carte(1, 'D')    
g.plateau.tapis[2][1] = Carte(2, 'E')
g.plateau.tapis[1][1] = Carte(1, 'F')
g.plateau.tapis[2][2] = Carte(6, 'D')



###################  Quelques cartes  ###############################
a = Carte(1, 'D')
b = Carte(2, 'E')
c = Carte(1, 'F')
d = Carte(6, 'D')




################# Mesure des probas, pour être sûr  #################
def MesProbas(nb = 150, lin = np.inf):
    T1, T2 = [0]*42, [0]*42
    
    for p in range(42):
        
        for k in range(nb*int(p/lin+1)):
            print('\n',100*k/(nb*int(p/lin+1)), '%  du tour', p+1, '/42')
            g = Jeu()
            g.pioche=[] 
            for i in range(9):
                for couleur in ['A','B','C','D','E','F']:
                    g.pioche.append('%c%i'%(couleur,i+1))
            if p!=0:
                g.pioche = g.pioche[:-p]
            
            t = time.time()
            for s in range(k):        #k%(1+int((p/lin+1)/2))
                shuffle(g.pioche)
            
            
            for i in range(g.J1.taille):
                g.J1.piocher()
                g.J2.piocher()
            mainJ1 = [str(g.J1[j]) for j in range(len(g.J1))]
            mainJ2 = [str(g.J2[j]) for j in range(len(g.J2))]
            
                
            if 'A1' in mainJ1:
#                T1 += 1
#                T3 += 1
                g.J1.pop(mainJ1.index('A1'))
                
            if 'A1' in mainJ2:
#                T2 += 1
#                T4 += 1
                g.J2.pop(mainJ2.index('A1'))
                
            
            print("Longueur pioche = ", len(g.pioche), 'Temps exec = ', time.time()-t)
            
             
            if p%2 == 1:
                g.J2.piocher()
                mainJ2 = [str(g.J2[i]) for i in range(len(g.J2))]
                if 'A1' in mainJ2:
                    T2[p] += 1/(nb*int(p/lin+1))
                g.J2.pop()
            
            while len(g.pioche) > 0:
                
                g.J1.piocher()
                g.J2.piocher()
                mainJ1 = [str(g.J1[i]) for i in range(len(g.J1))]
                mainJ2 = [str(g.J2[i]) for i in range(len(g.J2))]
                if 'A1' in mainJ1:
                    T1[p] += 1/(nb*int(p/lin+1))
                if 'A1' in mainJ2:
                    T2[p] += 1/(nb*int(p/lin+1))
                g.J1.pop()
                g.J2.pop()
                    
        print ("Proba J1 :", T1, "\n\n Proba J2 :", T2, " \n\nTotal ", np.array(T1)+np.array(T2))
#        print("origine J1 :", 100*np.array(T3)/nb, " origine J2 :", 100*np.array(T4)/nb)
        
    plt.plot(T1, 'b.', label = 'Probas J1')
    plt.plot(T2, 'y.', label = 'Probas J2')
    plt.legend()
    plt.grid()















################# Mesure des probas, pour être sûr  #################
def MesProbas2(nb = 150, lin = np.inf):
    T1, T2 = [0]*42, [0]*42
    
    for p in range(42):
        
        g = Jeu()
        Pioche=[] 
        for i in range(9):
            for couleur in ['A','B','C','D','E','F']:
                Pioche.append('%c%i'%(couleur,i+1))
                
        if p != 0:
            Pioche = Pioche[:-p]
        
        
        for k in range(nb*int(p/lin+1)):
            print(100*k/(nb*int(p/lin+1)), '%  du tour', p+1, '/42')
            
            g.pioche = [Pioche[i] for i in range(len(Pioche))]
            shuffle(g.pioche)
            Pioche = [g.pioche[i] for i in range(len(g.pioche))]
            
            
            for i in range(g.J1.taille):
                g.J1.piocher()
                g.J2.piocher()
            mainJ1 = [str(g.J1[j]) for j in range(len(g.J1))]
            mainJ2 = [str(g.J2[j]) for j in range(len(g.J2))]
            
                
            if 'A1' in mainJ1:
#                T1 += 1
#                T3 += 1
                g.J1.pop(mainJ1.index('A1'))
            if 'A1' in mainJ2:
#                T2 += 1
#                T4 += 1
                g.J2.pop(mainJ2.index('A1'))
                
            
            print("Longueur pioche = ", len(g.pioche), '\n')
            
                
            while len(g.pioche) > 0:
                g.J1.piocher()
                g.J2.piocher()
                mainJ1 = [str(g.J1[i]) for i in range(len(g.J1))]
                mainJ2 = [str(g.J2[i]) for i in range(len(g.J2))]
                if 'A1' in mainJ1:
                    T1[p] += 1/(nb*int(p/lin+1))
                if 'A1' in mainJ2:
                    T2[p] += 1/(nb*int(p/lin+1))
                g.J1.pop()
                g.J2.pop()
                    
        print ("Proba J1 :", T1, "\n\n Proba J2 :", T2, " \n\nTotal ", np.array(T1)+np.array(T2))
#        print("origine J1 :", 100*np.array(T3)/nb, " origine J2 :", 100*np.array(T4)/nb)
        
    plt.plot(T1, 'b.', label = 'Probas J1')
    plt.plot(T2, 'y.', label = 'Probas J2')
    plt.legend()
    plt.grid()