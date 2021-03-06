#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 18:25:15 2018

@author: quentin
"""

class Carte():
    
    
    
    
    def __init__(self,valeur,couleur):
        ''' 
        Crée une carte donnée.
        
        Paramètres
        ----------
        Valeur de la carte
        Couleur de la carte

        '''
        self.valeur=valeur
        self.couleur=couleur
        
    
    
    def __str__(self):
        '''
        Affiche le code de la carte 'CouleurValeur'.
        
        Paramètres
        ----------
        Aucun
        
        Renvoie
        -------
        s: str
            La chaîne de caractères qui sera affichée via ''print''
            
        '''
        if self.valeur==0 and self.couleur=='X':
            return '  '
        else:
            return '{0}{1}'.format(self.couleur,self.valeur)