#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 15:46:45 2018

@author: ducassqu
"""
from random import shuffle
from joueur import Joueur
from carte import Carte
from plateau import Plateau
from groupeCartes import GroupeCartes
from borne import Borne
    
    
class Jeu():
    
    
    def __init__(self,plateau=Plateau(9)):
        ''' 
        Crée une partie.
        
        Paramètres
        ----------
        Aucun

        '''
        self.plateau=plateau
        self.J1=Joueur(6,1,self.plateau,self)
        self.J2=Joueur(6,2,self.plateau,self)
        self.nbTours=0
        self.joueurCourant=1
        self.borne1=Borne(0,self.plateau)        
        self.borne2=Borne(1,self.plateau) 
        self.borne3=Borne(2,self.plateau) 
        self.borne4=Borne(3,self.plateau) 
        self.borne5=Borne(4,self.plateau) 
        self.borne6=Borne(5,self.plateau) 
        self.borne7=Borne(6,self.plateau) 
        self.borne8=Borne(7,self.plateau) 
        self.borne9=Borne(8,self.plateau) 
        
        #Initialisation et mise en place de la pioche
        self.pioche=[] 
        for i in range(9):
            for couleur in ['A','B','C','D','E','F']:
                self.pioche.append('%c%i'%(couleur,i+1))
        shuffle(self.pioche)
     
        
    def __str__(self):
        '''
        Affiche le nombre de tours, le joueur courant, le nombre de cartes dans la pioche et la main du joueur en cours
        
        Paramètres
        ----------
        Aucun

        '''
        
        s='{0} tours se sont écoulés, c\'est au joueur {1} de jouer, il reste {2} cartes dans la pioche \n'.format(self.nbTours,self.joueurCourant,len(self.pioche))
        s=s+str(self.plateau)
        return s
        
    def rafraichissementIntegral(self):
        self.borne1.rafraichir        
        self.borne2.rafraichir    
        self.borne3.rafraichir    
        self.borne4.rafraichir    
        self.borne5.rafraichir    
        self.borne6.rafraichir    
        self.borne7.rafraichir    
        self.borne8.rafraichir    
        self.borne9.rafraichir    
    
    def unTour(self):
        '''
        Fait progresser chacune des actions d'une case et donne la main à un des joueurs :
            Le joueur en question joue une carte (place + pioche)
            Le résultat de ses actions s'affiche
            Le nombre de tours s'incrémente
        
        Paramètres
        ----------
        Aucun
        '''
        ######### Affichage du jeu au moment de jouer ########################################
        
        print(self)
        if self.joueurCourant==1:
            print(self.J1)
        else:
            print(self.J2)
        
        ######### On demande au joueur de sélectionner sa carte et la position visée #########
        
        no_carte= eval(input('J{0}, sélectionnez une carte (par son numéro de 1 à 6 \n'.format(self.joueurCourant))) -1
        position= eval(input('Sélectionnez la position visée sous la forme (x,y) \n'))
        if self.joueurCourant==1:
            self.J1.jouer(no_carte,position)
        else:
            self.J2.jouer(no_carte,position)
        
        
        
        ######### Vérification de la victoire d'un des joueurs !! ############################
        
        
        ######### Changement de joueur et incrémentation du tour #############################
        
        if self.joueurCourant==1:
            self.joueurCourant=2
        else:
            self.joueurCourant=1
        
        self.nbTours=self.nbTours+1
        
        
        
        
        
        
        
        
if __name__=='__main__':
    j=Jeu()
    for i in range(j.J1.taille):
        j.J1.piocher()
        j.J2.piocher()
#    for i in range(55):
#        j.unTour()
 
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        