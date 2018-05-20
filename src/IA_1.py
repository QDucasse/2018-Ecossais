# -*- coding: utf-8 -*-
"""
Created on Tue May  1 17:46:59 2018

@author: Matthieu
"""

from carte import Carte
from plateau import Plateau
from joueur import Joueur
import numpy.random as rnd

class IA_1(Joueur):
    
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
        
        Paramètres
        ----------
        Position visée sous la forme d'un tuple
        '''
        
        #Tri de la main par valeurs croissantes
        
        self = sorted(self, key=lambda card: card.valeur)
        
       
        
        advList = []   #Liste des bornes où l'adversaire a joué
        for i in range(9):  #RQ : no_IA -> 1 + no_IA%2  =>  1->2 et 2->1
            totAdv = self.jeu.plateau.totalPoints(i, 1 + no_IA%2)      #on regarde le plateau côté
            if totAdv > self.jeu.plateau.totalPoints(i, no_IA) :       #adversaire et on cherche les bornes         
                advList.append(i)                                      #où il a plus de points que IA
        advList = sorted(advList, key=lambda i: self.jeu.plateau.totalPoints(i, 1 + no_IA%2)-self.jeu.plateau.totalPoints(i, no_IA))  #classement par écart de point entre les deux camps
        no_borne = advList[0]
        
        
        #Choix de la carte
        
        no_carte = 0
        advPoints = self.jeu.plateau.totalPoints(advList[0], 1 + no_IA%2)
        Points = self.jeu.plateau.totalPoints(advList[0], no_IA)
        while advPoints - Points - self[no_carte].valeur > 0 or not self.peutJouer(no_borne):
            no_carte += 1
          
        #########################################################################################
        ############ ajouter choix random en cas d'impossibilité ################################
        #########################################################################################
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
   
        
