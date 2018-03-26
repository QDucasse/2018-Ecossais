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



class TestJeu(unittest.TestCase):

#    def testInit(self):
#        #On teste la distribution lors de la mise en place du jeu
#        
    def testVictoireFalse(self):
        #On vérifie la victoire dans les cas False TrueJ1 TrueJ2
        j=Jeu()
        j.plateau.tapis[3][:]=['J1','XX','XX','J2','J1','XX','XX','XX','XX']
        self.assertEqual(j.testVictoire()[0],False)

    def testVictoireCond1(self):
        #On vérifie la victoire dans le cas condition 1 = 5 bornes gagnées
        j=Jeu()
        j.plateau.tapis[3][:]=['J1','J1','XX','J2','J1','XX','J1','XX','J1']
        self.assertEqual(j.testVictoire()[0],True)
        self.assertEqual(j.testVictoire()[1],'VJ1')   
        
    def testVictoireCond2(self):
        #On vérifie la victoire dans le cas condition 2 = 3 bornes consécutives
        j=Jeu()
        j.plateau.tapis[3][:]=['J1','J2','J2','J2','J1','XX','XX','XX','XX']
        self.assertEqual(j.testVictoire()[0],True)
        self.assertEqual(j.testVictoire()[1],'VJ2')
#    
#    def testUnTourPvP(self):
#    
#    def testUnTourPvIA(self):
#    
#    def testUnTourIAvIA(self):
        
    
    
if  __name__  == "__main__":
    unittest.main() 

