#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 14:33:50 2018

@author: quentin
"""

import sys
from PyQt5 import QtGui, QtCore, QtWidgets, uic
from ecossais import Jeu
from IA_0 import IA_0
from IA_1 import IA_1
from IA_2 import IA_2
from IA_3 import IA_3


# l'approche par héritage simple de la classe QMainWindow (même type de notre fenêtre 
# créée avec QT Designer. Nous configurons après l'interface utilisateur 
# dans le constructeur (la méthode init()) de notre classe

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        
        super(MyWindow,self).__init__()
        # Configuration de l'interface utilisateur.
        
        QtWidgets.QMainWindow.__init__(self)
        self.ui = uic.loadUi('interface.ui',self)   
        
        # Mise en place du fond d'écran
        palette= QtGui.QPalette()
        pixmap = QtGui.QPixmap("tapis.jpg")
        palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(pixmap))
        self.setPalette(palette) #background
        self.show()
        
        self.jeu = Jeu()
        
        self.carteEnCours = ""
        
        #Mise en place d'un dictionnaire pour sauvegarder les différents widgets plus simplement
        self.dictionnaire={}
        # Sauvegarde des conteneurs du côté du joueur 1 
        self.dictionnaire['J1B11'] = self.J1B11
        self.dictionnaire['J1B12'] = self.J1B12
        self.dictionnaire['J1B13'] = self.J1B13
        self.dictionnaire['J1B21'] = self.J1B21
        self.dictionnaire['J1B22'] = self.J1B22
        self.dictionnaire['J1B23'] = self.J1B23
        self.dictionnaire['J1B31'] = self.J1B31
        self.dictionnaire['J1B32'] = self.J1B32
        self.dictionnaire['J1B33'] = self.J1B33
        self.dictionnaire['J1B41'] = self.J1B41
        self.dictionnaire['J1B42'] = self.J1B42
        self.dictionnaire['J1B43'] = self.J1B43
        self.dictionnaire['J1B51'] = self.J1B51
        self.dictionnaire['J1B52'] = self.J1B52
        self.dictionnaire['J1B53'] = self.J1B53
        self.dictionnaire['J1B61'] = self.J1B61
        self.dictionnaire['J1B62'] = self.J1B62
        self.dictionnaire['J1B63'] = self.J1B63
        self.dictionnaire['J1B71'] = self.J1B71
        self.dictionnaire['J1B72'] = self.J1B72
        self.dictionnaire['J1B73'] = self.J1B73
        self.dictionnaire['J1B81'] = self.J1B81
        self.dictionnaire['J1B82'] = self.J1B82
        self.dictionnaire['J1B83'] = self.J1B83
        self.dictionnaire['J1B91'] = self.J1B91
        self.dictionnaire['J1B92'] = self.J1B92
        self.dictionnaire['J1B93'] = self.J1B93
        # Sauvegarde des conteneurs du côté du joueur 2
        self.dictionnaire['J2B11'] = self.J1B11
        self.dictionnaire['J2B12'] = self.J1B12
        self.dictionnaire['J2B13'] = self.J1B13
        self.dictionnaire['J2B21'] = self.J1B21
        self.dictionnaire['J2B22'] = self.J1B22
        self.dictionnaire['J2B23'] = self.J1B23
        self.dictionnaire['J2B31'] = self.J1B31
        self.dictionnaire['J2B32'] = self.J1B32
        self.dictionnaire['J2B33'] = self.J1B33
        self.dictionnaire['J2B41'] = self.J1B41
        self.dictionnaire['J2B42'] = self.J1B42
        self.dictionnaire['J2B43'] = self.J1B43
        self.dictionnaire['J2B51'] = self.J1B51
        self.dictionnaire['J2B52'] = self.J1B52
        self.dictionnaire['J2B53'] = self.J1B53
        self.dictionnaire['J2B61'] = self.J1B61
        self.dictionnaire['J2B62'] = self.J1B62
        self.dictionnaire['J2B63'] = self.J1B63
        self.dictionnaire['J2B71'] = self.J1B71
        self.dictionnaire['J2B72'] = self.J1B72
        self.dictionnaire['J2B73'] = self.J1B73
        self.dictionnaire['J2B81'] = self.J1B81
        self.dictionnaire['J2B82'] = self.J1B82
        self.dictionnaire['J2B83'] = self.J1B83
        self.dictionnaire['J2B91'] = self.J1B91
        self.dictionnaire['J2B92'] = self.J1B92
        self.dictionnaire['J2B93'] = self.J1B93
        
        # Sauvegarde des boutons poussoirs borne
        self.dictionnaire['B1'] = self.bouton_borne1
        self.dictionnaire['B2'] = self.bouton_borne2
        self.dictionnaire['B3'] = self.bouton_borne3
        self.dictionnaire['B4'] = self.bouton_borne4
        self.dictionnaire['B5'] = self.bouton_borne5
        self.dictionnaire['B6'] = self.bouton_borne6
        self.dictionnaire['B7'] = self.bouton_borne7
        self.dictionnaire['B8'] = self.bouton_borne8
        self.dictionnaire['B9'] = self.bouton_borne9
        
        # Sauvegarde des boutons poussoirs carte (main du joueur)
        self.dictionnaire['C1'] = self.bouton_carte1
        self.dictionnaire['C2'] = self.bouton_carte2
        self.dictionnaire['C3'] = self.bouton_carte3
        self.dictionnaire['C4'] = self.bouton_carte4
        self.dictionnaire['C5'] = self.bouton_carte5
        self.dictionnaire['C6'] = self.bouton_carte6

        # Association des fonctions aux actions du menu
        self.ui.actionJvIA0.triggered.connect(self.startJvIA0)
        self.ui.actionJvIA1.triggered.connect(self.startJvIA1)
        self.ui.actionJvIA2.triggered.connect(self.startJvIA2)
        self.ui.actionJvIA3.triggered.connect(self.startJvIA3)
        self.ui.actionIA0vIA0.triggered.connect(self.startIA0vIA0)
        self.ui.actionIA0vIA1.triggered.connect(self.startIA0vIA1)
        self.ui.actionIA0vIA2.triggered.connect(self.startIA0vIA2)
        self.ui.actionIA0vIA3.triggered.connect(self.startIA0vIA3)
        self.ui.actionIA1vIA1.triggered.connect(self.startIA1vIA1)
        self.ui.actionIA1vIA2.triggered.connect(self.startIA1vIA2)
        self.ui.actionIA1vIA3.triggered.connect(self.startIA1vIA3)
        self.ui.actionIA2vIA2.triggered.connect(self.startIA2vIA2)
        self.ui.actionIA2vIA3.triggered.connect(self.startIA2vIA3)
        self.ui.actionIA3vIA3.triggered.connect(self.startIA3vIA3)
        
        # Association des fonctions aux actions des boutons poussoirs
        
        # Menu
        self.ui.bouton_sauvegarder.clicked.connect(self.jeu.saveIHM)
        
        self.ui.bouton_nouvellePartie.clicked.connect(self.montreIA)
        self.ui.bouton_simulation.clicked.connect(self.montreIASimulation)
        
        self.ui.bouton_IA0.clicked.connect(self.startJvIA0)
        self.ui.bouton_IA1.clicked.connect(self.startJvIA1)
        self.ui.bouton_IA2.clicked.connect(self.startJvIA2)
        self.ui.bouton_IA3.clicked.connect(self.startJvIA3)
        self.ui.bouton_IA0vIA0.clicked.connect(self.startIA0vIA0)
        self.ui.bouton_IA0vIA1.clicked.connect(self.startIA0vIA1)
        self.ui.bouton_IA0vIA2.clicked.connect(self.startIA0vIA2)
        self.ui.bouton_IA0vIA3.clicked.connect(self.startIA0vIA3)
        self.ui.bouton_IA1vIA1.clicked.connect(self.startIA1vIA1)
        self.ui.bouton_IA1vIA2.clicked.connect(self.startIA1vIA2)
        self.ui.bouton_IA1vIA3.clicked.connect(self.startIA1vIA3)
        self.ui.bouton_IA2vIA2.clicked.connect(self.startIA2vIA2)
        self.ui.bouton_IA2vIA3.clicked.connect(self.startIA2vIA3)
        self.ui.bouton_IA3vIA3.clicked.connect(self.startIA3vIA3) 

        # Cartes
        self.ui.bouton_carte1.clicked.connect(self.carte1) 
        self.ui.bouton_carte2.clicked.connect(self.carte2) 
        self.ui.bouton_carte3.clicked.connect(self.carte3) 
        self.ui.bouton_carte4.clicked.connect(self.carte4) 
        self.ui.bouton_carte5.clicked.connect(self.carte5) 
        self.ui.bouton_carte6.clicked.connect(self.carte6) 
        
        # Bornes
        self.ui.bouton_borne1.clicked.connect(self.borne1) 
        self.ui.bouton_borne2.clicked.connect(self.borne2)
        self.ui.bouton_borne3.clicked.connect(self.borne3)
        self.ui.bouton_borne4.clicked.connect(self.borne4) 
        self.ui.bouton_borne5.clicked.connect(self.borne5) 
        self.ui.bouton_borne6.clicked.connect(self.borne6) 
    
        # On cache les différentes interfaces tant que le jeu n'est pas lancé
        self.ui.bouton_borne1.hide()
        self.ui.bouton_borne2.hide()
        self.ui.bouton_borne3.hide()
        self.ui.bouton_borne4.hide()
        self.ui.bouton_borne5.hide()
        self.ui.bouton_borne6.hide()
        self.ui.bouton_borne7.hide()
        self.ui.bouton_borne8.hide()
        self.ui.bouton_borne9.hide()
        
        self.ui.bouton_carte1.hide()
        self.ui.bouton_carte2.hide()
        self.ui.bouton_carte3.hide()
        self.ui.bouton_carte4.hide()
        self.ui.bouton_carte5.hide()
        self.ui.bouton_carte6.hide()
        
        self.ui.bouton_IA0.hide()
        self.ui.bouton_IA1.hide()
        self.ui.bouton_IA2.hide()
        self.ui.bouton_IA3.hide()
        
        self.ui.bouton_IA0vIA0.hide()
        self.ui.bouton_IA0vIA1.hide()
        self.ui.bouton_IA0vIA2.hide()
        self.ui.bouton_IA0vIA3.hide()
        self.ui.bouton_IA1vIA1.hide()
        self.ui.bouton_IA1vIA2.hide()
        self.ui.bouton_IA1vIA3.hide()
        self.ui.bouton_IA2vIA2.hide()
        self.ui.bouton_IA2vIA3.hide()
        self.ui.bouton_IA3vIA3.hide() 


    #Définition des fonctions de départ du jeu en fonction du mode souhaité
    
    def montreIA(self):
        self.ui.bouton_IA0.show()
        self.ui.bouton_IA1.show()
        self.ui.bouton_IA2.show()
        self.ui.bouton_IA3.show()
    
    def montreIASimulation(self):
        self.ui.bouton_IA0vIA0.show()
        self.ui.bouton_IA0vIA1.show()
        self.ui.bouton_IA0vIA2.show()
        self.ui.bouton_IA0vIA3.show()
        self.ui.bouton_IA1vIA1.show()
        self.ui.bouton_IA1vIA2.show()
        self.ui.bouton_IA1vIA3.show()
        self.ui.bouton_IA2vIA2.show()
        self.ui.bouton_IA2vIA3.show()
        self.ui.bouton_IA3vIA3.show()
    
    
    def devoilerPlateauAvecJoueur(self):
        self.ui.bouton_borne1.show()
        self.ui.bouton_borne2.show()
        self.ui.bouton_borne3.show()
        self.ui.bouton_borne4.show()
        self.ui.bouton_borne5.show()
        self.ui.bouton_borne6.show()
        self.ui.bouton_borne7.show()
        self.ui.bouton_borne8.show()
        self.ui.bouton_borne9.show()
        
        self.ui.bouton_carte1.show()
        self.ui.bouton_carte2.show()
        self.ui.bouton_carte3.show()
        self.ui.bouton_carte4.show()
        self.ui.bouton_carte5.show()
        self.ui.bouton_carte6.show()
        
    def devoilerPlateauSansJoueur(self):
        self.ui.bouton_borne1.show()
        self.ui.bouton_borne2.show()
        self.ui.bouton_borne3.show()
        self.ui.bouton_borne4.show()
        self.ui.bouton_borne5.show()
        self.ui.bouton_borne6.show()
        self.ui.bouton_borne7.show()
        self.ui.bouton_borne8.show()
        self.ui.bouton_borne9.show()

        

    def startJvIA0(self):
        self.devoilerPlateauAvecJoueur()
        self.jeu.startPvIA(0,True)
        self.bouton_carte1.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[0].couleur, self.jeu.J1[0].valeur))
        self.bouton_carte2.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[1].couleur, self.jeu.J1[1].valeur))
        self.bouton_carte3.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[2].couleur, self.jeu.J1[2].valeur))
        self.bouton_carte4.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[3].couleur, self.jeu.J1[3].valeur))
        self.bouton_carte5.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[4].couleur, self.jeu.J1[4].valeur))
        self.bouton_carte6.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[5].couleur, self.jeu.J1[5].valeur))
        
    def startJvIA1(self):
        self.devoilerPlateauAvecJoueur()
        self.jeu.startPvIA(1,True)
        self.bouton_carte1.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[0].couleur, self.jeu.J1[0].valeur))
        self.bouton_carte2.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[1].couleur, self.jeu.J1[1].valeur))
        self.bouton_carte3.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[2].couleur, self.jeu.J1[2].valeur))
        self.bouton_carte4.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[3].couleur, self.jeu.J1[3].valeur))
        self.bouton_carte5.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[4].couleur, self.jeu.J1[4].valeur))
        self.bouton_carte6.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[5].couleur, self.jeu.J1[5].valeur))
        
  
    def startJvIA2(self):
        self.devoilerPlateauAvecJoueur()
        self.jeu.startPvIA(2,True)
        self.bouton_carte1.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[0].couleur, self.jeu.J1[0].valeur))
        self.bouton_carte2.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[1].couleur, self.jeu.J1[1].valeur))
        self.bouton_carte3.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[2].couleur, self.jeu.J1[2].valeur))
        self.bouton_carte4.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[3].couleur, self.jeu.J1[3].valeur))
        self.bouton_carte5.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[4].couleur, self.jeu.J1[4].valeur))
        self.bouton_carte6.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[5].couleur, self.jeu.J1[5].valeur))
        
    def startJvIA3(self):
        self.devoilerPlateauAvecJoueur()
        self.jeu.startPvIA(3,True)
        self.bouton_carte1.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[0].couleur, self.jeu.J1[0].valeur))
        self.bouton_carte2.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[1].couleur, self.jeu.J1[1].valeur))
        self.bouton_carte3.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[2].couleur, self.jeu.J1[2].valeur))
        self.bouton_carte4.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[3].couleur, self.jeu.J1[3].valeur))
        self.bouton_carte5.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[4].couleur, self.jeu.J1[4].valeur))
        self.bouton_carte6.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[5].couleur, self.jeu.J1[5].valeur))
                
    def startIA0vIA0(self):
        self.devoilerPlateauSansJoueur()
        self.jeu.startIAvIA('0','0')
           
    def startIA0vIA1(self):
        self.devoilerPlateauSansJoueur()
        self.jeu.startIAvIA('0','1')
        
    def startIA0vIA2(self):
        self.devoilerPlateauSansJoueur()
        self.jeu.startIAvIA('0','2')

    def startIA0vIA3(self):
        self.devoilerPlateauSansJoueur()
        self.jeu.startIAvIA('0','3')
        
    def startIA1vIA1(self):
        self.devoilerPlateauSansJoueur()
        self.jeu.startIAvIA('1','1')
        
    def startIA1vIA2(self):
        self.devoilerPlateauSansJoueur()
        self.jeu.startIAvIA('1','2')
        
    def startIA1vIA3(self):
        self.devoilerPlateauSansJoueur()
        self.jeu.startIAvIA('1','3')
        
    def startIA2vIA2(self):
        self.devoilerPlateauSansJoueur()
        self.jeu.startIAvIA('2','2')
        
    def startIA2vIA3(self):
        self.devoilerPlateauSansJoueur()
        self.jeu.startIAvIA('2','3')
        
    def startIA3vIA3(self):
        self.devoilerPlateauSansJoueur()
        self.jeu.startIAvIA('3','3')
        
        
        
    # Définition des fonctions propres aux boutons poussoirs
    # Cartes dans la main => On mémorise la carte sélectionnée
    #                     => On fait disparaître la carte de la main
    #                     => On décale le reste des cartes vers la gauche
    
    def carte1(self):
        self.carteEnCours=self.jeu.J1[0]
        if len(self.pioche)>0:
            self.bouton_carte1.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[1].couleur, self.jeu.J1[1].valeur))
            self.bouton_carte2.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[2].couleur, self.jeu.J1[2].valeur))
            self.bouton_carte3.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[3].couleur, self.jeu.J1[3].valeur))
            self.bouton_carte4.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[4].couleur, self.jeu.J1[4].valeur))
            self.bouton_carte5.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[5].couleur, self.jeu.J1[5].valeur))
            self.jeu.J1.remove(self.jeu.J1[0])        
            self.bouton_carte6.hide()
        else:
            self.bouton_carte1.hide()
            
    def carte2(self):
        self.carteEnCours=self.jeu.J1[1]
        if len(self.pioche)>0:
            self.bouton_carte2.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[2].couleur, self.jeu.J1[2].valeur))
            self.bouton_carte3.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[3].couleur, self.jeu.J1[3].valeur))
            self.bouton_carte4.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[4].couleur, self.jeu.J1[4].valeur))
            self.bouton_carte5.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[5].couleur, self.jeu.J1[5].valeur))
            self.jeu.J1.remove(self.jeu.J1[1])
            self.bouton_carte6.hide()
        else:
            self.bouton_carte2.hide()
            
    def carte3(self):
        self.carteEnCours=self.jeu.J1[2]
        if len(self.pioche)>0:
            self.bouton_carte3.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[3].couleur, self.jeu.J1[3].valeur))
            self.bouton_carte4.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[4].couleur, self.jeu.J1[4].valeur))
            self.bouton_carte5.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[5].couleur, self.jeu.J1[5].valeur))
            self.jeu.J1.remove(self.jeu.J1[2])        
            self.bouton_carte6.hide()
        else:
            self.bouton_carte3.hide()
            
    def carte4(self):
        self.carteEnCours=self.jeu.J1[3]
        if len(self.pioche)>0:
            self.bouton_carte4.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[4].couleur, self.jeu.J1[4].valeur))
            self.bouton_carte5.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[5].couleur, self.jeu.J1[5].valeur))
            self.jeu.J1.remove(self.jeu.J1[3])        
            self.bouton_carte6.hide()
        else:
            self.bouton_carte4.hide()
            
    def carte5(self):
        self.carteEnCours=self.jeu.J1[4]
        if len(self.pioche)>0:
            self.bouton_carte5.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[5].couleur, self.jeu.J1[5].valeur))
            self.jeu.J1.remove(self.jeu.J1[4])        
            self.bouton_carte6.hide()
        else:
            self.bouton_carte5.hide()
            
    def carte6(self):
        self.carteEnCours=self.jeu.J1[5]
        if len(self.pioche)>0:
            self.jeu.J1.remove(self.jeu.J1[5])        
            self.bouton_carte6.hide()
        else:
            self.bouton_carte6.hide()
    
    # Bornes
    
    # => On utilise la fonction placerIHM qui ne supprime pas la carte de la main
    #    cette action étant déja faite lors des actions carte{i}
    # => On affiche la carte à l'emplacement voulu
    # => Si le groupe est complet, on désactive le bouton pour empêcher une utilisation ultérieure
    # => On pioche puis on affiche la carte piochée
    
    def borne1(self):
        self.jeu.J1.placerIHM(self.carteEnCours,0)
        self.dictionnaire['J1B{0}{1}'.format(1,self.jeu.borne1.g1.carteCourante+1)].setStyleSheet("background-image: url({0}{1}.png)".format(self.carteEnCours.couleur, self.carteEnCours.valeur))
        if self.jeu.borne1.g1.estComplet():
            self.bouton_borne1.setEnabled(False)
        self.bouton_carte6.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[5].couleur, self.jeu.J1[5].valeur))
        self.bouton_carte6.show()    
        
    def borne2(self):
        self.jeu.J1.placerIHM(self.carteEnCours,1)
        self.dictionnaire['J1B{0}{1}'.format(2,self.jeu.borne2.g1.carteCourante+1)].setStyleSheet("background-image: url({0}{1}.png)".format(self.carteEnCours.couleur, self.carteEnCours.valeur))
        if self.jeu.borne2.g1.estComplet():
            self.bouton_borne2.setEnabled(False)
        self.bouton_carte6.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[5].couleur, self.jeu.J1[5].valeur))
        self.bouton_carte6.show()
        
    def borne3(self):
        self.jeu.J1.placerIHM(self.carteEnCours,2)
        self.dictionnaire['J1B{0}{1}'.format(3,self.jeu.borne3.g1.carteCourante+1)].setStyleSheet("background-image: url({0}{1}.png)".format(self.carteEnCours.couleur, self.carteEnCours.valeur))
        if self.jeu.borne3.g1.estComplet():
            self.bouton_borne3.setEnabled(False)
        self.bouton_carte6.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[5].couleur, self.jeu.J1[5].valeur))
        self.bouton_carte6.show()
        
    def borne4(self):
        self.jeu.J1.placerIHM(self.carteEnCours,3)
        self.dictionnaire['J1B{0}{1}'.format(4,self.jeu.borne4.g1.carteCourante+1)].setStyleSheet("background-image: url({0}{1}.png)".format(self.carteEnCours.couleur, self.carteEnCours.valeur))
        if self.jeu.borne4.g1.estComplet():
            self.bouton_borne4.setEnabled(False)
        self.bouton_carte6.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[5].couleur, self.jeu.J1[5].valeur))
        self.bouton_carte6.show()
        
    def borne5(self):
        self.jeu.J1.placerIHM(self.carteEnCours,4)
        self.dictionnaire['J1B{0}{1}'.format(5,self.jeu.borne5.g1.carteCourante+1)].setStyleSheet("background-image: url({0}{1}.png)".format(self.carteEnCours.couleur, self.carteEnCours.valeur))
        if self.jeu.borne1.g1.estComplet():
            self.bouton_borne5.setEnabled(False)
        self.bouton_carte6.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[5].couleur, self.jeu.J1[5].valeur))
        self.bouton_carte6.show()
        
    def borne6(self):
        self.jeu.J1.placerIHM(self.carteEnCours,5)
        self.dictionnaire['J1B{0}{1}'.format(6,self.jeu.borne6.g1.carteCourante+1)].setStyleSheet("background-image: url({0}{1}.png)".format(self.carteEnCours.couleur, self.carteEnCours.valeur))
        if self.jeu.borne6.g1.estComplet():
            self.bouton_borne6.setEnabled(False)
        self.bouton_carte6.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[5].couleur, self.jeu.J1[5].valeur))
        self.bouton_carte6.show()
    
    def borne7(self):
        self.jeu.J1.placerIHM(self.carteEnCours,6)
        self.dictionnaire['J1B{0}{1}'.format(7,self.jeu.borne7.g1.carteCourante+1)].setStyleSheet("background-image: url({0}{1}.png)".format(self.carteEnCours.couleur, self.carteEnCours.valeur))
        if self.jeu.borne1.g1.estComplet():
            self.bouton_borne7.setEnabled(False)
        self.bouton_carte6.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[5].couleur, self.jeu.J1[5].valeur))
        self.bouton_carte6.show()
        
    def borne8(self):
        self.jeu.J1.placerIHM(self.carteEnCours,7)
        self.dictionnaire['J1B{0}{1}'.format(8,self.jeu.borne8.g1.carteCourante+1)].setStyleSheet("background-image: url({0}{1}.png)".format(self.carteEnCours.couleur, self.carteEnCours.valeur))
        if self.jeu.borne1.g1.estComplet():
            self.bouton_borne8.setEnabled(False)
        self.bouton_carte6.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[5].couleur, self.jeu.J1[5].valeur))
        self.bouton_carte6.show()
    
    def borne9(self):
        self.jeu.J1.placerIHM(self.carteEnCours,8)
        self.dictionnaire['J1B{0}{1}'.format(9,self.jeu.borne9.g1.carteCourante+1)].setStyleSheet("background-image: url({0}{1}.png)".format(self.carteEnCours.couleur, self.carteEnCours.valeur))
        if self.jeu.bouton_borne1.g1.estComplet():
            self.bouton_borne9.setEnabled(False)
        self.jeu.J1.piocher()
        self.bouton_carte6.setStyleSheet("background-image: url({}{}.png)".format(self.jeu.J1[5].couleur, self.jeu.J1[5].valeur))
        self.bouton_carte6.show()
        
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()