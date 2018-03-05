#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 18:25:13 2018

@author: quentin
"""

from carte import Carte
from plateau import Plateau

class Joueur(list):
    
    
    def __init__(self,taille,no,plat,partie):
        ''' 
        Crée un joueur à travers une main de taille donnée et un numéro caractéristique.
        
        Paramètres
        ----------
        Taille de la main du joueur
        Numéro du joueur
        Plateau en cours
        Partie en cours

        '''
        self.jeu=partie
        self.plateau=plat
        self.taille=taille
        self.numero=no
    
    
    def __str__(self):
        ''' 
        Affiche la main du joueur en question
        
        Paramètres
        ----------
        Aucun
        '''
        res=[]
        for carte in self:
            res.append(str(carte))
        return str(res)
            
        
        
    def jouer(self,no_carte,position):
        '''
        Joue une carte de la main d'un joueur dans la position donnée
        Correspond aux actions successives de placer et piocher pour compléter la main
        
        Paramètres
        ----------
        Carte choisie
        Position visée
        '''
        self.placer(no_carte,position)
        self.piocher()
        
    
    
    def placer(self,no_carte,position):
        '''
        Place la carte sélectionnée à l'emplacement donné
        
        Paramètres
        ----------
        Carte choisie
        Position visée sous la forme d'un tuple
        '''
        self.plateau.tapis[position[0]][position[1]]=str(self[no_carte])
        self[no_carte].position=str(position)
        del(self[no_carte])
    
    def piocher(self):
        '''
        Pioche la première carte de la pioche et l'ajoute à la main du joueur
        
        Paramètres
        ----------
        Aucun
        '''
        self.append(Carte(self.jeu.pioche.pop()[1],self.jeu.pioche.pop()[0],'MainJoueur{0}'.format(self.numero)))

