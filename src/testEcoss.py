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
    # plateau[3]=['XX','XX','XX','XX','XX','XX','XX','XX','XX']
    
    plateau = Plateau(9)
    
    partie = Jeu(plateau)
    
    Toto = Joueur(6, 1, plateau, partie)
    
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
        
        with self.assertRaises(Exception) as err1:
            Toto.placer(no, (ord, abs))
        
        with self.assertRaises(Exception) as err2:
            Toto.placer(randint(1,6), (abs, ord))
        self.assertTrue('Emplacement occupé' in err2.exception)
        
        
        self.assertEqual(Toto.plateau[ord][abs], '{0}{1}'.format(carte.couleur, carte.valeur))
        
        
        
        
        
     def testPeutJouer(self):
         
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
