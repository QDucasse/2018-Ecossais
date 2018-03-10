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
        
        self.plateau.tapis[position[0]][position[1]]=str(self[no_carte]) 
        #Placement de la carte sur le tapis
        
        self[no_carte].position=str(position)                           
        #Rafraîchissement de la position de la carte en elle-même
        
        self.jeu.rafraichissementIntegral
        #Rafraîchissement des bornes pour y faire apparaître la carte
        
        borneEnCours=self.jeu.ensembleBorne[position[1]]
        #On mémorise la borne sur laquelle la carte a été placée
        if self.jeu.joueurCourant==1:
            if borneEnCours.g1.force!=0 and borneEnCours.premierComplete==0:
                borneEnCours.premierComplete=1
                borneEnCours.comparer()
        #On vérifie que le groupe de carte du côté du joueur venant de jouer est incomplet et s'il vient
        #d'être complété, on change la valeur de PremierComplété
        else:
            if borneEnCours.g1.force==0 and borneEnCours.premierComplete==0:
                borneEnCours.premierComplete=2
                borneEnCours.comparer()
        
        del(self[no_carte])
        #Suppression de la carte de la main du joueur
   
        