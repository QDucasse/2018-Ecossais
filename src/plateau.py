#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 18:25:16 2018

@author: quentin
"""

from carte import Carte

class Plateau():
    
#    
#    def __new__(cls,nb_bornes):
#        plateau = super(Plateau, cls).__new__(cls, (9, nb_bornes))
#        return plateau
#    
#    
#    def __init__(self, nb_bornes):
#        ''' 
#        Crée un plateau de taille donnée.
#        
#        Paramètres
#        ----------
#        Nombre de bornes
#
#        '''
#        self.nb_bornes = nb_bornes
#        self.tapis = np.array([['CC']*nb_bornes]*7, dtype=str)
#        self.tapis[3] = ['B ']*nb_bornes 

      
    def __init__(self,nb_bornes):
         ''' 
         Crée un plateau de taille donnée.
         
         Paramètres
         ----------
         Nombre de bornes

         '''
         self.taille=nb_bornes
         self.tapis=[]
         for i in range(7):
             self.tapis.append([str(Carte(0,'X',' '))]*nb_bornes)
         self.tapis[3]=['XX','XX','XX','XX','XX','XX','XX','XX','XX']
         
         
    def __str__(self):
        ''' 
        Affiche le plateau de jeu.
        
        Paramètres
        ----------
        Self

        '''
        s=''
        for ligne in self.tapis:
            s=s+str(ligne)+'\n'
        return s
