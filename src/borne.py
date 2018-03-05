#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 18:25:17 2018

@author: quentin
"""

from plateau import Plateau
from joueur import Joueur
from carte import Carte
from groupeCartes import GroupeCartes


class Borne():
    
    
    def __init__(self,pos,plateau):
        ''' 
        Crée une borne séparant les groupes de cartes g1 et g2.
        
        Paramètres
        ----------
        Groupe de cartes 1: g1
        Groupe de cartes 2: g2

        '''
        self.g1=GroupeCartes(Carte(self.plateau.tapis[0][pos][1],self.plateau.tapis[0][pos][0],' '),
                             Carte(self.plateau.tapis[1][pos][1],self.plateau.tapis[1][pos][0],' '),
                             Carte(self.plateau.tapis[2][pos][1],self.plateau.tapis[2][pos][0],' '))
                             # le groupe de cartes du côté du joueur 1
        self.g2=GroupeCartes(Carte(self.plateau.tapis[4][pos][1],self.plateau.tapis[4][pos][0],' '),
                             Carte(self.plateau.tapis[5][pos][1],self.plateau.tapis[5][pos][0],' '),
                             Carte(self.plateau.tapis[6][pos][1],self.plateau.tapis[6][pos][0],' ')) 
                             # le groupe de cartes du côté du joueur 2
        self.position=pos       # la position de la borne sur le plateau
        self.premierComplete=0  # conserve  1 ou 2 correspondant au côté du joueur ayant fini en premier
        self.gagnant= ' '
        self.plateau=plateau
        
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
            self.plateau[3][self.pos]='J1'
        elif self.g2.force>self.g1.force:
            self.plateau[3][self.pos]='J2'
        else:
            # En cas d'égalité, on compare le total de points 
            if self.g1.totalPoints>self.g2.totalPoints:
                self.plateau[3][self.pos]='J1'
            elif self.g2.totalPoints>self.g1.totalPoints:
                self.plateau[3][self.pos]='J2'
            else:
                # Enfin, en cas d'égalité à nouveau, le premier à avoir complété don côté gagne
                self.gagnant= 'J{0}'.format(self.premierComplete)
                
          
