#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 15:46:45 2018

@author: ducassqu
"""
from random import shuffle


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
        self[no_carte].position=str(position)
        del(self[no_carte])
    
    def piocher(self):
        '''
        Pioche la première carte de la pioche et l'ajoute à la main du joueur
        
        Paramètres
        ----------
        Aucun
        '''
        self.append(Carte(self.jeu.pioche.pop()[1],self.jeu.pioche.pop()[0],'MainJoueur{0}'.format(self.numero)))



class Carte():
    
    
    def __init__(self,valeur,couleur,position):
        ''' 
        Crée une carte donnée.
        
        Paramètres
        ----------
        Valeur de la carte
        Couleur de la carte
        Position de la carte

        '''
        self.valeur=valeur
        self.couleur=couleur
        self.position=position
    
    
    def __str__(self):
        '''
        Affiche le code de la carte 'CouleurValeur'.
        
        Paramètres
        ----------
        Aucun
        
        Renvoie
        -------
        s: str
            La chaîne de caractères qui sera affichée via ''print''
            
        '''
        
        return '{0}{1}'.format(self.couleur,self.valeur)

    
class Plateau():
    
#    
#    def __new__(cls,nb_bornes):
#        plateau = super(Plateau, cls).__new__(cls, (9, nb_bornes))
#        return plateau
#    
#    
#    def __init__(self, nb_bornes):
#        ''' 
#        Crée un plateau de taille donnée.
#        
#        Paramètres
#        ----------
#        Nombre de bornes
#
#        '''
#        self.nb_bornes = nb_bornes
#        self.tapis = np.array([['CC']*nb_bornes]*7, dtype=str)
#        self.tapis[3] = ['B ']*nb_bornes 

      
    def __init__(self,nb_bornes):
         ''' 
         Crée un plateau de taille donnée.
         
         Paramètres
         ----------
         Nombre de bornes

         '''
         self.taille=nb_bornes
         self.tapis=[]
         for i in range(7):
             self.tapis.append(['  ']*nb_bornes)
         self.tapis[3]=['XX','XX','XX','XX','XX','XX','XX','XX','XX']
         
         
    def __str__(self):
        ''' 
        Affiche le plateau de jeu.
        
        Paramètres
        ----------
        Self

        '''
        s=''
        for ligne in self.tapis:
            s=s+str(ligne)+'\n'
        return s
       


#    def testVictoire(self):
        
        
    
class Borne():
    
    
    def __init__(self,g1,g2,pos):
        ''' 
        Crée une borne séparant les groupes de cartes g1 et g2.
        
        Paramètres
        ----------
        Groupe de cartes 1: g1
        Groupe de cartes 2: g2

        '''
        self.g1=g1              # le groupe de cartes du côté du joueur 1
        self.g2=g2              # le groupe de cartes du côté du joueur 2
        self.position=pos       # la position de la borne sur le plateau
        self.premierComplete=0  # conserve  1 ou 2 correspondant au côté du joueur ayant fini en premier
        self.gagnant= ' '
     
        
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
        # Première condition de victoire via la force
        if self.g1.force>self.g2.force:
            self.gagnant= 'J1'
        elif self.g2.force>self.g1.force:
            self.gagnant= 'J2'
        else:
            # En cas d'égalité, on compare le total de points 
            if self.g1.totalPoints>self.g2.totalPoints:
                self.gagnant= 'J1'
            elif self.g2.totalPoints>self.g1.totalPoints:
                self.gagnant= 'J2'
            else:
                # Enfin, en cas d'égalité à nouveau, le premier à avoir complété don côté gagne
                self.gagnant= 'J{0}'.format(self.premierComplete)
                
          
            
class GroupeCartes():
    
    
    def __init__(self,C1=Carte(0,'  ','Vide'),C2=Carte(0,'  ','Vide'),C3=Carte(0,'  ','Vide')):
        # On définit Carte(0,'X','Vide) comme un emplacement vide
        ''' 
        Crée un groupe de 3 cartes, la carte vide étant Carte(0,'X','Vide') .
        
        Paramètres
        ----------
        Les 3 cartes qui composent le groupe

        '''
        self.C1 = C1
        self.C2 = C2
        self.C3 = C3
        self.totalPoints = C1.valeur + C2.valeur + C3.valeur
        self.force = 0
    
    
    def calculForce(self): 
        ''' 
        Calcule la force d'un groupe de cartes comme suit :
            5 = Force max, le groupe se constitue de 3 cartes de même couleur dont les valeurs sont consécutives
            4 = 3 cartes de même valeur 
            3 = 3 cartes de même couleur 
            2 = 3 cartes dont les valeurs sont consécutives
            1 = 3 cartes sans lien apparent
            
        Paramètres
        ----------
        Aucun

        '''
        if (self.C1.valeur==0) or (self.C2.valeur==0) or (self.C3.valeur==0):
            self.force=0
            #Ce cas correspond à l'absence d'une des 3 cartes
        
        else:
             l=[self.C1.valeur,self.C2.valeur,self.C3.valeur]
             if ((self.C1.couleur==self.C2.couleur) and (self.C2.couleur==self.C3.couleur)) and (min(l)==max(l)-2):
                 self.force=5
                 #On vérifie que les cartes sont de la même couleur et forment une suite
             elif (self.C1.valeur==self.C2.valeur) and (self.C2.valeur==self.C3.valeur):   
                 self.force=4
                 #On vérifie que les cartes sont de la même valeur 
             elif (self.C1.couleur==self.C2.couleur) and (self.C2.couleur==self.C3.couleur):
                 self.force=3
                 #On vérifie que les cartes sont de la même couleur 
             elif (min(l)==max(l)-2) and (l.count(min(l))==1) and (l.count(max(l))==1):
                 self.force=2
                 #On vérifie que les cartes forment une suite
             else:
                 self.force=1
                 
    
    
class Jeu():
    
    
    def __init__(self,plateau=Plateau(9)):
        ''' 
        Crée une partie.
        
        Paramètres
        ----------
        Aucun

        '''
        self.plateau=plateau
        self.J1=Joueur(6,1,self.plateau,self)
        self.J2=Joueur(6,2,self.plateau,self)
        self.nbTours=0
        self.joueurCourant=1
        
        #Initialisation et mise en place de la pioche
        self.pioche=[] 
        for i in range(9):
            for couleur in ['A','B','C','D','E','F']:
                self.pioche.append('%c%i'%(couleur,i+1))
        shuffle(self.pioche)
     
        
    def __str__(self):
        '''
        Affiche le nombre de tours, le joueur courant, le nombre de cartes dans la pioche et la main du joueur en cours
        
        Paramètres
        ----------
        Aucun

        '''
        
        s='{0} tours se sont écoulés, c\'est au joueur {1} de jouer, il reste {2} cartes dans la pioche \n'.format(self.nbTours,self.joueurCourant,len(self.pioche))
        s=s+str(self.plateau)
        return s
        
        
    def unTour(self):
        '''
        Fait progresser chacune des actions d'une case et donne la main à un des joueurs :
            Le joueur en question joue une carte (place + pioche)
            Le résultat de ses actions s'affiche
            Le nombre de tours s'incrémente
        
        Paramètres
        ----------
        Aucun
        '''
        ######### Affichage du jeu au moment de jouer ########################################
        
        print(self)
        if self.joueurCourant==1:
            print(self.J1)
        else:
            print(self.J2)
        
        ######### On demande au joueur de sélectionner sa carte et la position visée #########
        
        no_carte= eval(input('J{0}, sélectionnez une carte (par son numéro de 1 à 6) \n'.format(self.joueurCourant))) 
        position= eval(input('Sélectionnez la position visée sous la forme (x,y) \n'))
        if self.joueurCourant==1:
            self.J1.jouer(no_carte,position)
        else:
            self.J2.jouer(no_carte,position)
        
        ######### Affichage des résultats des actions ########################################
        
        #print(self.plateau)
        
        
        ######### Vérification de la victoire d'un des joueurs !! ############################
        
        
        ######### Changement de joueur et incrémentation du tour #############################
        
        if self.joueurCourant==1:
            self.joueurCourant=2
        else:
            self.joueurCourant=1
        
        self.nbTours=self.nbTours+1
        
        
        
        
        
        
        
        
if __name__=='__main__':
    j=Jeu()
    for i in range(j.J1.taille):
        j.J1.piocher()
        j.J2.piocher()
    for i in range(55):
        j.unTour()
 
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        