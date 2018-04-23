
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 15:46:45 2018

@author: quentin
"""

from random import shuffle
from IA_0 import IA_0
from IA_1 import IA_1
from joueur import Joueur
from carte import Carte
from plateau import Plateau
from groupeCartes import GroupeCartes
from borne import Borne
import numpy.random as rnd   
from time import sleep
    
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
        self.coupsJoues=0
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
        if self.testVictoire()[0] and self.joueurCourant == 1:
            s = 'Et c\'est fini :\n\n'+ str(self.plateau)
        
        else:
            s='\n\n{0} tours se sont écoulés, c\'est au joueur {1} de jouer, il reste {2} cartes dans la pioche \n'.format(self.nbTours,self.joueurCourant,len(self.pioche))
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
        True ou False ainsi que Ji avec i le numéro du joueur gagnant
        '''
        etatBornes=self.plateau.tapis[3][:] #La liste des bornes du plateau
        
        #Condition 1: 5 bornes en tout
        if etatBornes.count('J1')==5:
            return (True,'J1')
        elif etatBornes.count('J2')==5:
            return (True,'J2')
        else:
            for i in range(7):
                #condition 2: 3 bornes successives
                if etatBornes[i:i+3]==['J1','J1','J1']:
                    return (True,'J1') 
                elif etatBornes[i:i+3]==['J2','J2','J2']:
                    return (True,'J2')
                if i==6:
                    return (False,'XX')





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
        
        self.nbTours=self.nbTours + (self.coupsJoues%2)
        self.coupsJoues = self.coupsJoues+1




    def bonNumeroCarte(self,no_carte):
        '''
        Vérifie que le numéro correspond bien à une carte
        '''
        return (no_carte<=len(self.J2)-1 and no_carte>=0)



        
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
        
        if not(self.joueurCourant == 1 and self.testVictoire()[0]):
            print(self)
            if self.joueurCourant==1:
                print(self.J1)
            else:
                print(self.J2)
        
        ######### On demande au joueur de sélectionner sa carte et la position visée #########
        
        no_carte= eval(input('J{0}, sélectionnez une carte (par son numéro de 1 à 6) \n'.format(self.joueurCourant))) -1
        while not self.bonNumeroCarte(no_carte):
            no_carte= eval(input('Sélectionnez un numéro de carte valable \n')) -1
        no_borne = eval(input('Sélectionnez la borne visée (par son numéro de 1 à 9) \n'))-1
        if self.joueurCourant==1:
            while not self.J1.peutJouer(no_borne):
                #On vérifie que le joueur peut bien jouer à l'endroit sélectionné 
                #et dans le cas contraire, on lui redemande une position
                no_borne= eval(input('Sélectionnez une position valable \n')) -1  
            else:
                self.J1.jouer(no_carte,no_borne)
       
        else:
            while not self.J2.peutJouer(no_borne):
                no_borne= eval(input('Sélectionnez une position valable \n'))    
            else:
                self.J2.jouer(no_carte,no_borne)
    
    ###CETTE PARTIE PEUT ÊTRE EXTRAITE EN TANT QUE METHODE A PART
    
        self.rafraichissementIntegral()
        
        ######### Changement de joueur et incrémentation du tour #############################
        
        self.tourSuivant()
        
        
        
    def unTourPvIA(self):
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
        
        ######### On demande au joueur de sélectionner sa carte et la position visée #########
        if self.joueurCourant==1:
            no_carte= eval(input('J{0}, sélectionnez une carte (par son numéro de 1 à 6) \n'.format(self.joueurCourant))) -1
            while not self.bonNumeroCarte(no_carte):
                no_carte= eval(input('Sélectionnez un numéro de carte valable \n')) -1
            no_borne = eval(input('Sélectionnez la borne visée (par son numéro de 1 à 9) \n')) -1
            while not self.J1.peutJouer(no_borne):
                #On vérifie que le joueur peut bien jouer à l'endroit sélectionné 
                #et dans le cas contraire, on lui redemande une position
                no_borne= eval(input('Sélectionnez une position valable \n')) -1 
            else:
                self.J1.jouer(no_carte,no_borne)
            
        elif self.joueurCourant==2:
            self.J2.jouer()
            
    ###CETTE PARTIE PEUT ÊTRE EXTRAITE EN TANT QUE METHODE A PART
    
        self.rafraichissementIntegral()
        
        ######### Changement de joueur et incrémentation du tour #############################
        
        self.tourSuivant()
        



    def unTourIAvIA(self):
        '''
        Fait progresser chacune des actions d'une case et donne la main à l'une des IA :
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
        if self.joueurCourant==2:
            print(self.J2)
        
        ######### L'IA en cours choisit sa carte et la position visée #########
        if self.joueurCourant==1:
            self.J1.jouer(1)
            
        elif self.joueurCourant==2:
            self.J2.jouer(2)
    
        self.rafraichissementIntegral()
        
        ######### Changement de joueur et incrémentation du tour #############################
        #sleep(0.1)
        self.tourSuivant()






    def start(self):
        '''
        Lance une partie entre différents joueurs
        
        Paramètres
        ----------
        Aucun
        '''
        print('Écossais Bagarreurs ! \nLe jeu oppose deux joueurs avec les règles de base de Shotten Totten.\nLe côté du joueur 1 est en haut du plateau, celui du joueur 2 en bas')
        mode=input('Sélectionnez votre mode de jeu: \nH pour Humain contre Humain \nou I contre une IA \nou II pour l\'opposition de deux IA\n\n')
        if mode=='H':
            for i in range(self.J1.taille):
                self.J1.piocher()
                self.J2.piocher()
            while self.J2!=[] and (not self.testVictoire()[0]):  #Le jeu s'arrête quand J2 n'a plus de carte
                 self.unTourPvP()
        ### PAREIL, IL FAUT FAIRE UNE FONCTION STARTPVP STARTPVIA ET STARTIAVIA
        elif mode=='I':
            niveau=input('Sélectionnez le niveau de votre adversaire: \n0 = Aleatoire \n1 = Groupements brelans\n')
            
            if niveau=='0':
                self.J2=IA_0(6,2,self)
                for i in range(self.J1.taille):
                    self.J1.piocher()
                    self.J2.piocher()
                while self.J2!=[] and (not self.testVictoire()[0]):
                     self.unTourPvIA()
            
            if niveau=='1':
                self.J2=IA_1(6,2,self)
                for i in range(self.J1.taille):
                    self.J1.piocher()
                    self.J2.piocher()
                while self.J2!=[] and (not self.testVictoire()[0]):  
                     self.unTourPvIA()


        elif mode=='II':    #On sélectionne les niveaux des deux IA et on initialise la partie
            niveau1=input('Sélectionnez le niveau de l\'IA Joueur 1: \n0 = Aleatoire \n1 = Groupements brelans\n')
            niveau2=input('Sélectionnez le niveau de l\'IA Joueur 2: \n0 = Aleatoire \n1 = Groupements brelans\n')
            if niveau1=='0':
                self.J1 = IA_0(6,2,self)
            if niveau1=='1':
                self.J1 = IA_1(6,2,self)
            if niveau2=='0':
                self.J2 = IA_0(6,2,self)
            if niveau2=='1':
                self.J2 = IA_1(6,2,self)
                
            for i in range(self.J1.taille):
                    self.J1.piocher()
                    self.J2.piocher()
            while self.J2!=[] and not (self.joueurCourant == 1 and self.testVictoire()[0]):  #Le jeu s'arrête quand J2 n'a plus de carte ou que l'un des deux a gagné lors de la fin du tour
                 self.unTourIAvIA()
        
        print("\n\n\n", self)
        print("\nVICTOIRE DU JOUEUR ", self.testVictoire()[1], " !!!")



if __name__=='__main__':
    j=Jeu()
    j.start()
