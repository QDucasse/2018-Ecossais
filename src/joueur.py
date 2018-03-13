#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 18:25:13 2018

@author: quentin
"""

from carte import Carte
from plateau import Plateau

class Joueur(list):
    
    
    def __init__(self,taille,no,partie):
        ''' 
        Crée un joueur à travers une main de taille donnée et un numéro caractéristique.
        
        Paramètres
        ----------
        Taille de la main du joueur
        Numéro du joueur
        Plateau en cours
        Partie en cours

        '''
        self.jeu=partie
        self.plateau=partie.plateau
        self.taille=taille
        self.numero=no
    
    
    def __str__(self):
        ''' 
        Affiche la main du joueur en question
        
        Paramètres
        ----------
        Aucun
        '''
        res=[]
        for carte in self:
            res.append(str(carte))
        return str(res)
            
        
        
    def jouer(self,no_carte,position):
        '''
        Joue une carte de la main d'un joueur dans la position donnée
        Correspond aux actions successives de placer et piocher pour compléter la main
        
        Paramètres
        ----------
        Carte choisie
        Position visée
        '''
        self.placer(no_carte,position)
        self.piocher()
    
    
    def placer(self,no_carte,position):
        '''
        Place la carte sélectionnée à l'emplacement donné
        
        Paramètres
        ----------
        Carte choisie
        Position visée sous la forme d'un tuple
        '''
        
        #Placement de la carte sur le tapis
        self.plateau.tapis[position[0]][position[1]]=self[no_carte] 
        
        #Rafraîchissement des bornes pour y faire apparaître la carte
        self.jeu.rafraichissementIntegral
       
        #On mémorise la borne sur laquelle la carte a été placée
        borneEnCours=self.jeu.ensembleBorne[position[1]]
        
        #Si jamais un des groupes est complété, on change la valeur de premierComplete !
        if self.jeu.joueurCourant==1:
            if (borneEnCours.g1.estComplet() and not borneEnCours.g2.estComplet()):
                self.jeu.borneEnCours.premierComplete=1
        else:
            if (borneEnCours.g1.estComplet() and not borneEnCours.g2.estComplet()):
                self.jeu.borneEnCours.premierComplete=2
        
        #Comparaison si jamais les deux groupes sont complets
        if (borneEnCours.g1.estComplet() and borneEnCours.g2.estComplet()):
            borneEnCours.comparer()
        
        #Suppression de la carte de la main du joueur
        del(self[no_carte])
        
   
    def peutJouer(self,position):
        '''
        Vérifie que le joueur courant peut bien placer sa carte à l'endroit choisi
        
        Paramètres
        ----------
        Position visée
        
        Renvoie
        -------
        True ou False
        ''' 
        #Vérification du type des données insérées


        if (type(position)==tuple):
            #Vérification côté du plateau et emplacement différent d'une borne
            if self.jeu.joueurCourant==1:
                cd1= (position[0]<3) and (position[0]>=0)
            else:
                cd1= (position[0]>3) and (position[0]<=6)
            
            #Vérification emplacement vide
            cd2=str(self.plateau.tapis[position[0]][position[1]])=='  '
    
            return cd1 and cd2
        
        else:
            return False
        
      
        
        
    def piocher(self):
        '''
        Pioche la première carte de la pioche et l'ajoute à la main du joueur
        
        Paramètres
        ----------
        Aucun
        '''
        if self.jeu.pioche!=[]:
            self.append(Carte(self.jeu.pioche.pop()[1],self.jeu.pioche.pop()[0]))

