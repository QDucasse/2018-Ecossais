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
        
    def rafraichissementIntegral(self):
        '''
        Rafraîchissement de l'intégralité des bornes.
        A utiliser après une action.  
        !!!Peut être amélioré si on choisit de rafraîchir seulement 
        !!!la borne qui a changé
        
        Paramètres
        ---------- 
        '''
        self.borne1.rafraichir        
        self.borne2.rafraichir    
        self.borne3.rafraichir    
        self.borne4.rafraichir    
        self.borne5.rafraichir    
        self.borne6.rafraichir    
        self.borne7.rafraichir    
        self.borne8.rafraichir    
        self.borne9.rafraichir    
    
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
        True ou False
        '''
        etatBornes=self.plateau.tapis[3][:]
        
        #Condition 1
        if etatBornes.count('J1')==5:
            return (True,'VJ1')
        elif etatBornes.count('J2')==5:
            return (True,'VJ2')
        
        #Condition 2
        #On sauvegarde dans un dictionnaire le maximum d'occurences successives de 'J1' ou 'J2'
#        res = {}
#        curseur = etatBornes[0]
#        compt = 0
#        for val in etatBornes:
#            if val == curseur:
#                compt += 1
#            else:
#                res[curseur]=compt
#                curseur = val
#                compt = 1
#        res[curseur]=compt
        
        #Puis vérification condition 2
#        if res['J1']>=3:
#            return (True,'VJ1')
#        elif res['J2']>=3:
#            return (True,'VJ2')
        
        
    
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
        
        no_carte= eval(input('J{0}, sélectionnez une carte (par son numéro de 1 à 6 \n'.format(self.joueurCourant))) -1
        position= eval(input('Sélectionnez la position visée sous la forme (x,y) \n'))
        if self.joueurCourant==1:
            while not self.J1.peutJouer(position):
                #On vérifie que le joueur peut bien jouer à l'endroit sélectionné 
                #et dans le cas contraire, on lui redemande une position
                position= eval(input('Sélectionnez une position valable \n'))    
            else:
                self.J1.jouer(no_carte,position)
       
        else:
            while not self.J1.peutJouer():
                position= eval(input('Sélectionnez une position valable \n'))    
            else:
                self.J2.jouer(no_carte,position)
        
        
        
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
    while not j.testVictoire()[0]:
        j.unTour()
    else:
        print(j.testVictoire()[1])
        
 
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        