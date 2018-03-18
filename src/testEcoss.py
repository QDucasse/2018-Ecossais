#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 19:56:49 2018
@author: matthieu
"""


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

    
    def testJouer(self):
        j=Jeu()
        Toto = Joueur(6, randint(1,3), j)
        for i in range(Toto.taille):
            Toto.piocher()          
        no = randint(0,6)
        abs = randint(8)
        ord = randint(6)
        position = (abs, ord)
        
        Toto.jouer(no,position)
        if len(j.pioche)!=0:
            self.assertEqual(6,len(Toto))
        
        
    def testPlacer(self):
        j=Jeu()
        joueur1 = Joueur(6,1,j)
        joueur1.piocher()
        strCarte=str(joueur1[0])
        joueur1.placer(0,(0,0))
        self.assertEqual(str(j.plateau.tapis[0][0]),strCarte)
    

         
    def testPeutJouerPositionMauvaisType1(self):
         j=Jeu()
         j.joueurCourant=1
         self.assertEqual(j.J1.peutJouer(4),False)
         
    def testPeutJouerPositionMauvaisType2(self):
         j=Jeu()
         j.joueurCourant=1
         self.assertEqual(j.J1.peutJouer('a'),False)
    
    def testPeutJouerPositionMauvaisJoueur(self):
         j=Jeu()
         j.joueurCourant=1
         self.assertEqual(j.J1.peutJouer((4,0)),False)
         
    def testPeutJouerPositionOccupee(self):
        j=Jeu()
        j.joueurCourant=1
        plateau = j.plateau
        plateau.tapis[0][0]=Carte(1,'A')
        self.assertEqual(j.J1.peutJouer((0,0)),False)
        
         
    def testPeutJouerPositionBorne(self):
        j=Jeu()
        j.joueurCourant=1
        self.assertEqual(j.J1.peutJouer((3,0)),False)
       
    def testPeutJouerTrue(self):
        j=Jeu()
        j.joueurCourant=1
        self.assertEqual(j.J1.peutJouer((0,0)),True)
        
        
#    def testPeutJouer(self):
#        j=Jeu()
#        plateau = j.plateau
#        
#        j=Jeu()
#        plateau = j.plateau
#        
#        testJ11 = [(0,0) ,(1,8) ,(2,8) ,(2,5) ,(0,8)]
#        testJ21 = [(6,8) ,(5,0) ,(6,0) ,(4,8) ,(4,0)]
#        testJ12 = [(6,8), (5,0), (6,0), (4,8), (4,0), (0,1), (2,3), (2,9), (-1,3), (0,1), (2,3)]
#        testJ22 = [(0,0), (1,8), (2,8), (2,5), (0,8), (3,0), (3,8), (9,3), (4,9), (6,1), (4,3)]
#        
#        plateau.tapis[0][1] = Carte(6,'A')
#        plateau.tapis[2][3] = Carte(6,'A')
#        plateau.tapis[6][1] = Carte(6,'A')
#        plateau.tapis[4][3] = Carte(6,'A')
#        
#        J1 = Joueur(6, 1, j)
#        J2 = Joueur(6, 2, j)
#        
#        
#        for pos in testJ11:
#            self.assertEqual(J1.peutJouer(pos), True)
#            
#        for pos in testJ21:
#            self.assertEqual(J2.peutJouer((4,4)),True)
#            
#        for pos in testJ12:
#            self.assertEqual(J1.peutJouer(pos), False)
#            
#        for pos in testJ22:
#            self.assertEqual(J2.peutJouer(pos), False)
            
        
         
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


if  __name__  == "__main__":
    unittest.main() 

