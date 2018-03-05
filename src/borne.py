#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 18:25:17 2018

@author: quentin
"""

from joueur import Joueur
from carte import Carte
from plateau import Plateau
from groupeCartes import GroupeCartes
from ecossais import Jeu

class Borne():
    
    
    def __init__(self,g1,g2,pos):
        ''' 
        Crée une borne séparant les groupes de cartes g1 et g2.
        
        Paramètres
        ----------
        Groupe de cartes 1: g1
        Groupe de cartes 2: g2

        '''
        self.g1=g1              # le groupe de cartes du côté du joueur 1
        self.g2=g2              # le groupe de cartes du côté du joueur 2
        self.position=pos       # la position de la borne sur le plateau
        self.premierComplete=0  # conserve  1 ou 2 correspondant au côté du joueur ayant fini en premier
        self.gagnant= ' '
     
        
    def comparer(self): 
        '''
        Compare les 2 groupes de cartes de chacun des côtés de la borne
        La victoire et donc la possession de la borne est attribuée au joueur possédant
        le groupe le plus fort et, en cas d'égalité, de plus haut total de points et, en
        cas d'égalité, le premier complété
        
        Paramètres
        ----------
        Aucun
        '''
        # Première condition de victoire via la force
        if self.g1.force>self.g2.force:
            self.gagnant= 'J1'
        elif self.g2.force>self.g1.force:
            self.gagnant= 'J2'
        else:
            # En cas d'égalité, on compare le total de points 
            if self.g1.totalPoints>self.g2.totalPoints:
                self.gagnant= 'J1'
            elif self.g2.totalPoints>self.g1.totalPoints:
                self.gagnant= 'J2'
            else:
                # Enfin, en cas d'égalité à nouveau, le premier à avoir complété don côté gagne
                self.gagnant= 'J{0}'.format(self.premierComplete)
                
          
