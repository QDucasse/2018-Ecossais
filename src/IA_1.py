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
    
    def __init__(self,taille,no,partie):
        super().__init__(taille,no,partie)
        self.niveau = 1
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
        Place une carte sur une borne de manière à y avoir plus de points que l'adversaire.
        84% de victoire face à IA_0 en J1
        76% de victoire face à IA_0 en J2
        
        Paramètres
        ----------
        Position visée sous la forme d'un tuple
        '''
        
        #Tri de la main par valeurs croissantes
        
        mainClassee = sorted(self, key=lambda card: card.valeur)
        for i in range(len(self)):
            self[i] = mainClassee[i]
        
        
        advList = []   #Liste des bornes où l'adversaire a joué
        
        for i in range(9):  #RQ : no_IA -> 1 + no_IA%2  =>  1->2 et 2->1
            
            #on regarde le plateau côté adversaire et on cherche les bornes où il a plus de points que IA
            totAdv = self.jeu.plateau.totalPoints(i, 1 + no_IA%2)  
            
            if self.peutJouer(i) and totAdv > self.jeu.plateau.totalPoints(i, no_IA) :  
                advList.append(i)
        
        advList = sorted(advList, key=lambda i: self.jeu.plateau.totalPoints(i, 1 + no_IA%2)-self.jeu.plateau.totalPoints(i, no_IA))  #classement par écart de point entre les deux camps
        
        
        if advList != []:
            #Choix de la borne
            no_borne = advList[0]
            k, fin = 0, 0
            while not (fin or self.peutJouer(no_borne)):
                k += 1
                if k < len(advList):
                    no_borne = advList[k]
                else:
                    fin = 1
            
            
            #Choix de la carte
            no_carte = 0
            advPoints = self.jeu.plateau.totalPoints(no_borne, 1 + no_IA%2)
            Points = self.jeu.plateau.totalPoints(no_borne, no_IA)
            
            while no_carte < len(self) and not Points + self[no_carte].valeur > advPoints :  #tant qu'on a pas plus de points que l'adversaire
                no_carte += 1
          
        # ajout choix random en cas d'impossibilité ou que IA est le premier joueur
        if advList == [] or no_carte == len(self):
            no_carte=rnd.randint(0,6)
            while not self.jeu.bonNumeroCarte(no_carte):
                no_carte=rnd.randint(0,6)
            no_borne=(rnd.randint(0,9))
            while not self.peutJouer(no_borne):
                no_borne=(rnd.randint(0,9))
            
        
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
   
        
