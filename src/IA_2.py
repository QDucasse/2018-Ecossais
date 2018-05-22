# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 11:25:00 2018

@author: Matthieu
"""


from carte import Carte
from plateau import Plateau
from joueur import Joueur
import numpy.random as rnd

class IA_2(Joueur):
    
    def __init__(self,taille,no,partie):
        super().__init__(taille,no,partie)
        self.niveau = 2
        self.carteJouee = Carte(0,'X')
        self.emplacementVise = 0
    
    def jouer(self,no_IA=2):
        '''
        Joue une carte de la main d'un joueur 
        Correspond aux actions successives de placer et piocher pour compléter la main
        
        Paramètres
        ----------
        Carte choisie
        Numéro de joueur de l'IA (1 ou 2, par défaut 2)
        '''
        self.placer(no_IA)
        self.piocher()


    def placer(self, no_IA=2):
        '''
        Place une carte de valeur k sur la borne indexée par le numéro k.
        100 % de victoire face à IA_0
        100 % de victoire face à IA_1
        
        
        Paramètres
        ----------
        Position visée sous la forme d'un tuple
        '''
        no_carte = 0
        no_borne = self[no_carte].valeur-1
        
        while self.jeu.bonNumeroCarte(no_carte+1) and not self.peutJouer(no_borne): #Si possible, on place la carte de valeur k sur la borne k
             no_carte += 1
             no_borne = self[no_carte].valeur-1

        if not self.peutJouer(no_borne):#si on a pas de carte de la même valeur, hasard
            for b in range(0,9):
                if self.peutJouer(b):
                    no_borne = b
                    no_carte = rnd.randint(0,len(self.jeu.J2))
        
                    
        if no_IA == 1:
            ordonnee=self.jeu.ensembleBorne[no_borne].g1.carteCourante
            self.jeu.ensembleBorne[no_borne].g1.carteCourante-=1
        
        elif no_IA == 2:
            ordonnee=self.jeu.ensembleBorne[no_borne].g2.carteCourante
            self.jeu.ensembleBorne[no_borne].g2.carteCourante+=1
        
        #Placement de la carte sur le tapis
        
        self.plateau.tapis[ordonnee][no_borne]=self[no_carte] 
        self.carteJouee = self[no_carte]
        self.emplacementVise = no_borne
        
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
   
        
