# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 17:48:35 2018

@author: Matthieu
"""

from carte import Carte
from plateau import Plateau
from joueur import Joueur
import numpy.random as rnd
import scipy.special as sp

class IA_3(Joueur):
    
    def __init__(self,taille,no,partie):
        super().__init__(taille,no,partie)
        self.niveau = 3
        self.no_carte = -1
        self.no_carte_next = -1
        self.no_carte_next2 = -1
        self.noBorne = -1
    
    
    def jouer(self,no_IA=2):
        '''
        Cette IA favorise l'apparition de suites couleur sur ses borne, avec brelans en cas d'impossibilité ou de mauvaise probabilité.
        Joue une carte de la main d'un joueur 
        Correspond aux actions successives de choisir, placer et piocher pour compléter la main.
        
        
        Paramètres
        ----------
        Numéro de joueur de l'IA (1 ou 2, par défaut 2)
        '''
        self.placer()
        self.piocher()
    

    
    def chercheSuites(self, no_IA):
        '''
        Cette fonction recherche les cartes à poser pour faire apparaitre des 
        suites couleur, soit sur une borne vide mais que l'on peut compléter 
        avec des cartes que l'on a en main ou que l'on a un probabilité>0.3 
        d'obtenir, soit sur une borne où la suite couleur est proche.        
        
        
        Paramètres
        ----------
        Numéro de joueur de l'IA (1 ou 2, par défaut 2)
        
        
        Renvoie
        -------
        [suitesCompletesMain, suitesACompleterMain, suitesSurTapisACompleter]
        
        avec :
            
        suitesCompletesMain : les indices des 3 cartes suite couleur dans la 
        main du joueur triée par ordre croissant de couleur et de valeur
        
        suitesACompleterMain : de meme que precedemment, mais il peut manquer 
        une carte dans la suite couleur (critere probabiliste)
        
        suitesSurTapisACompleter : classee par numero de borne, comporte couleur 
        puis valeurs des cartes necessaires pour completer la suite couleur.
        
        '''
        
        ### on commence par trier la main par couleur puis valeur
        mainClassee = sorted(self, key=lambda card: [card.couleur, card.valeur])
        for i in range(len(self)):
            self[i] = mainClassee[i]
        
        print('\nmainClassee ', self)
        
        [suitesCompletesMain, suitesACompleterMain] = self.chercheSuitesMain(no_IA)
        [suitesSurTapisACompleter, borneQuasiComplete] = self.chercheSuitesTapis(no_IA)
        
        return [suitesCompletesMain, suitesACompleterMain, suitesSurTapisACompleter, borneQuasiComplete]
        
    
    
        
    def chercheSuitesTapis(self, no_IA):
        ### on cherche les débuts de suite déjà sur le tapis (1 ou 2 cartes)
        suitesTap = []
        borneQuasiComplete = [False]*9
        
        for borne in self.jeu.ensembleBorne:
            valPossibles = []
            if no_IA == 1 and borne.g1.C3.couleur != 'X' and (borne.g1.C2.couleur == borne.g1.C3.couleur or borne.g1.C2.couleur == 'X'): 
                difVal = abs(borne.g1.C3.valeur-borne.g1.C2.valeur)
                if not borne.g1.estComplet() and (difVal == borne.g1.C3.valeur or (difVal>0 and difVal<2)): 
                    # on a une ou deux cartes sur la borne, qui rendent possibles une suite
                    valPossibles.append(borne.g1.C3.couleur)
                    
                    if borne.g1.C3.valeur > 1 and borne.g1.C3.valeur < 9 :
                        valPossibles.append(borne.g1.C3.valeur -1)
                        valPossibles.append(borne.g1.C3.valeur +1)
                        
                    if borne.g1.C2.valeur > 1 and borne.g1.C2.valeur < 9 :
                        valPossibles.append(borne.g1.C2.valeur -1)
                        valPossibles.append(borne.g1.C2.valeur +1)
                    
                    if borne.g1.C3.valeur == 1 :
                        valPossibles.append(borne.g1.C3.valeur +1)
                    
                    if borne.g1.C3.valeur == 9 :
                        valPossibles.append(borne.g1.C3.valeur -1)
                    
                    if borne.g1.C2.valeur == 1 :
                        valPossibles.append(borne.g1.C3.valeur +1)
                    
                    if borne.g1.C2.valeur == 9 :
                        valPossibles.append(borne.g1.C3.valeur -1)
                        
                    if borne.g1.C2.couleur == 'X':
                        valPossibles.append(max(0,borne.g1.C3.valeur-2))
                        valPossibles.append(min(borne.g1.C3.valeur+2,9))
                    
                    if borne.g1.C2.couleur != 'X':
                        borneQuasiComplete[borne.position] = True
                    

            if no_IA == 2 and borne.g2.C1.couleur != 'X' and (borne.g2.C2.couleur == borne.g2.C1.couleur or borne.g2.C2.couleur == 'X'): 
                difVal = abs(borne.g2.C1.valeur-borne.g2.C2.valeur)
                if not borne.g2.estComplet() and ((difVal>0 and difVal<2) or difVal==borne.g2.C1.valeur) :    
                    # on a une ou deux cartes sur la borne, qui rendent possibles une suite
                    valPossibles.append(borne.g2.C1.couleur)
                    
                    if borne.g2.C1.valeur > 0 and borne.g2.C1.valeur < 9 :
                        valPossibles.append(borne.g2.C1.valeur -1)
                        valPossibles.append(borne.g2.C1.valeur +1)
                        
                    if borne.g2.C2.valeur > 0 and borne.g2.C2.valeur < 9 :
                        valPossibles.append(borne.g2.C2.valeur -1)
                        valPossibles.append(borne.g2.C2.valeur +1)
                    
                    if borne.g2.C1.valeur == 0 :
                        valPossibles.append(borne.g2.C1.valeur +1)
                    
                    if borne.g2.C1.valeur == 9 :
                        valPossibles.append(borne.g2.C1.valeur -1)
                    
                    if borne.g2.C2.valeur == 0 :
                        valPossibles.append(borne.g2.C1.valeur +1)
                    
                    if borne.g2.C2.valeur == 9 :
                        valPossibles.append(borne.g2.C1.valeur -1)
                    
                    if borne.g2.C2.couleur == 'X':
                        valPossibles.append(max(0,borne.g2.C1.valeur-2))
                        valPossibles.append(min(borne.g2.C1.valeur+2,9))
                    
                    if borne.g2.C2.couleur != 'X':
                        borneQuasiComplete[borne.position] = True
                    
            suitesTap.append(valPossibles)
#            print("valPossible borne %i"%(borne.position), valPossibles)
        return [suitesTap, borneQuasiComplete]
        
    
    
    
    
    def chercheSuitesMain(self, no_IA):
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
                
            if carte_next.couleur == carte_prev.couleur and carte_next.valeur - carte_prev.valeur == 2:  
                #suite complète
                suitesCompletesMain.append([i-1, i, i+1])
                
            elif carte.couleur == carte_prev.couleur and carte.valeur-carte_prev.valeur == 1 : 
                try:
                    #on va chercher la première ou la dernière de la suite
                    probaTot = self.jeu.proba(no_IA)[dicoCouleur[carte.couleur]][carte.valeur] 
                    + self.jeu.proba(no_IA)[dicoCouleur[carte.couleur]][carte_prev.valeur -2]
                    -sp.binom(len(self.jeu.pioche)+6, 2)/sp.binom(len(self.jeu.pioche)+6, int(1+len(self.jeu.pioche)/2))
                
                except IndexError:   #il est impossible d'obtenir certaines cartes
                    if carte.valeur == 1:    
                        probaTot = self.jeu.proba(no_IA)[dicoCouleur[carte.couleur]][carte.valeur]
                    if carte.valeur == 9:
                        probaTot = self.jeu.proba(no_IA)[dicoCouleur[carte.couleur]][carte_prev.valeur -2]
                    
                
                #Probabilité d'obtenir la première ou dernière de la suite
                if probaTot > 0.3:
                    suitesACompleterMain.append([i-1, i])
                    

            elif carte.couleur == carte_prev.couleur and carte.valeur-carte_prev.valeur == 2:            
            #on va chercher la carte du milieu
                probaTot = self.jeu.proba(no_IA)[dicoCouleur[carte.couleur]][carte_prev.valeur]
                #Probabilité d'obtenir la carte du milieu de la suite
                if probaTot > 0.3:
                    suitesACompleterMain.append([i-1, i])

        return [suitesCompletesMain, suitesACompleterMain]
        



    
    def chercheBrelansTapis(self, no_IA):
        ### on cherche les débuts de suite déjà sur le tapis (1 ou 2 cartes)
        brelansTap = [0]*9
        
        for borne in self.jeu.ensembleBorne:
            if no_IA == 1 and borne.g1.C3.valeur != 0 and (borne.g1.C2.valeur == borne.g1.C3.valeur or borne.g1.C2.valeur == 0) and self.peutJouer(borne.position): 
                    # on a deux cartes sur la borne, qui rendent possibles un brelan
                    brelansTap[borne.position] = borne.g1.C3.valeur
                    

            if no_IA == 2 and borne.g2.C1.valeur != 0 and (borne.g2.C2.valeur == borne.g2.C1.valeur or borne.g2.C2.valeur == 0) and self.peutJouer(borne.position): 
                    # on a deux cartes sur la borne, qui rendent possibles un brelan
                    brelansTap[borne.position] = borne.g2.C1.valeur
        
        return brelansTap
    
    

    
    def strategie(self, no_IA):
        '''
        Cette fonction recherche un numero de carte qui permet de finaliser ou 
        de faire progresser une suite couleur sur le tapis. En dernier recours,
        le choix est aléatoire.
        
        
        Paramètres
        ----------
        Numéro de joueur de l'IA (1 ou 2, par défaut 2)
        
        
        Renvoie
        -------
        [no_carte, no_borne] les numeros de la carte et de la borne choisies
        '''
        
        
        [suitesCompletesMain, suitesACompleterMain, suitesTap, borneQuasiComplete] = self.chercheSuites(no_IA)
        brelansTap = self.chercheBrelansTapis(no_IA)
        
        print('\nsuitesCompletesMain ', suitesCompletesMain)
        print('\nsuitesACompleterMain ', suitesACompleterMain)
        print('\nsuitesTap ', suitesTap)
        print("\nbrelansTap ", brelansTap)
        
        CTrouve = False
        BTrouve = False
        
        #On commence par compléter d'éventuelles suites du tapis
        for noBorne in range(9):
            for valeur in suitesTap[noBorne][1:]:
                couleur = suitesTap[noBorne][0]
                for card in self:
                    if card.couleur == couleur and card.valeur == valeur:
                        no_carte = self.index(card)
                        no_borne = noBorne
                        CTrouve = True
                        BTrouve = True
        
        #Si on avait prevu de poser 3 cartes d'affilee, on le fait en priorité
        if self.no_carte_next != -1 :
            no_carte = self.no_carte_next
            no_borne = self.noBorne
            CTrouve = True
            BTrouve = True
            
            if self.no_carte_next2 != -1 :
                self.no_carte_next = self.no_carte_next2
                self.no_carte_next2 = -1
            
            else :
                self.noBorne = -1
        
        
        #Si un brelan est presque termine, on le complete
        if not CTrouve :
            noborne = 0
            while noborne < 9 and not CTrouve:                
                if brelansTap[noborne] != 0:
                    val = brelansTap[noborne]
                    for card in self:
                        if card.valeur == val:
                            no_carte = self.index(card)
                            no_borne = noborne
                            CTrouve = True
                            BTrouve = True
                noborne += 1
        
        
        
        #Si on a une suite complete en main, qu'aucune suite facile a completer ne se trouve sur le tapis
        #et que l'on avait pas commence a poser une serie de cartes, on commence a poser la nouvelle
        #On commence par verifier qu'une borne vide existe encore, sinon impossible de poser.
        if not BTrouve: 
            for noborne in range(9):
                if self.jeu.plateau.totalPoints(noborne, no_IA) == 0:
                    self.noBorne = noborne
                    no_borne = noborne
                    BTrouve = True
        
        
        if len(suitesCompletesMain) != 0 and BTrouve and not CTrouve:
            no_carte = suitesCompletesMain[0][0]
            self.no_carte_next = suitesCompletesMain[0][1]
            self.no_carte_next2 = suitesCompletesMain[0][1]
            CTrouve = True                  
                
            
        
        if not CTrouve:
            no_carte=rnd.randint(0,6)
            while not self.jeu.bonNumeroCarte(no_carte):
                no_carte=rnd.randint(0,6)
                
        if not BTrouve:    
            no_borne=0
            while no_borne < 9 and borneQuasiComplete[no_borne] and not self.peutJouer(no_borne):
                #on cherche une borne qui n'est pas complete et n'est pas proche 
                #de realiser une suite couleur
                 no_borne += 1
                 BTrouve = True
                 
            if not BTrouve:
                no_borne=(rnd.randint(0,9))
                while not self.peutJouer(no_borne):
                    no_borne = rnd.randint(0,9)
                    BTrouve = True
        
#        print("\nno_carte ", no_carte, "no_borne ", no_borne)
        return [no_carte, no_borne]
    
    
    
    
    
    def placer(self):
        
        '''
        Place la carte indiquée sur la zone de jeu de l'IA, à l'emplacement indiqué
        
        Paramètres
        ----------
        Carte choisie
        Borne visée
        '''
        no_IA = self.numero
        strat = self.strategie(no_IA)
        no_carte = strat[0]
        no_borne = strat[1]
        print('no_carte', no_carte, 'no_borne', no_borne)
        
        if no_IA == 1:
            ordonnee=self.jeu.ensembleBorne[no_borne].g1.carteCourante
            self.jeu.ensembleBorne[no_borne].g1.carteCourante-=1
        
        elif no_IA == 2:
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







