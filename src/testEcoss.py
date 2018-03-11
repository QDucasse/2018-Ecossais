#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 19:56:49 2018
@author: quentin
"""
import os
from os import chdir
chdir('D:/Users/Matthieu/Documents/Devoirs Matthieu/ENSTA BZH/Projet 2.1 Ecossais Bagarreurs/GitHub')

from ecossais import Jeu
from borne import Borne
from groupeCartes import GroupeCartes
from carte import Carte
from plateau import Plateau
from joueur import Joueur

import unittest
import numpy as np
from numpy.random import randint



class TestJoueur(unittest.TestCase):
    
    # plateau = []
    # for i in range(7):
    #     plateau.append(['  ']*9)
    # # plateau[3]=['XX','XX','XX','XX','XX','XX','XX','XX','XX']
    
    plateau = Plateau(9)
    
    partie = Jeu(plateau)
    
    Toto = Joueur(6, randint(1,3), plateau, partie)
    
    
    # def testInstance:    inutile, aucun échec possible
    #     Toto = Joueur(5, 1, plateau, partie)
    
    def testJouer(self):
        no = randint(1,6)
        abs = randint(7)
        ord = randint(7)
        
        Toto.jouer(no, (abs, ord))
        if len(self.pioche)!=0:
            self.assertEqual(6, len(Toto))
         
        
    def testPlacer(self):
        no = randint(1,6)
        abs = randint(7)
        ord = randint(7)
        
        carte = Toto[no]   
        
        
        self.assertEqual(Toto.plateau[ord][abs], '{0}{1}'.format(carte.couleur, carte.valeur))
        
        
    
    def testPeutJouer(self):
        test1 = {1:(0,0) ,1:(1,8) ,1:(2,8) ,1:(2,5) ,1:(0,8) ,2:(8,8) ,2:(7,0) ,2:(6,0) ,2:(8,0) ,2:(6,8)}
        test2 = {2:(0,0) ,2:(1,8) ,2:(2,8) ,2:(2,5) ,2:(0,8) ,1:(8,8) ,1:(7,0) ,1:(6,0) ,1:(8,0) ,1:(6,8), 2:(3,0), 2:(3,8), 1:(3,0), 1:(3,8), 2:(9,3), 2:(4,9), 1:(2,9), 1:(-1,3), 1:(0,1), 1:(2,3), 2:(7,1), 2:(6,3)}
        
        plateau = Plateau(9)
        plateau.tapis[0][1] = 'A6'
        plateau.tapis[2][3] = 'A6'
        plateau.tapis[7][1] = 'A6'
        plateau.tapis[6][3] = 'A6'
        
        
        for Jt,pos in self.test1.items():
            self.assertEqual(Joueur(5, Jt, plateau, Jeu(plateau)).peutJouer(pos), True)
            
        for Jt,pos in self.test2.items():
            self.assertEqual(Joueur(5, Jt, plateau, Jeu(plateau)).peutJouer(pos), False)
        
         
#     def testPiocher(self):
#         
# class TestCarte(unittest.TestCase):
#     def testInstance(self):
#     
# class TestPlateau(unittest.TestCase):
#    def testInstance(self):
#    
# class TestBorne(unittest.TestCase):
#     def testInstance(self):
#     def testComparer(self):
#     def testRafraichir(self):
#     
#    
# class TestGroupeCartes(unittest.TestCase):
#     def testInstance(self):
#     def testCalculForce(self):
#     
#    
# class TestJeu(unittest.TestCase):
#     def testInstance(self):
#     def testRafraichissementIntegral(self):
#     def testTestVictoire(self):
#     def testUnTour(self):


# if  __name__  == "__main__":
#     unittest.main() 

