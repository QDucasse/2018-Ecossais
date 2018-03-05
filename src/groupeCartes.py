#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 18:26:48 2018

@author: quentin
"""

from carte import Carte

class GroupeCartes():
    
    
    def __init__(self,C1=Carte(0,'  ','Vide'),C2=Carte(0,'  ','Vide'),C3=Carte(0,'  ','Vide')):
        # On définit Carte(0,'X','Vide) comme un emplacement vide
        ''' 
        Crée un groupe de 3 cartes, la carte vide étant Carte(0,'X','Vide') .
        
        Paramètres
        ----------
        Les 3 cartes qui composent le groupe

        '''
        self.C1 = C1
        self.C2 = C2
        self.C3 = C3
        self.totalPoints = C1.valeur + C2.valeur + C3.valeur
        self.force = 0
    
    
    def calculForce(self): 
        ''' 
        Calcule la force d'un groupe de cartes comme suit :
            5 = Force max, le groupe se constitue de 3 cartes de même couleur dont les valeurs sont consécutives
            4 = 3 cartes de même valeur 
            3 = 3 cartes de même couleur 
            2 = 3 cartes dont les valeurs sont consécutives
            1 = 3 cartes sans lien apparent
            
        Paramètres
        ----------
        Aucun

        '''
        if (self.C1.valeur==0) or (self.C2.valeur==0) or (self.C3.valeur==0):
            self.force=0
            #Ce cas correspond à l'absence d'une des 3 cartes
        
        else:
             l=[self.C1.valeur,self.C2.valeur,self.C3.valeur]
             if ((self.C1.couleur==self.C2.couleur) and (self.C2.couleur==self.C3.couleur)) and (min(l)==max(l)-2):
                 self.force=5
                 #On vérifie que les cartes sont de la même couleur et forment une suite
             elif (self.C1.valeur==self.C2.valeur) and (self.C2.valeur==self.C3.valeur):   
                 self.force=4
                 #On vérifie que les cartes sont de la même valeur 
             elif (self.C1.couleur==self.C2.couleur) and (self.C2.couleur==self.C3.couleur):
                 self.force=3
                 #On vérifie que les cartes sont de la même couleur 
             elif (min(l)==max(l)-2) and (l.count(min(l))==1) and (l.count(max(l))==1):
                 self.force=2
                 #On vérifie que les cartes forment une suite
             else:
                 self.force=1
                 