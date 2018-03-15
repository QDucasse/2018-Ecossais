#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 16:40:31 2018

@author: quentin
"""

from carte import Carte
from plateau import Plateau
from joueur import Joueur
import numpy.random as rnd

class IA_0(Joueur):
    
    
    def placer(self,no_carte):
        '''
        Place la carte sélectionnée à l'emplacement donné
        
        Paramètres
        ----------
        Carte choisie
        Position visée sous la forme d'un tuple
        '''
        
        position=(rnd.randint(4,7),rnd.randint(0,9))
        
        while not self.peutJouer(position):
             position=(rnd.randint(4,7),rnd.randint(0,9))
        
        
        #Placement de la carte sur le tapis
        self.plateau.tapis[position[0]][position[1]]=self[no_carte] 
        
        #Rafraîchissement des bornes pour y faire apparaître la carte
        self.jeu.rafraichissementIntegral()
       
        #On mémorise la borne sur laquelle la carte a été placée
        borneEnCours=self.jeu.ensembleBorne[position[1]]
        
        #Si jamais un des groupes est complété, on change la valeur de premierComplete !
        borneEnCours.verifPremierComplete(self.jeu)
        
        #Comparaison si jamais les deux groupes sont complets
        borneEnCours.comparer()
        
        #Suppression de la carte de la main du joueur
        del(self[no_carte])
        
   
        