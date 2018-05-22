
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 15:46:45 2018

@author: quentin

"""

from random import shuffle
from IA_0 import IA_0
from IA_1 import IA_1
from IA_2 import IA_2
from IA_3 import IA_3
from joueur import Joueur
from carte import Carte
from plateau import Plateau
from groupeCartes import GroupeCartes
from borne import Borne
import numpy.random as rnd  
import numpy as np 
from time import sleep
import matplotlib.pyplot as plt
import time
import datetime
import pickle


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
            s='\n\n{0} tours se sont écoulés, c\'est au joueur {1} de jouer, il reste {2} cartes dans la pioche \n\n'.format(self.nbTours,self.joueurCourant,len(self.pioche))
#            s=s+'Probabilités pour ce tour (joueur {0}):\n\n'.format(self.joueurCourant)
#            num = self.joueurCourant
#            s=s+str(self.proba(num))
#            s=s+'\n\n'                     A DECOMMENTER POUR AVOIR L'AFFICHAGE DES PROBABILITES AVANT LE PLATEAU
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


    
    def proba2(self, no_IA):
        '''
        Calcule les probabilités (égale à 1 si la carte est déjà dans la main) d'obtenir chacune des cartes du jeu entre le tour en cours et la fin du jeu. L'intérêt est de récupérer par traitement simple les probabilités d'obtenir une couleur ou une valeur donnée. Les probabilités sont regroupées sous forme d'un tableau (SANS les en-têtes  indiquant les lignes et colonnes):
            
             | 1 2 3 4 5 6 7 8 9
            _|_________________
            A| X X X X X X X X X
            B| X X X X X X X X X 
            C| X X X X X X X X X
            D| X X X X X X X X X 
            E| X X X X X X X X X
            F| X X X X X X X X X
        
        Paramètre
        ----------
        Le numéro de joueur de l'IA pour laquelle on veut les probabilités.
        '''
        probaChart = np.zeros((6,9))
        listeCouleurs = ['A','B','C','D','E','F']
        tapisStr = [[str(self.plateau.tapis[i][j]) for j in range(len(self.plateau.tapis[0]))] for i in range(len(self.plateau.tapis))]
        mainJ1 = [str(self.J1[i]) for i in range(len(self.J1))]
        mainJ2 = [str(self.J2[i]) for i in range(len(self.J2))]
        
        for valeur in range(1,10):
            for color in range(6):
                cartePosee = False
                couleur = listeCouleurs[color]
                
                for ligne in range(7):
                    if '%c%i'%(couleur,valeur) in tapisStr[ligne]:     #La carte est posée sur le plateau
                        probaChart[color, valeur-1] = 0
                        cartePosee = True
                
                if no_IA == 1 and '%c%i'%(couleur,valeur) in mainJ1:
                    probaChart[color, valeur-1] = 1
                
                elif no_IA == 2 and '%c%i'%(couleur,valeur) in mainJ2:
                    probaChart[color, valeur-1] = 1
                    
                elif  not cartePosee and len(self.pioche) != 0:
                    proba = 0
                    prod = 1                    #probabilité d'intersection de non-sortie de la carte
                    P = 2*self.nbTours + self.joueurCourant    #numéro du piochage
                    N = 42                      #nombre initial de cartes  dans la pioche
                    
                    if no_IA == 1:              
                        proba = 1/(len(self.J1)+N-(P-1))       #proba de piocher la carte à ce tour
                        
                        for k in range(int((P+1)/2), int(N/2)): #sommation des probas de piocher la carte 
                            prod = 1                            #à un tour ultérieur
                            
                            for i in range(P, 1+2*k):           #le produit des probabilités de ne pas la
                                prod = prod*(1 - 1/(len(self.J2)+N+1-i)) #piocher entre ce tour et le tour 
                                                                         #ultérieur où on la pioche
                            proba += prod*(1/(len(self.J2)+N+1-(2*k+1)))
                        
                        
                    elif no_IA == 2:                                     # de même pour J2
                        proba = 1/(len(self.J1)+N-(P-1))
                        
                        for k in range(int(1+P/2), int(1+N/2)):
                            prod = 1
                            
                            for i in range(P, 2*k):
                                prod = prod*(1 - 1/(len(self.J2)+N+1-i))
                                
                            proba += prod*(1/(len(self.J2)+N+1-(2*k))) 
                            
                        
                    probaChart[color, valeur-1] = proba          #on recense les valeurs dans un tableau
                                                                 #pour les récupérer facilement après
                elif len(self.pioche) == 0:
                    probaChart[color, valeur-1] = 0
        
        return probaChart
                    
   
    def proba(self, no_IA):
#        global p11
#        global p22
#        global t
        '''
        Calcule les probabilités (égale à 1 si la carte est déjà dans la main) d'obtenir chacune des cartes du jeu entre le tour en cours et la fin du jeu. L'intérêt est de récupérer par traitement simple les probabilités d'obtenir une couleur ou une valeur donnée. Les probabilités sont regroupées sous forme d'un tableau (SANS les en-têtes  indiquant les lignes et colonnes):
            
             | 1 2 3 4 5 6 7 8 9
            _|_________________
            A| X X X X X X X X X
            B| X X X X X X X X X 
            C| X X X X X X X X X
            D| X X X X X X X X X 
            E| X X X X X X X X X
            F| X X X X X X X X X
        
        Paramètre
        ----------
        Le numéro de joueur de l'IA pour laquelle on veut les probabilités.
        '''
        probaChart = np.zeros((6,9))
        listeCouleurs = ['A','B','C','D','E','F']
        tapisStr = [[str(self.plateau.tapis[i][j]) for j in range(len(self.plateau.tapis[0]))] for i in range(len(self.plateau.tapis))]
        mainJ1 = [str(self.J1[i]) for i in range(len(self.J1))]
        mainJ2 = [str(self.J2[i]) for i in range(len(self.J2))]
        
        for valeur in range(1,10):
            for color in range(6):
                cartePosee = False
                couleur = listeCouleurs[color]
                
                for ligne in range(7):
                    if '%c%i'%(couleur,valeur) in tapisStr[ligne]:     #La carte est posée sur le plateau
                        probaChart[color, valeur-1] = 0
                        cartePosee = True
                
                if no_IA == 1 and '%c%i'%(couleur,valeur) in mainJ1:
                    probaChart[color, valeur-1] = 1
                
                elif no_IA == 2 and '%c%i'%(couleur,valeur) in mainJ2:
                    probaChart[color, valeur-1] = 1
                    
                elif  not cartePosee and len(self.pioche) != 0:
                    
                    proba = (len(self.pioche)+(no_IA+1)%2)/(2*(len(self.pioche)+6))
#                    if no_IA == 1:
#                        p11[t] = proba            #listes pour débug
#                    elif no_IA == 2:
#                        p22[t] = proba
                    
                    # pour J1, il reste N = len(pioche)/2 piochages
                    # pour J2, il reste N = (len(pioche)+1)/2 piochages
                    # La probabilité de tirer une carte que l'on suppose non tirée jusque-là
                    # est de N/Total des cartes inconnues.
                    # Tirages sans remises.
                    
                    
                    probaChart[color, valeur-1] = proba          #on recense les valeurs dans un tableau
                                                                 #pour les récupérer facilement après
                elif len(self.pioche) == 0:
                    probaChart[color, valeur-1] = 0
#        if no_IA == 2:
#            t+=1
        return probaChart
                    
   
    
    def joueurCourant(self):
        '''
        Rend le joueur courant
        
        Paramètres
        ----------
        Aucun
        '''
        if self.joueurCourant == 1:
            return self.J1
        else:
            return self.J2


     
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
        
        
        
    def unTourPvIA(self,IHM=False):
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
        
        if self.joueurCourant==1 and not IHM:
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

        sleep(0.1)

        self.tourSuivant()
        
        

####### Sauvegarde et Chargement ########################

    def save(self):
        '''
        Sauvegarde du jeu en cours dans le fichier saves où le nom est formaté avec la date et heure courante
        
        Paramètres
        ----------
        Aucun
        '''
        now = datetime.datetime.now()
        fichier = open('saves/sauvegarde_{0}'.format(now),'wb')
        pickler = pickle.Pickler(fichier)
        pickler.dump(self.ensembleBorne)
        pickler.dump(self.J1)
        pickler.dump(self.J2)
        pickler.dump(self.joueurCourant)
        pickler.dump(self.nbTours)
        pickler.dump(self.pioche)
        pickler.dump(self.plateau)
        fichier.close()
    
    def saveIHM(self):
        '''
        Le chemin change pour l'IHM mais la fonction reste la même
        
        Paramètres
        ----------
        Aucun
        '''
        now = datetime.datetime.now()
        fichier = open('../src/saves/sauvegarde_{0}'.format(now),'wb')
        pickler = pickle.Pickler(fichier)
        pickler.dump(self.ensembleBorne)
        pickler.dump(self.J1)
        pickler.dump(self.J2)
        pickler.dump(self.joueurCourant)
        pickler.dump(self.nbTours)
        pickler.dump(self.pioche)
        pickler.dump(self.plateau)
        fichier.close()  
        
    def loadAndPlay(self,fichier):
        '''
        Charge un fichier situé dans saves/fichier par exemple
        
        Paramètres
        ----------
        Le chemin menant au fichier souhaité
        '''
        fichierOuvert = open(fichier,'rb')
        depickler = pickle.Unpickler(fichierOuvert)
        self.ensembleBorne = depickler.load()
        self.borne1 = self.ensembleBorne[0]
        self.borne1 = self.ensembleBorne[1]
        self.borne1 = self.ensembleBorne[2]
        self.borne1 = self.ensembleBorne[3]
        self.borne1 = self.ensembleBorne[4]
        self.borne1 = self.ensembleBorne[5]
        self.borne1 = self.ensembleBorne[6]
        self.borne1 = self.ensembleBorne[7]
        self.borne1 = self.ensembleBorne[8]
        self.J1 = depickler.load()
        self.J2 = depickler.load()
        self.JoueurCourant = depickler.load()
        self.nbTours = depickler.load()
        self.pioche = depickler.load()
        self.plateau = depickler.load()
        self.startWithLoad()
        fichierOuvert.close()
        
        
        
        
############# Fonction de départ pour l'interface dans la console Python #####################

    def start(self, test = False):
        global T1, T2
        '''
        Lance une partie entre différents joueurs
        
        Paramètres
        ----------
        test : True ou False 
        Permet de choisir si on veut lancer une partie ou une simulation de plusieurs combats d'IA
        '''
        print('Écossais Bagarreurs ! \nLe jeu oppose deux joueurs avec les règles de base de Shotten Totten.\nLe côté du joueur 1 est en haut du plateau, celui du joueur 2 en bas')
        if not test:
            mode=input('Sélectionnez votre mode de jeu: \nH pour Humain contre Humain \nou I contre une IA \nou II pour l\'opposition de deux IA\n\n')
            if mode=='H':
                self.startPvP()
            ### PAREIL, IL FAUT FAIRE UNE FONCTION STARTPVP STARTPVIA ET STARTIAVIA
            elif mode=='I':

                niveau=input('Sélectionnez le niveau de votre adversaire: \n0 = Aleatoire \n1 = Groupements brelans\n')
                self.startPvIA(niveau)


            elif mode=='II':    #On sélectionne les niveaux des deux IA et on initialise la partie
                niveau1=input('Sélectionnez le niveau de l\'IA Joueur 1: \n0 = Aleatoire \n1 = Peuples de qualité \n2 = Groupements brelans \n3 = Stratégie et probabilités\n')
                niveau2=input('Sélectionnez le niveau de l\'IA Joueur 2: \n0 = Aleatoire \n1 = Peuples de qualité \n2 = Groupements brelans \n3 = Stratégie et probabilités\n') 
                self.startIAvIA(niveau1,niveau2)
        
        if test:
            self.J1 = IA_0(6,1,self)
            self.J2 = IA_1(6,2,self)
            self.installation()
            
    
            while self.J2!=[] and (not self.testVictoire()[0]):  #Le jeu s'arrête quand J2 n'a plus de carte
                self.unTourIAvIA()
            if self.testVictoire()[1] == 'J1':
                T1 += 1
            if self.testVictoire()[1] == 'J2':
                T2 += 1        
            
        print("\n\n\n", self)
        print("\nVICTOIRE DU JOUEUR ", self.testVictoire()[1], " !!!\n\n\n")


############## Redéfinition et spécification de la fonction start() pour différents cas (IHM) ###############

    def installation(self):
        '''
        Distribue les cartes aux différents joueurs
        
        Paramètres
        ----------
        Aucun
        '''
        for i in range(self.J1.taille):
                    self.J1.piocher()
                    self.J2.piocher()
                               
    def startPvP(self,load=False):
        '''
        Lance le jeu en mode PvP
        
        Paramètres
        ----------
        Aucun
        '''
        if not load:
            self.installation()
        while self.J2!=[] and (not self.testVictoire()[0]):  #Le jeu s'arrête quand J2 n'a plus de carte
             self.unTourPvP()
        
    def startPvIA(self,niveau,load=False,IHM=False):
        '''
        Lance le jeu en mode PvIA
        
        Paramètres
        ----------
        Niveau de l'IA
        '''
        if niveau=='0':
            self.J2=IA_0(6,2,self)
        
        elif niveau=='1':
            self.J2=IA_1(6,2,self)
        
        elif niveau=='2':
            self.J2=IA_2(6,2,self)
        
        elif niveau=='3':
            self.J2=IA_3(6,2,self)
        
        if not load:
            self.installation()
            
        while self.J2!=[] and (not self.testVictoire()[0]):  
             self.unTourPvIA(IHM)
        
    def startIAvIA(self,niveau1,niveau2,load=False):
        '''
        Lance le jeu en mode IAvIA
        
        Paramètres
        ----------
        Niveaux des deux IA
        '''
        if niveau1=='0':
            self.J1 = IA_0(6,1,self)
        if niveau1=='1':
            self.J1 = IA_1(6,1,self)
        if niveau1=='2':
            self.J1 = IA_2(6,2,self)
        if niveau1=='3':
            self.J1 = IA_3(6,2,self)
            
        if niveau2=='0':
            self.J2 = IA_0(6,2,self)
        if niveau2=='1':
            self.J2 = IA_1(6,2,self)
        if niveau2=='2':
            self.J2 = IA_2(6,2,self)            
        if niveau2=='3':
            self.J2 = IA_3(6,2,self)
            
        if not load:
            self.installation()

        while self.J2!=[] and (not self.testVictoire()[0]):  #Le jeu s'arrête quand J2 n'a plus de carte
            self.unTourIAvIA()
        else:
            print(self.testVictoire()[1])
    def startWithLoad(self):
        '''
        La fonction start utilisée après la mise en place du jeu par la fonction loadAndPlay()
        /!\ A lancer après le load
        
        Paramètres
        ----------
        Aucun
        '''
        print('Reprise de la partie en cours')
        if type(self.J1) == Joueur:
            if type(self.J2) == Joueur:
                self.startPvP(load=True)
            else:
                self.startPvIA(self.J2.niveau,load=True)
        else:
            self.startIAvIA(self.J1.niveau,self.J2.niveau,load=True)
        
        
            
            
if __name__=='__main__':
    game=Jeu()
    game.start(False)

    global T1, T2
    T1 = 0
    T2 = 0
#    for k in range(50):
#        game=Jeu()
#        game.start(True)
#    print("Victoires J1 :", 100*T1/(T1+T2), '%')


