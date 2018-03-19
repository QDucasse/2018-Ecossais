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
    
    
    def placer(self,no_carte,no_borne):
        '''
        Place la carte sélectionnée à l'emplacement donné
        
        Paramètres
        ----------
        Carte choisie
        Position visée sous la forme d'un entier correspondant à une borne
        '''
        
        if self.jeu.joueurCourant==1:
            ordonnee=self.jeu.ensembleBorne[no_borne].g1.carteCourante
            
            self.jeu.ensembleBorne[no_borne].g1.carteCourante+=1
        elif self.jeu.joueurCourant==2:
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
   
    def peutJouer(self,no_borne):
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


        if (type(no_borne)==int):
        #Vérification côté du plateau et emplacement différent d'une borne
            cd1 = (no_borne<9) and (no_borne>-1)
            if self.jeu.joueurCourant==1:
                ord1 = self.jeu.ensembleBorne[no_borne].g1.carteCourante 
                cd2=ord1<3  #Vérif bon côté du plateau
                cd3=str(self.plateau.tapis[ord1][no_borne])=='  ' #Vérif emplacement vide
            else:
                ord2=self.jeu.ensembleBorne[no_borne].g2.carteCourante
                cd2=ord2<7 #Vérif bon côté du plateau
                cd3=str(self.plateau.tapis[ord2][no_borne])=='  ' #Vérif emplacement vide
            
            return cd1 and cd2 and cd3
        
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
            nouvelleCarte=self.jeu.pioche.pop()
            self.append(Carte(int(nouvelleCarte[1]),nouvelleCarte[0]))

