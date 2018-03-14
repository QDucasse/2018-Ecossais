#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 18:25:17 2018

@author: quentin
"""

from plateau import Plateau
from joueur import Joueur
from carte import Carte
from groupeCartes import GroupeCartes


class Borne():
    
    
    def __init__(self,pos,plateau):
        ''' 
        Crée une borne séparant les groupes de cartes g1 et g2.
        
        Paramètres
        ----------
        Position sur le plateau
        Plateau

        '''
        self.position=pos       # la position de la borne sur le plateau
        self.premierComplete=0  # conserve  1 ou 2 correspondant au côté du joueur ayant fini en premier
        self.plateau=plateau
        
        self.g1=GroupeCartes(Carte(self.plateau.tapis[0][self.position].valeur,self.plateau.tapis[0][self.position].couleur),
                             Carte(self.plateau.tapis[1][self.position].valeur,self.plateau.tapis[1][self.position].couleur),
                             Carte(self.plateau.tapis[2][self.position].valeur,self.plateau.tapis[2][self.position].couleur))
                                # le groupe de cartes du côté du joueur 1
        self.g2=GroupeCartes(Carte(self.plateau.tapis[4][self.position].valeur,self.plateau.tapis[4][self.position].couleur),
                             Carte(self.plateau.tapis[5][self.position].valeur,self.plateau.tapis[5][self.position].couleur),
                             Carte(self.plateau.tapis[6][self.position].valeur,self.plateau.tapis[6][self.position].couleur)) 
                                # le groupe de cartes du côté du joueur 2
                                
        
    def __str__(self):
        '''
        Affiche 'Contenu du groupe 1 - No de borne - Contenu du groupe 2'.
        
        Paramètres
        ----------
        Aucun
        
        Renvoie
        -------
        s: str
            La chaîne de caractères qui sera affichée via ''print''
        '''
        return str(self.g1)+' - '+str(self.position)+' - '+str(self.g2)
    
    
    def peutComparer(self):
        '''
        Vérifie que chacun des groupes de cartes de part et d'autre de la borne est bien complet
        
        Paramètres
        ----------
        Aucun
        
        Renvoie
        -------
        True ou False
        '''
        self.g1.calculForce()
        self.g2.calculForce()
        return (self.g1.estComplet() and self.g2.estComplet())
    
    
    def comparer(self): 
        '''
        Compare les 2 groupes de cartes de chacun des côtés de la borne
        La victoire et donc la possession de la borne est attribuée au joueur possédant
        le groupe le plus fort et, en cas d'égalité, de plus haut total de points et, en
        cas d'égalité, le premier complété
        
        Paramètres
        ----------
        Aucun
        '''
        #Verif de possibilité de comparaison
        if self.peutComparer():
            # Première condition de victoire via la force
            if (self.g1.force>self.g2.force):
                self.plateau.tapis[3][self.position]='J1'
            elif (self.g2.force>self.g1.force):
                self.plateau.tapis[3][self.position]='J2'
            else:
                # En cas d'égalité, on compare le total de points 
                if (self.g1.totalPoints>self.g2.totalPoints):
                    self.plateau.tapis[3][self.position]='J1'
                elif (self.g2.totalPoints>self.g1.totalPoints):
                    self.plateau.tapis[3][self.position]='J2'
                else:
                    # Enfin, en cas d'égalité à nouveau, le premier à avoir complété son côté gagne
                    self.plateau.tapis[3][self.position]='J{0}'.format(self.premierComplete)
           
        
    def verifPremierComplete(self,jeu):
        '''
        Accesseur de la variable d'instance premierComplete
        
        Parametres
        ----------
        Jeu la partie en cours
        '''
        if jeu.joueurCourant==1:
            if (self.g1.estComplet() and not self.g2.estComplet()):
                self.premierComplete=1
        else:
            if (self.g1.estComplet() and not self.g2.estComplet()):
                self.premierComplete=2
        
        

         
    def rafraichir(self):
        '''
        Rafraîchit le contenu de la borne à l'aide des éléments du tableau
        
        Paramètres
        ----------
        Aucun
        '''
        self.g1=GroupeCartes(Carte(self.plateau.tapis[0][self.position].valeur,self.plateau.tapis[0][self.position].couleur),
                             Carte(self.plateau.tapis[1][self.position].valeur,self.plateau.tapis[1][self.position].couleur),
                             Carte(self.plateau.tapis[2][self.position].valeur,self.plateau.tapis[2][self.position].couleur))
        self.g2=GroupeCartes(Carte(self.plateau.tapis[4][self.position].valeur,self.plateau.tapis[4][self.position].couleur),
                             Carte(self.plateau.tapis[5][self.position].valeur,self.plateau.tapis[5][self.position].couleur),
                             Carte(self.plateau.tapis[6][self.position].valeur,self.plateau.tapis[6][self.position].couleur))