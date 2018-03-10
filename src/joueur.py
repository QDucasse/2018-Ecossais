#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 18:25:13 2018

@author: quentin
"""

from carte import Carte
from plateau import Plateau

class Joueur(list):
    
    
    def __init__(self,taille,no,plat,partie):
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
        self.plateau=plat
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
            cd2=self.plateau.tapis[position[0]][position[1]]=='  '
            
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
            self.append(Carte(self.jeu.pioche.pop()[1],self.jeu.pioche.pop()[0],'MainJoueur{0}'.format(self.numero)))

