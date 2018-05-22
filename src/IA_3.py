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
        self.carteJouee = ''
        self.emplacementVise = ''
    
    def jouer(self,no_IA=2):
        '''
        Cette IA favorise l'apparition de suites couleur sur ses borne, avec brelans en cas d'impossibilité ou de mauvaise probabilité.
        Joue une carte de la main d'un joueur 
        Correspond aux actions successives de choisir, placer et piocher pour compléter la main.
        
        
        Paramètres
        ----------
        Numéro de joueur de l'IA (1 ou 2, par défaut 2)
        '''
#        self.placer(no_carte, no_borne)
#        self.piocher()
    

    
    def chercheSuites(self, no_IA):
        
        ### on commence par trier la main par couleur puis valeur
        mainClassee = sorted(self, key=lambda card: [card.couleur, card.valeur])
        for i in range(len(self)):
            self[i] = mainClassee[i]
        
        
        
        ### on cherche les embryons de suite déjà sur le tapis
        suitesTap = []
        for borne in self.jeu.ensembleBorne:
            if no_IA == 1:
                difVal = abs(borne.g1.C1.valeur-borne.g1.C2.valeur)
                if not borne.g1.estComplet() and ((difVal>0 and difVal<2) or difVal==borne.g1.C1.valeur) :    # on a une ou deux cartes sur la borne, qui rendent possibles une suite
                    suitesTap.append(borne)

            if no_IA == 2:
                difVal = abs(borne.g1.C1.valeur-borne.g1.C2.valeur)
                if not borne.g1.estComplet() and ((difVal>0 and difVal<2) or difVal==borne.g1.C1.valeur) :    # on a une ou deux cartes sur la borne, qui rendent possibles une suite
                    suitesTap.append(borne)
                    
        
        ### on cherche les suites complètes ou possibles à compléter dans la main
        suitesCompletesMain = []
        suitesACompleterMain = []
        dicoCouleur = {'A': 0, 'B' :1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}
        
        for i in range(1,len(self)):
            carte_prev = self[i-1]
            carte = self[i]
            try:
                carte_next = self[i+1]
            except:
                carte_next = Carte(0, 'X')
                
            if carte_next.couleur == carte_prev.couleur and carte_next.valeur - carte_prev.valeur == 2:  #suite complète
                suitesCompletesMain.append([i-1, i, i+1])
                
            elif carte.couleur == carte_prev.couleur and carte.valeur-carte_prev.valeur == 1:             #on va chercher la première ou la dernière de la suite
                probaTot = self.jeu.proba[dicoCouleur[carte.couleur]][carte.valeur] + self.jeu.proba[dicoCouleur[carte.couleur]][carte_prev.valeur -2]
                #Probabilité d'obtenir la première ou dernière de la suite
                if probaTot > 0.3:
                    suitesACompleterMain.append = ([i-1, i])

            elif carte.couleur == carte_prev.couleur and carte.valeur-carte_prev.valeur == 2:            
#on va chercher la carte du milieu
                probaTot = self.jeu.proba[dicoCouleur[carte.couleur]][carte_prev.valeur]
#Probabilité d'obtenir la première ou dernière de la suite
                if probaTot > 0.3:
                    suitesACompleterMain.append = ([i-1, i])

        return [suitesCompletesMain, suitesACompleterMain, suitesTap]
        
        
    
    def strategie(self, no_borne, no_IA):
        
        B = self.jeu.ensembleBorne[no_borne-1] #on récupère l'objet borne et ses fonctionnalités
        
        
    
    
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







