#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 18:25:16 2018

@author: quentin
"""

from carte import Carte

class Plateau():

      
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
             self.tapis.append([Carte(0,'X')]*nb_bornes)
         self.tapis[3]=['XX','XX','XX','XX','XX','XX','XX','XX','XX']
         
         
    def __str__(self):
        ''' 
        Affiche le plateau de jeu en passant par l'affichage de chacune des cartes.
        
        Paramètres
        ----------
        Aucun
        '''
        s='[ '
        for ligne in self.tapis:
            for i in range(len(ligne)):
                if i!=len(ligne)-1:
                    s=s+str(ligne[i])+' , '
                else:
                    s=s+str(ligne[i])+' '
            s=s+']\n[ '
        return s
    
    
    
    def totalPoints(self, no_borne, no_joueur):
        
        if no_joueur == 1:
            C1 = self.tapis[2][no_borne]
            C2 = self.tapis[1][no_borne]
            C3 = self.tapis[0][no_borne]
        
        if no_joueur == 2:
            C1 = self.tapis[4][no_borne]
            C2 = self.tapis[5][no_borne]
            C3 = self.tapis[6][no_borne]
        
        return C1.valeur + C2.valeur + C3.valeur
    
    
    
    
    
    
    