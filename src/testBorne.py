#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 11:29:00 2018

@author: quentin
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



class TestBorne(unittest.TestCase):
    
    

    def testInit(self):
        p=Plateau(9)
        p.tapis[0][0]=Carte(1,'A')
        p.tapis[1][0]=Carte(2,'B')
        p.tapis[2][0]=Carte(3,'C')
        p.tapis[4][0]=Carte(4,'D')
        p.tapis[5][0]=Carte(5,'E')
        p.tapis[6][0]=Carte(6,'F')
        b=Borne(0,p)
        self.assertEqual(str(b.g1),str(GroupeCartes(Carte(1,'A'),Carte(2,'B'),Carte(3,'C'))))
        self.assertEqual(str(b.g2),str(GroupeCartes(Carte(4,'D'),Carte(5,'E'),Carte(6,'F'))))
        self.assertEqual(b.g1.carteCourante,2)
        self.assertEqual(b.g2.carteCourante,4)
        
    def testPeutComparerTrue(self):
        p=Plateau(9)
        p.tapis[0][0]=Carte(1,'A')
        p.tapis[1][0]=Carte(2,'B')
        p.tapis[2][0]=Carte(3,'C')
        p.tapis[4][0]=Carte(4,'D')
        p.tapis[5][0]=Carte(5,'E')
        p.tapis[6][0]=Carte(6,'F')
        b=Borne(0,p)
        #Vérification peutComparer dans un cas Vrai
        self.assertEqual(b.peutComparer(),True)
     
    
    def testPeutComparerFalse(self):
        p=Plateau(9)
        p.tapis[0][0]=Carte(0,'X')
        p.tapis[1][0]=Carte(2,'B')
        p.tapis[2][0]=Carte(3,'C')
        p.tapis[4][0]=Carte(4,'D')
        p.tapis[5][0]=Carte(5,'E')
        p.tapis[6][0]=Carte(6,'F')
        b=Borne(0,p)
        #Vérification peutComparer dans un cas Faux
        p.tapis[0][0]=Carte(0,'X')
        b=Borne(0,p)
        self.assertEqual(b.peutComparer(),False)
    
    def testComparerCondition1(self):
        p=Plateau(9)
        p.tapis[0][0]=Carte(1,'A')
        p.tapis[1][0]=Carte(2,'A')
        p.tapis[2][0]=Carte(3,'A')
        p.tapis[4][0]=Carte(4,'D')
        p.tapis[5][0]=Carte(5,'E')
        p.tapis[6][0]=Carte(6,'F')
        b=Borne(0,p)
        b.g1.calculForce()
        b.g2.calculForce()
        b.comparer()
        
        #Cas dans lequel J1 gagne, son groupe étant de force 5 contre g2 de force 2
        self.assertEqual(p.tapis[3][0],'J1')
      
    def testComparerCondition2(self):
        #Cas dans lequel les deux groupes sont de force identique => on prnd en compte le total de points
        p=Plateau(9)
        p.tapis[0][0]=Carte(1,'A')
        p.tapis[1][0]=Carte(2,'A')
        p.tapis[2][0]=Carte(3,'A')
        p.tapis[4][0]=Carte(4,'B')
        p.tapis[5][0]=Carte(5,'B')
        p.tapis[6][0]=Carte(6,'B')
        b=Borne(0,p)
        b.g1.calculForce()
        b.g2.calculForce()
        b.comparer()
        
        self.assertEqual(p.tapis[3][0],'J2')
        
    def testComparerCondition3(self):
        #Cas dans lequel les deux groupes sont de force identique => on prnd en compte le total de points
        p=Plateau(9)
        p.tapis[0][0]=Carte(1,'C')
        p.tapis[1][0]=Carte(3,'D')
        p.tapis[2][0]=Carte(3,'B')
        p.tapis[4][0]=Carte(1,'B')
        p.tapis[5][0]=Carte(3,'E')
        p.tapis[6][0]=Carte(3,'F')
        b=Borne(0,p)
        b.g1.calculForce()
        b.g2.calculForce()
        b.premierComplete=1
        b.comparer()
        
        self.assertEqual(p.tapis[3][0],'J1')
        
    def testPremierComplete(self,j=Jeu()):
        p=j.plateau
        p.tapis[0][0]=Carte(1,'C')
        p.tapis[1][0]=Carte(3,'D')
        p.tapis[2][0]=Carte(3,'B')
        p.tapis[4][0]=Carte(1,'B')
        p.tapis[5][0]=Carte(3,'E')
        p.tapis[6][0]=Carte(0,'X')
        b=Borne(0,p)
        b.verifPremierComplete(j)
        self.assertEqual(b.premierComplete,1)
        
if  __name__  == "__main__":
    unittest.main() 
