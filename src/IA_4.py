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
    
    def jouer(self,no_IA=2):
        '''
        Cette IA favorise l'apparition de suites couleur sur ses borne, avec brelans en cas d'impossibilité ou de mauvaise probabilité.
        Joue une carte de la main d'un joueur 
        Correspond aux actions successives de choisir, placer et piocher pour compléter la main.
        
        
        Paramètres
        ----------
        Numéro de joueur de l'IA (1 ou 2, par défaut 2)
        '''
        self.placer(no_carte, no_borne)
        self.piocher()
    
    
    def recupBorne(self, no_borne): #permet de récupérer l'objet borne et ses fonctionnalités
        if no_borne == 1:
            return self.jeu.borne1
        if no_borne == 2:
            return self.jeu.borne2
        if no_borne == 3:
            return self.jeu.borne3
        if no_borne == 4:
            return self.jeu.borne4
        if no_borne == 5:
            return self.jeu.borne5
        if no_borne == 6:
            return self.jeu.borne6
        if no_borne == 7:
            return self.jeu.borne7
        if no_borne == 8:
            return self.jeu.borne8
        if no_borne == 9:
            return self.jeu.borne9
    
    def advCombi(self, advTot):
        Combis = ['Somme', 'Suite', 'Couleur', 'Brelan', 'Suite Couleur']
        advC = [Combis[advTot[0]], advTot[1]]   #on remplace la valeur de la force le nom de la combinaison
        return advC
        
    
    def strategie(self, no_borne, no_IA):
        
        B = self.recupBorne(no_borne)
        
        if no_IA == 1 and B.g2.estComplet():
            advTot = [B.g2.force, B.g2.totalPoints]
        if no_IA == 2 and B.g1.estComplet():
            advTot = [B.g1.force, B.g1.totalPoints]
        combinaisonAdv = advCombi(advTot)
        
        
        
    
    
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