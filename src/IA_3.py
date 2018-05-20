# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 17:48:35 2018

@author: Matthieu
"""

from carte import Carte
from plateau import Plateau
from joueur import Joueur
import numpy.random as rnd

class IA_3(Joueur):
    
    def __init__(self,taille,no,partie):
        super().__init__(taille,no,partie)
        self.niveau = 3
    
    def jouer(self,no_IA=2):
        '''
        Joue une carte de la main d'un joueur 
        Correspond aux actions successives de choisir, placer et piocher pour compléter la main
        
        Paramètres
        ----------
        Numéro de joueur de l'IA (1 ou 2, par défaut 2)
        '''
        self.placer(no_carte, no_borne)
        self.piocher()
    
    
    def recupBorne(self, no_borne): 
        #permet de récupérer l'objet borne et ses fonctionnalités
        '''
        Récupère l'objet borne et ses fonctionnalités
        
        Paramètres
        ----------
        no_borne le numéro de la borne visée
        '''
        return self.jeu.ensembleBorne[no_borne]
    
    
    def strategie(self, no_borne, no_IA):
        
        B = self.recupBorne(no_borne)
        
        if no_IA == 1 and B.g2.estComplet():
            advTot = B.g2.calculForce()
        if no_IA == 2 and B.g1.estComplet():
            advTot = B.g1.calculForce()
        
        
    
    
    def placer(self, no_carte, no_borne):
        
        '''
        Place la carte indiquée sur la zone de jeu de l'IA, à l'emplacement indiqué
        
        Paramètres
        ----------
        Carte choisie
        Borne visée
        '''
        no_IA = self.numero
        if no_IA == 1:
            ordonnee=self.jeu.ensembleBorne[no_borne].g1.carteCourante
            self.jeu.ensembleBorne[no_borne].g1.carteCourante-=1
        
        elif no_IA == 2:
            ordonnee=self.jeu.ensembleBorne[no_borne].g2.carteCourante
            self.jeu.ensembleBorne[no_borne].g2.carteCourante+=1
            
        #Placement de la carte sur le tapis
        
        self.plateau.tapis[ordonnee][no_borne]=self[no_carte] 
        
        #Rafraîchissement des bornes pour y faire apparaître la carte
        self.jeu.rafraichissementIntegral()
       
        #On mémorise la borne sur laquelle la carte a été placée
        borneEnCours=self.jeu.ensembleBorne[no_borne]
        
        #Si jamais un des groupes est complété, on change la valeur de premierComplete !
        borneEnCours.verifPremierComplete(self.jeu)
        
        #Comparaison si jamais les deux groupes sont complets
        borneEnCours.comparer()
        
        #Suppression de la carte de la main du joueur
        del(self[no_carte])   