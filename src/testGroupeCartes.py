#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 20:56:57 2018

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



class TestGroupeCartes(unittest.TestCase):
    
    def testInitVide(self):
        c1=Carte(0,'X')
        c2=Carte(0,'X')
        c3=Carte(0,'X')
        g=GroupeCartes(c1,c2,c3)
        self.assertEquals(g.totalPoints,0)
    
    def testInit(self):
        c1=Carte(1,'A')
        c2=Carte(2,'B')
        c3=Carte(3,'C')
        g=GroupeCartes(c1,c2,c3)
        self.assertEquals(g.totalPoints,6)
        
        
    def testEstCompletFaux(self):
        c1=Carte(0,'X')
        c2=Carte(0,'X')
        c3=Carte(0,'X')
        g=GroupeCartes(c1,c2,c3)
        self.assertEquals(g.estComplet(),False)
        
    def testEstCompletVrai(self):
        c1=Carte(1,'A')
        c2=Carte(2,'B')
        c3=Carte(3,'C')
        g=GroupeCartes(c1,c2,c3)
        self.assertEquals(g.estComplet(),True)
        
    def testCalculForce5(self):
        c1=Carte(1,'A')
        c2=Carte(2,'A')
        c3=Carte(3,'A')
        g=GroupeCartes(c1,c2,c3)
        g.calculForce()
        self.assertEquals(g.force,5)
        
    def testCalculForce4(self):
        c1=Carte(1,'A')
        c2=Carte(1,'B')
        c3=Carte(1,'C')
        g=GroupeCartes(c1,c2,c3)
        g.calculForce()
        self.assertEquals(g.force,4)

    def testCalculForce3(self):
        c1=Carte(1,'A')
        c2=Carte(5,'A')
        c3=Carte(7,'A')
        g=GroupeCartes(c1,c2,c3)
        g.calculForce()
        self.assertEquals(g.force,3)
        
    def testCalculForce2(self):
        c1=Carte(1,'A')
        c2=Carte(2,'B')
        c3=Carte(3,'C')
        g=GroupeCartes(c1,c2,c3)
        g.calculForce()
        self.assertEquals(g.force,2)
        
    def testCalculForce1(self):
        c1=Carte(1,'E')
        c2=Carte(6,'B')
        c3=Carte(3,'C')
        g=GroupeCartes(c1,c2,c3)
        g.calculForce()
        self.assertEquals(g.force,1)
        
    def testCalculForce0(self):
        c1=Carte(0,'X')
        c2=Carte(2,'B')
        c3=Carte(3,'C')
        g=GroupeCartes(c1,c2,c3)
        g.calculForce()
        self.assertEquals(g.force,0)
        
if  __name__  == "__main__":
    unittest.main() 
