#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 15:46:45 2018

@author: ducassqu
"""
from random import shuffle

from joueur import Joueur
from carte import Carte
from plateau import Plateau
from groupeCartes import GroupeCartes
from borne import Borne
    
    
class Jeu():
    
    
    def __init__(self):
        ''' 
        Crée une partie.
        
        Paramètres
        ----------
        Aucun

        '''
        self.plateau=Plateau(9)
        self.J1=Joueur(6,1,self)
        self.J2=Joueur(6,2,self)
        self.nbTours=0
        self.joueurCourant=1
        
        #Initialisation des bornes
        self.borne1=Borne(0,self.plateau)        
        self.borne2=Borne(1,self.plateau) 
        self.borne3=Borne(2,self.plateau) 
        self.borne4=Borne(3,self.plateau) 
        self.borne5=Borne(4,self.plateau) 
        self.borne6=Borne(5,self.plateau) 
        self.borne7=Borne(6,self.plateau) 
        self.borne8=Borne(7,self.plateau) 
        self.borne9=Borne(8,self.plateau) 
        self.ensembleBorne=[self.borne1,self.borne2,self.borne3,self.borne4,self.borne5,self.borne6,self.borne7,self.borne8,self.borne9]
        
        #Initialisation et mise en place de la pioche
        self.pioche=[] 
        for i in range(9):
            for couleur in ['A','B','C','D','E','F']:
                self.pioche.append('%c%i'%(couleur,i+1))
        shuffle(self.pioche)
        self.pioche=list(set(self.pioche))
        
        
    def __str__(self):
        '''
        Affiche le nombre de tours, le joueur courant, le nombre de cartes dans la pioche et la main du joueur en cours
        
        Paramètres
        ----------
        Aucun
        
        Renvoie
        -------
        s: str
            La chaîne de caractères qui sera affichée via ''print''
        '''
        
        s='{0} tours se sont écoulés, c\'est au joueur {1} de jouer, il reste {2} cartes dans la pioche \n'.format(self.nbTours,self.joueurCourant,len(self.pioche))
        s=s+str(self.plateau)
        return s
        
    def rafraichissementIntegral(self):
        '''
        Rafraîchissement de l'intégralité des bornes.
        A utiliser après une action.  
        !!!Peut être amélioré si on choisit de rafraîchir seulement 
        !!!la borne qui a changé
        
        Paramètres
        ----------
        Aucun
        '''
        self.borne1.rafraichir()        
        self.borne2.rafraichir()    
        self.borne3.rafraichir()    
        self.borne4.rafraichir()    
        self.borne5.rafraichir()    
        self.borne6.rafraichir()    
        self.borne7.rafraichir()    
        self.borne8.rafraichir()    
        self.borne9.rafraichir()    
    
    def testVictoire(self):
        '''
        Vérification de la victoire d'un des joueurs suivant les deux conditions suivantes:
            Un joueur possède trois bornes consécutives
            Un joueur possède cinq bornes en tout
        
        Paramètres
        ----------
        Aucun
        
        Renvoie
        -------
        True ou False ainsi que VJi avec i le numéro du joueur gagnant
        '''
        etatBornes=self.plateau.tapis[3][:] #La liste des bornes du plateau
        
        #Condition 1: 5 bornes en tout
        if etatBornes.count('J1')==5:
            return (True,'VJ1')
        elif etatBornes.count('J2')==5:
            return (True,'VJ2')
        else:
            for i in range(7):
                #condition 2: 3 bornes successives
                if etatBornes[i:i+3]==['J1','J1','J1']:
                    return (True,'VJ1') 
                elif etatBornes[i:i+3]==['J2','J2','J2']:
                    return (True,'VJ2')
      
        
    
    def tourSuivant(self):
        '''
        Change le compteur de tour et le joueur courant
        
        Paramètres
        ----------
        Aucun
        '''
        if self.joueurCourant==1:
            self.joueurCourant=2
        else:
            self.joueurCourant=1
        self.nbTours=self.nbTours+1
        
        
    def unTourPvP(self):
        '''
        Fait progresser chacune des actions d'une case et donne la main à un des joueurs :
            L'état du jeu s'affiche
            Le joueur en question joue une carte (place + pioche)
            Le nombre de tours s'incrémente
        
        Paramètres
        ----------
        Aucun
        '''
        ######### Affichage du jeu et du la main du joueur ####################################
        
        print(self)
        if self.joueurCourant==1:
            print(self.J1)
        else:
            print(self.J2)
        
        ######### On demande au joueur de sélectionner sa carte et la position visée #########
        
        no_carte= eval(input('J{0}, sélectionnez une carte (par son numéro de 1 à 6) \n'.format(self.joueurCourant))) -1
        position= eval(input('Sélectionnez la position visée sous la forme (x,y) \n'))
        if self.joueurCourant==1:
            while not self.J1.peutJouer(position):
                #On vérifie que le joueur peut bien jouer à l'endroit sélectionné 
                #et dans le cas contraire, on lui redemande une position
                position= eval(input('Sélectionnez une position valable \n'))    
            else:
                self.J1.jouer(no_carte,position)
       
        else:
            while not self.J2.peutJouer(position):
                position= eval(input('Sélectionnez une position valable \n'))    
            else:
                self.J2.jouer(no_carte,position)
        
        self.rafraichissementIntegral()
        
        ######### Changement de joueur et incrémentation du tour #############################
        
        self.tourSuivant()
        
        
        
    def start(self):
        '''
        Lance une partie entre différents joueurs
        
        Paramètres
        ----------
        Aucun
        '''
        print('Écossais Bagarreurs ! \nLe jeu oppose deux joueurs avec les règles de base de Shotten Totten.\nLe côté du joueur 1 est en haut du plateau, celui du joueur 2 en bas')
        mode=input('Sélectionnez votre mode de jeu: \nH pour Humain contre Humain ou I contre une IA \n')
        if mode=='H':
            for i in range(self.J1.taille):
                self.J1.piocher()
                self.J2.piocher()
            while (self.J1!=[] and self.J2!=[]) or (not self.testVictoire()[0]):
                 self.unTourPvP()
#        elif mode=='I':
#            self.J2=IA(blablabla)
        
        
if __name__=='__main__':
    j=Jeu()
    j.start()